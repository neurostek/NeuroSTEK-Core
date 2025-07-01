import sqlite3

def get_connection():
    return sqlite3.connect("neurostek.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        gender TEXT,
        birth_date TEXT,
        tokens INTEGER DEFAULT 200
    )
    """)

    conn.commit()
    conn.close()
