from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize database
def init_db():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS menu
                      (id INTEGER PRIMARY KEY, item_name TEXT, price REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                      (id INTEGER PRIMARY KEY, item_name TEXT, quantity INTEGER, price REAL)''')
    conn.commit()
    conn.close()

# Route for the home page
@app.route('/')
def menu():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM menu')
    menu_items = cursor.fetchall()
    conn.close()
    return render_template('menu.html', menu_items=menu_items)

# Route to handle placing an order
@app.route('/order', methods=['POST'])
def order():
    item_id = request.form['item_id']
    quantity = int(request.form['quantity'])

    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM menu WHERE id = ?', (item_id,))
    item = cursor.fetchone()

    cursor.execute('INSERT INTO orders (item_name, quantity, price) VALUES (?, ?, ?)',
                   (item[1], quantity, item[2] * quantity))
    conn.commit()
    conn.close()

    return redirect(url_for('bill'))

# Route for displaying the bill
@app.route('/bill')
def bill():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()

    total_amount = sum(order[2] * order[3] for order in orders)

    conn.close()
    return render_template('bill.html', orders=orders, total_amount=total_amount)

# Route to clear the order (simulate payment)
@app.route('/clear')
def clear():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM orders')
    conn.commit()
    conn.close()

    return redirect(url_for('menu'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
