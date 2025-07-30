# pipeline/main.py

import argparse
import importlib
import logging
from pathlib import Path
import sys
import uuid
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ica_std_lib.databricks_runner import DatabricksJobRunner
from ica_std_lib.pyodbc_mssql_connector import PyodbcMsSqlConnector
from ica_std_lib.extract_writer import ExtractWriter
from ica_std_lib.payload_writer import PayloadWriter
from ica_std_lib.storage_uploader import StorageUploader
from ica_std_lib.merge_type import MergeType
from ica_std_lib.key_vault_reader import get_secret_from_key_vault

job_config = {
    "Job1": MergeType.UPSERT,
    "Job2": MergeType.OVERWRITE,
    "Job3": MergeType.APPEND,
    # Add more as needed
}

RUN_ID = str(uuid.uuid4())

class RunIdFilter(logging.Filter):
    """Custom logging filter to add a unique run ID to each log message."""
    def filter(self, record):
        record.run_id = RUN_ID
        return True

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="RunID: %(run_id)s %(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logging.getLogger("azure").setLevel(logging.WARNING)
    logging.getLogger("msal").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    run_id_filter = RunIdFilter()
    logging.getLogger().addFilter(run_id_filter)

def parse_command_args():
    try:
        parser = argparse.ArgumentParser(description="Run a data extraction job.")
        parser.add_argument("--job_name", required=True, help="The name of the job to execute.")
        args = parser.parse_args()

        if not args.job_name:
            logging.error("Job name cannot be empty.")
            raise ValueError("Job name cannot be empty.")

        return args

    except SystemExit as e:
        logging.error("Error parsing command line arguments. Ensure required arguments are provided.")
        raise

def get_job_definition(job_name):
    """
    Dynamically imports and instantiates a job definition class by name.
    :param job_name: The name of the job to process (must match a class name in the ica_job_defs module)
    :return: An instance of the job definition class
    """
    try:
        logging.info(f"Processing job name: {job_name}")
        job_module = importlib.import_module(f"ica_job_defs.{job_name}")
        job_cls = getattr(job_module, job_name)
        job_def = job_cls()

        if not job_def:
            raise ValueError(f"Failed to initialize job definition for job: {job_name}")

        return job_def

    except (AttributeError, ModuleNotFoundError) as e:
        raise ValueError(f"Job definition class '{job_name}' could not be found or imported.") from e

    except Exception as e:
        raise ValueError(f"An error occurred while initializing the job definition for job: {job_name}") from e

def extract_data(connector, job_def, download_path, upload_path, merge_type):
    result = None
    try:
        result = connector.execute_query(job_def.query)

        writer = ExtractWriter(
            job_def.database_name,
            job_def.dataset_name,
            download_path,
            row_batch=50
        )
        files_written = writer.write(result)

        payload_writer = PayloadWriter(download_path, upload_path)
        payload_file_name = payload_writer.write(
            job_def.database_name,
            job_def.dataset_name,
            result.description,
            files_written,
            merge_type
        )
        files_written.append(payload_file_name)
        return files_written

    finally:
        if result:
            result.close()

def upload_extract(download_path, extract_file_list, storage_account_name, storage_container_name, storage_sas_token):
    try:
        uploader = StorageUploader(storage_account_name, storage_container_name, storage_sas_token)
        uploader.upload_csv_to_azure(download_path, extract_file_list)
    except Exception as e:
        logging.error(f"Error uploading files to storage: {e}")
        raise

def main():
    configure_logging()
    logging.info("Starting the data extraction job.")

    try:
        for job_name, merge_type in job_config.items():
            logging.info(f"Running job: {job_name} with merge type: {merge_type.name}")

            job_def = get_job_definition(job_name)

            storage_account_name = get_secret_from_key_vault("lcastd-landing-name")
            storage_container_name = get_secret_from_key_vault("lcastd-landing-container")
            storage_sas_token = get_secret_from_key_vault("lcastd-landing-sas")
            con_string = get_secret_from_key_vault(job_def.database_cnn)

            download_path = Path("\\\\ms.ds.uhc.com\\userdata\\053\\tdebnath\\Desktop\\AirFlow_Dag\\LCA-StandardDataPull")
            upload_path = f"/mnt/{storage_container_name}/landing/"

            extract_file_list = None

            with PyodbcMsSqlConnector(con_string) as connector:
                extract_file_list = extract_data(connector, job_def, download_path, upload_path, merge_type)  # Pass merge type

            if extract_file_list:
                upload_extract(
                    download_path,
                    extract_file_list,
                    storage_account_name,
                    storage_container_name,
                    storage_sas_token
                )

                payload_file = f"{upload_path}/{extract_file_list[-1]}"
                runner = DatabricksJobRunner()
                runner.submit_databricks_job(payload_file)
            else:
                logging.warning(f"No files to process for job: {job_name}. Skipping upload and processing.")


    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

    logging.info("Data extraction job completed successfully.")
    sys.exit(0)

if __name__ == "__main__":
    main()
