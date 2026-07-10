import sqlite3
from datetime import datetime

DB_NAME = "proofpixels.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            content TEXT,
            prediction TEXT,
            score REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_result(content_type, content, prediction, score):
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        "INSERT INTO history (type, content, prediction, score, timestamp) VALUES (?, ?, ?, ?, ?)",
        (content_type, content, prediction, score, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def get_history(limit=50):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute(
        "SELECT type, content, prediction, score, timestamp FROM history ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows