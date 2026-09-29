import sqlite3

conn =  sqlite3.connect('hello.db')

c = conn.cursor()

# c.execute("SELECT rowid, * FROM customers")
c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE '%Tom'")

items = c.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()