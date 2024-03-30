from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for the application
app.secret_key = "supersecretkey"

# Connect to the SQLite database
def get_db():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn

# Decorator for handling HTTP requests
@app.route("/")
def home():
    # Get the database connection
    db = get_db()

    # Query the dishes table
    dishes = db.execute("SELECT * FROM dishes").fetchall()

    # Render the index.html template with the dishes data
    return render_template("index.html", dishes=dishes)

# Decorator for handling HTTP requests
@app.route("/menu")
def menu():
    # Get the database connection
    db = get_db()

    # Query the dishes table
    dishes = db.execute("SELECT * FROM dishes").fetchall()

    # Render the menu.html template with the dishes data
    return render_template("menu.html", dishes=dishes)

# Decorator for handling HTTP requests
@app.route("/reservation", methods=("GET", "POST"))
def reservation():
    if request.method == "POST":
        # Get the reservation data from the form
        name = request.form["name"]
        phone = request.form["phone"]
        date = request.form["date"]
        time = request.form["time"]
        people = request.form["people"]

        # Insert the reservation data into the reservations table
        db = get_db()
        db.execute(
            "INSERT INTO reservations (name, phone, date, time, people) VALUES (?, ?, ?, ?, ?)",
            (name, phone, date, time, people),
        )
        db.commit()

        # Redirect to the reservation success page
        return redirect(url_for("reservation_success"))

    # Render the reservation.html template
    return render_template("reservation.html")

# Decorator for handling HTTP requests
@app.route("/reservation-success")
def reservation_success():
    # Render the reservation_success.html template
    return render_template("reservation_success.html")

# Decorator for handling HTTP requests
@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        # Get the order data from the form
        name = request.form["name"]
        phone = request.form["phone"]
        dish = request.form["dish"]
        quantity = request.form["quantity"]

        # Insert the order data into the orders table
        db = get_db()
        db.execute(
            "INSERT INTO orders (name, phone, dish, quantity) VALUES (?, ?, ?, ?)",
            (name, phone, dish, quantity),
        )
        db.commit()

        # Redirect to the order success page
        return redirect(url_for("order_success"))

    # Render the order.html template
    return render_template("order.html", dishes=dishes)

# Decorator for handling HTTP requests
@app.route("/order-success")
def order_success():
    # Render the order_success.html template
    return render_template("order_success.html")

# Decorator for handling HTTP requests
@app.route("/specials")
def specials():
    # Get the database connection
    db = get_db()

    # Query the dishes table for the specials
    specials = db.execute(
        "SELECT * FROM dishes WHERE is_special = 1"