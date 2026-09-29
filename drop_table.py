import sqlite3

conn = sqlite3.connect('hello.db')

c = conn.cursor()

#  DROP TABLE
# c.execute("DROP TABLE customers")
# (I am not yet dropping this table because this command deletes my table.)
# conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()