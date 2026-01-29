import sqlite3

connection = sqlite3.connect('02_SQLite\\movies.db')
cursor = connection.cursor()

# cursor.execute(
#     """INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976)""")
cursor.execute("""SELECT * FROM Movies""")

print(cursor.fetchone())

connection.commit()
connection.close()