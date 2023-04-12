import sqlite3

connection = sqlite3.connect('mom_db.db')

with open('schema_mom.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
