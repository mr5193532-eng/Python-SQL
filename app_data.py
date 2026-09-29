import sqlite3

# Query the app_data and show all records.
def show_all():

    conn = sqlite3.connect('hello.db')

    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")

    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()

# A a new record to table.
def add_one(first, last, email):
    conn = sqlite3.connect('hello.db')
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES(?,?,?)", (first, last, email))

    conn.commit()
    conn.close()

# Add many records in table.
def add_many(list):
    conn = sqlite3.connect('hello.db')
    c = conn.cursor()
    
    c.executemany("INSERT INTO customers VALUES(?,?,?)", (list))
    
    conn.commit()
    conn.close()

# Delete record from table.
def delete_one(id):
    conn = sqlite3.connect('hello.db')
    c = conn.cursor()

    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    
    conn.commit()
    conn.close()

# Lookup where.
def data_lookup(email):
    conn = sqlite3.connect('hello.db')
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))

    items = c.fetchall()
    for item in items:
        print(item)
    
    conn.commit()
    conn.close()