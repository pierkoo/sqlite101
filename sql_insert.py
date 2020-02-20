import random
import sqlite3

random_nums = [(random.randint(0,100),) for e in range(100)]

with  sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers (num INT)")
    c.executemany("INSERT INTO numbers (num) VALUES(?)", random_nums)




