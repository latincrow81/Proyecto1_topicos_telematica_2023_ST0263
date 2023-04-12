import sqlite3


# Add your own utility classes and functions here.

def get_db_connection():
    conn = sqlite3.connect('../mom_db.db')
    conn.row_factory = sqlite3.Row
    return conn
