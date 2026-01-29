import sqlite3

# Connection object instantiate a connection with the database
# If the database doesn't exists yet, it will be created in the first time we run it
connection = sqlite3.connect('02_SQLite\\movies.db')

# Cursor object allows us to execute commands and queries in the DB
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)""")

connection.commit() # Commit changes
connection.close() # Closes connection