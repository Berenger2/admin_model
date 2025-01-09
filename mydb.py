import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# database
dataBase = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port,
)

cursor = dataBase.cursor()

cursor.execute(f"CREATE DATABASE {db_name}")
print("Database created successfully!")