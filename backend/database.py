import sqlite3

def get_connection():
    conn = sqlite3.connect("neurostek.db")
    return conn

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
