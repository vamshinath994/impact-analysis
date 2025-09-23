# Data/storage logic for Compliance Dashboard

import sqlite3
from typing import Any, List

DB_PATH = 'compliance_dashboard.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    # Example: create a table for policies
    c.execute('''CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()
