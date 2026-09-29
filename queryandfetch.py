import sqlite3

conn = sqlite3.connect('hello.db')

# create a cursor
c = conn.cursor()  # it is use to say the function to do something.

# Query the database

c.execute("SELECT * FROM customers")

# print(c.fetchone()) 
# print(c.fetchone()[1])

# print(c.fetchmany(2))

# print(c.fetchall())
item = c.fetchall()

print("NAMES" + "\t\tEMAILS")
print("--------" + "\t--------")

for item in item:
    print(item[0] + " " + item[1] + " \t " + item[2])

# print("Command sucessfully executed.....")

conn.commit()

conn.close()