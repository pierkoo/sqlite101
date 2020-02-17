# Creating a SQLite3 database and table

import sqlite3
with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()

    cursor.execute("INSERT INTO population VALUES ('New York city', \
                    'NY', 8400000)")
    cursor.execute("INSERT INTO population VALUES ('San Francisco', \
                    'CA', 800000)")


