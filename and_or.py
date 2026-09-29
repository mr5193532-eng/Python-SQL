import sqlite3

conn = sqlite3.connect('hello.db')

c = conn.cursor()

# AND FUNCTION
c.execute("SELECT rowid, * FROM  customers WHERE first_name LIKE '%Billie' AND rowid = 3")

# OR FUNCTION
c.execute("SELECT rowid, * FROM  customers WHERE first_name LIKE '%Billie' OR rowid = 3")

items = c.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()