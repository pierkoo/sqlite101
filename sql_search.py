import sqlite3

commands = ["AVG",
             "MAX",
             "MIN",
             "SUM",
             "EXIT"
]

prompt = """Welcome in aggregation sample program
Please choose type of operation jou want oto perform:
AVG - average of numbers in the table
MAX - maxiumum number in the table
MIN - minimum number in the table
SUM - sum of numbers
To exit program type: EXIT.\n"""
print(prompt)

while True:
    command_choice = input("Type your choice:").upper()
    if command_choice in commands:
        if command_choice == "EXIT":
            exit()
        break
    else:
        print("Incorect command!")


query = f"SELECT {command_choice}(num) FROM numbers"

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()
    try:
        c.execute(query)
    except sqlite3.OperationalError:
        print("Table numbers is missing from database. Plese execute sql_insert.py file first.")
        exit()
    result = c.fetchone()
    if result[0] != None:
        print(f"Result of performing {command_choice} operation is {result[0]}")
    else:
        print(f"There aren't any numbers in the table to perform {command_choice} operation with! Please execute sql_insert.py file first.")


