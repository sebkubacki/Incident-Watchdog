import sqlite3

def create_connection():
    con = sqlite3.connect("database/incidents.db")
    return con

create_table = """
    CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT,
    timestamp TEXT,
    status TEXT,
    module TEXT,
    event TEXT
    )"""

def create_tables(con):
    con.execute(create_table)

con = create_connection()
create_tables(con)
con.commit()
print("END")
