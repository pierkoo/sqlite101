import sqlite3

with sqlite3.connect("cars.db") as conn:
    cursor = conn.cursor()
    try:
        create_table = """ CREATE TABLE inventory (Make TEXT,
                                                   Model TEXT,
                                                   Quantity INT
                                                  )"""
        cursor.execute(create_table)
    except:
        pass

    cars = [
        ("Ford", "Mustang", 2),
        ("Ford", "Escort", 14),
        ("Ford", "Anglia", 8),
        ("Honda", "Civic", 7),
        ("Honda", "S2000", 3)
    ]

    # cursor.executemany("INSERT INTO inventory VALUES (?,?,?)", cars)

    # cursor.execute("UPDATE inventory SET quantity = 4 WHERE Make='Honda' and Model='S2000'")

    # cursor.execute("UPDATE inventory SET quantity = 17 WHERE Make='Ford' and Model='Escort'")

    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    for r in rows:
        print(r)

    cursor.execute("SELECT * FROM inventory where Make='Ford'")
    rows = cursor.fetchall()
    print("\nOnly FORD's\n")
    for r in rows:
        print(f"{r[0]} {r[1]} - quantity: {r[2]}")

    # cursor.execute("""CREATE TABLE orders
    #                 (Make TEXT, Model TEXT, order_date DATE)""")

    orders = [
        ('Ford', 'Escort', '2014-01-22'),
        ('Ford', 'Escort', '2014-01-23'),
        ('Ford', 'Escort', '2014-01-24'),
        ('Honda', 'Civic', '2014-01-25'),
        ('Honda', 'Civic', '2014-01-26'),
        ('Honda', 'Civic', '2014-01-27'),
        ('Ford', 'Mustang', '2014-01-28'),
        ('Ford', 'Mustang', '2014-01-22'),
        ('Ford', 'Mustang', '2014-01-23'),
        ('Honda', 'S2000', '2014-01-24'),
        ('Honda', 'S2000', '2014-01-25'),
        ('Honda', 'S2000', '2014-01-26'),
        ('Ford', 'Anglia', '2014-01-27'),
        ('Ford', 'Anglia', '2014-01-28'),
        ('Ford', 'Anglia', '2014-01-22'),
         ]

    # cursor.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)

    rows = cursor.execute("SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date FROM inventory INNER JOIN orders ON inventory.model=orders.model")

    # for r in rows:
    #     print(*r[0:2])
    #     print(r[2])
    #     print(r[3])
    #     print()

    """Using the COUNT() function, calculate the total number of orders for each make and model."""
    print()
    cursor.execute("SELECT model FROM inventory")
    models = cursor.fetchall()
    for model in models:
        model=model[0]
        cursor.execute(f"SELECT count(order_date) FROM orders WHERE model='{model}'")
        result = cursor.fetchone()[0]
        print(f"For {model} there are {result} orders")


    """Output the car's make and model on one line, the quantity on another line, and then
    the order count on the next line."""

    print()
    cursor.execute("SELECT model FROM inventory")
    models = cursor.fetchall()

    for model in models:
        model=model[0]
        cursor.execute(f"SELECT count(orders.order_date), orders.make, inventory.quantity FROM orders JOIN inventory ON orders.model=inventory.model WHERE orders.model='{model}'")


        result = cursor.fetchone()
        print(result[1],model)
        print(f"Quantity: {result[2]}")
        print(f"Orders: {result[0]}")
        print()
