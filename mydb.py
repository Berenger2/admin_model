import mysql.connector

# Establish a connection to the database
dataBase = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    port = '3306',

    # database="your_database"
)

# Prepare cursor object
cursor = dataBase.cursor()

# Create a database
cursor.execute("CREATE DATABASE mod_admin")
print("Database created successfully!")