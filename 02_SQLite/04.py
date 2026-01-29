import sqlite3

connection = sqlite3.connect('02_SQLite\\movies.db')
cursor = connection.cursor()

famous_films = [
    ("Pulp Fiction", "Quentin Tarantino", 1994),
    ("Back to the Future", "Robert Zemeckis", 1985),
    ("Moorise Kingdom", "Wes Anderson", 2012),
]

# cursor.executemany("INSERT INTO Movies VALUES (?,?,?)", famous_films)
cursor.execute("SELECT * FROM Movies")

print(cursor.fetchall())

connection.commit()
connection.close()