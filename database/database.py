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


device = 'ATM001'
timestamp = '2026-06-09 06:49:55'
status = 'ERROR'
module = 'NETWORK'
event = 'CONNECTION LOST'

values = (
        device,
        timestamp,
        status,
        module,
        event
    )   

sql = """
    INSERT INTO incidents (
        device_id,
        timestamp,
        status,
        module,
        event
    ) VALUES (?, ?, ?, ?, ?)
"""



con = create_connection()
#create_tables(con)
con.execute(sql, values)
con.commit()
print("END")
