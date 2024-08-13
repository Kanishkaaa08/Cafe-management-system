import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()

# Insert sample menu items
cursor.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", ('Coffee', 2.99))
cursor.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", ('Tea', 1.99))
cursor.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", ('Sandwich', 4.99))
cursor.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", ('Cake', 3.49))
cursor.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", ('Juice', 2.49))

# Commit the changes and close the connection
conn.commit()
conn.close()
