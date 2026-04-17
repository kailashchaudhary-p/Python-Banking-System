import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
        acc_no INTEGER PRIMARY KEY,
        name TEXT,
        pin TEXT,
        balance REAL
    )
    """)
    conn.commit()

def close_connection():
    conn.close()