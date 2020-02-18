# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("SELECT firstname, lastname FROM employees")

    rows = c.fetchall()

    # for r in rows:
    #     print(r[0], r[1])
    c.execute("UPDATE population SET population = 9000000 WHERE city='New York City'")

    c.execute("DELETE FROM population WHERE city='Boston'")
    c.execute("SELECT * FROM population")

    result = c.fetchall()
    for r in result:
        print(r)
