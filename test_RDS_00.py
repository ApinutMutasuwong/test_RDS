import mysql.connector
from mysql.connector import pooling


import mysql.connector

# Replace these values with your own database credentials
db_config = {
    host="poopdb.ctdl0ufcmt9o.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Poopprom",
    database="poopdb"
}

# Establish a connection to the MySQL database
connection = mysql.connector.connect(**db_config)

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
query = "SELECT * FROM example_table"
cursor.execute(query)

# Fetch and print the data
for row in cursor.fetchall():
    print(row)

# Close the cursor and the connection
cursor.close()
connection.close()
