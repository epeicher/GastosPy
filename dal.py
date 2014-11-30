import sqlite3

DB_NAME = 'data/expenses.db'


def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS movements
        (
            id INTEGER PRIMARY KEY,
            dateValue TEXT,
            concept TEXT,
            amount REAL,
            balance REAL,
            category_id INTEGER,
            account_id INTEGER
        );
        ''')
    c.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS
        IX_UNIQUE_TRANSACTION
        ON movements(dateValue, concept, amount);''')

    conn.commit()
    conn.close()


def save_movements(m):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.executemany('INSERT OR IGNORE INTO movements (dateValue, concept, amount, balance) VALUES (?,?,?,?)', m)
    conn.commit()
    conn.close()
