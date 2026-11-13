"""SQLite history repository with no import-time side effects."""
from __future__ import annotations
import sqlite3
import threading
from pathlib import Path

SCHEMA = """CREATE TABLE IF NOT EXISTS incidents (
id INTEGER PRIMARY KEY AUTOINCREMENT, device_id TEXT NOT NULL, device_type TEXT,
timestamp TEXT NOT NULL, status TEXT NOT NULL, module TEXT NOT NULL, event TEXT NOT NULL)"""

class Repository:
    def __init__(self, path="database/incidents.db"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._local = threading.local()
        connection = self._connection()
        columns = {row[1] for row in connection.execute("PRAGMA table_info(incidents)")}
        if "device_type" not in columns:
            connection.execute("ALTER TABLE incidents ADD COLUMN device_type TEXT")
            connection.commit()

    def _connection(self):
        if not hasattr(self._local, "connection"):
            connection = sqlite3.connect(self.path, timeout=5)
            connection.row_factory = sqlite3.Row
            connection.execute(SCHEMA)
            connection.commit()
            self._local.connection = connection
        return self._local.connection

    def record(self, event):
        connection = self._connection()
        connection.execute(
            "INSERT INTO incidents (device_id, device_type, timestamp, status, module, event) VALUES (?, ?, ?, ?, ?, ?)",
            (event["device"], event.get("device_type"), event["timestamp"], event["status"], event["module"], event["event"]))
        connection.commit()

    def recent(self, limit=20):
        return list(self._connection().execute("SELECT * FROM incidents ORDER BY id DESC LIMIT ?", (limit,)))

    def count(self):
        return self._connection().execute("SELECT COUNT(*) FROM incidents").fetchone()[0]

    def close(self):
        if hasattr(self._local, "connection"):
            self._local.connection.close()
