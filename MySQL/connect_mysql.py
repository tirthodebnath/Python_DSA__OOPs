import mysql.connector


conn = mysql.connector.connect(
    host='localhost:3306',
    user='root',
    password='root',
    database='new_schema1'  # Replace 'your_database_name' with the actual name of your database
)

my_cursor=conn.cursor()
conn.commit()
conn.close()
print("Connection Closed.")
