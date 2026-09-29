import sqlite3

conn = sqlite3.connect('hello.db')

# create a cursor
c = conn.cursor()  # it is use to say the function to do something.

# creating a table
c.execute(""" CREATE TABLE IF NOT EXISTS customers(
        first_name text,
        last_name text,
        email text
    )""")

many_customers = [
    ('Jhon', 'bricks', 'world@james.com'),
    ('Billie', 'Eilish', 'billie@gmail.com'),
    ('Tom', 'Holand', 'tom@gmail.com'),
    ('Tom', 'Cruise', 'tom@gmail.com')
    ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


print("Command sucessfully executed.....")


# DATA TYPES:
# 1. NULL      (It is use for nothing exist)
# 2. Integer   (It is use for numbers means any whole number)
# 3. real      (It is use for decimal numbers)
# 4. text      (It is use for any simple text)
# 5. blob      (It is use for binary pictures)

conn.commit()

conn.close()