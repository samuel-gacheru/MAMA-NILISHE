import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:') # create a database in memory
        print(f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE dishes (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        print("Table created successfully")
    except Error as e:
        print(e)

def insert_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Biriani", 1250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Tamarind Fish", 1500))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Ugali ya Nazi", 250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Viazi Karai", 1250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Kaimati", 150))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Mahamri", 150))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Biriani", 1000))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Vitumbua", 1250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("kuku wa choma", 2250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Bagia", 1250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Mkate wa ufuta", 550))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Matoke", 850))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Kachumbari", 150))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Mshikaki", 650))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Chapati", 50))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Maharage ya nazi ", 250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Wali wa nazi", 250))
        cursor.execute("INSERT INTO dishes (name, price) VALUES (?, ?)",
                       ("Dagaa wa nazi", 1050))
        
        
        conn.commit()
        print("Records created successfully")
    except Error as e:
        print(e)

def select_all_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dishes")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        insert_data(conn)
        select_all_data(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()