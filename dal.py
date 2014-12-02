import sqlite3
import csv

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
            accountName TEXT,
            category_id INTEGER
        );
        ''')
    c.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS
        IX_UNIQUE_TRANSACTION
        ON movements(dateValue, concept, amount, accountName);''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS categories
        (
            id INTEGER PRIMARY KEY,
            category TEXT,
            value TEXT UNIQUE
        )
        ''')

    seed_categories(conn)

    conn.commit()
    conn.close()


def unicode_csv_reader(unicode_csv_data):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(unicode_csv_data)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]


def seed_categories(conn):
    l_cat = []
    with open('categories.csv','rb') as csvfile:
        spamreader = unicode_csv_reader(csvfile)
        for val,cat in spamreader:
            l_cat.append((cat,val))

    cur = conn.cursor()
    cur.executemany('''INSERT INTO categories (category, value) VALUES (?,?)''',l_cat)


def save_movements(m):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.executemany('''INSERT OR IGNORE INTO movements (dateValue, concept, amount, balance, accountName)
                    VALUES (?,?,?,?,?)''', m)
    conn.commit()
    conn.close()


def update_movements(m):
    conn = sqlite3.connect(DB_NAME)
    conn.executemany('UPDATE movements SET category_id = ? WHERE id = ?',m)
    conn.commit()
    conn.close()


def get_categories():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT * FROM categories')
    rows = cur.fetchall()
    return rows


def get_uncategorized_movements():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT * FROM movements WHERE category_id IS NULL')
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    initialize_db()
