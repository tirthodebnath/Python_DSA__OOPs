import csv

# Column names
columns = ['TDL_ID', 'TX_ID', 'PERIOD', 'ORIG_POST_DATE', 'ORIG_SERVICE_DATE', 'AMOUNT', 'AR_AMOUNT', 'PATIENT_AMOUNT', 'INSURANCE_AMOUNT', 'BAD_DEBT_AR_AMOUNT', 'CREDIT_FLAG', 'SERV_AREA_ID', 'DEPARTMENT_RECORD_ID', 'LOCATION_ID', 'PLACE_OF_SERVICE_ID', 'PROVIDER_ID_', 'DIAGNOSIS_ONE_ID', 'DIAGNOSIS_TWO_ID', 'DIAGNOSIS_THREE_ID', 'DIAGNOSIS_FOUR_ID', 'DIAGNOSIS_FIVE_ID', 'DIAGNOSIS_SIX_ID', 'PROCEDURE_ID', 'TRAN_CODE', 'ORGINAL_PAYOR_ID', 'ORIGINAL_FIN_CLASS', 'CURRENT_PAYOR_ID', 'CURRENT_FIN_CLASS', 'WORK_RVU', 'TOTAL_RVU', 'QUANTITY', 'Load_Date', 'Transaction']

# File path to save the CSV file
file_path = r'C:\Users\user\OneDrive\Desktop\EXL_NEW_CSV_Files\APND_PB_TRANSACTION_SUMMARY.csv'

# Writing data into the CSV file
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)

print("CSV file created successfully at:", file_path)
