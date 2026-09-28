import sqlite3

db_connection=sqlite3.connect("iris.db")
#cursor object
cursor = db_connection.cursor()

createTable=""" create table if not exists irisData (
sepal_id INTEGER PRIMARY KEY AUTOINCREMENT,
sepal_length REAL NOT NULL,
sepal_width REAL NOT NULL,
petal_length REAL NOT NULL,
petal_width REAL NOT NULL,
class INTEGER NOT NULL
)
"""
cursor.execute(createTable)
db_connection.commit()
