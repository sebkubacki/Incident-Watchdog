import sqlite3
from live_monitoring.generator import generate_event


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

def insert_incident(con, log_data):

    sql = """
        INSERT INTO incidents (
            device_id,
            timestamp,
            status,
            module,
            event
        ) VALUES (?, ?, ?, ?, ?)
        """
    values = (
            log_data['device'],
            log_data['timestamp'],
            log_data['status'],
            log_data['module'],
            log_data['event']
        )
    con.execute(sql, values)

def get_all_incidents():
    doit = "SELECT * FROM incidents"
    result = con.execute(doit)
    return result.fetchall()


log_data = generate_event()
con = create_connection()
insert_incident(con, log_data)
incidents = get_all_incidents()
con.commit()
print(incidents)

