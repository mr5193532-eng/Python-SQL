import sqlite3

conn = sqlite3.connect('hello.db')

c = conn.cursor()

# update records
# c.execute("""UPDATE customers SET first_name = 'Kerlin'
#             WHERE rowid = 1

#     """)

# delete records
c.execute("DELETE FROM customers WHERE rowid = 4")

conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()