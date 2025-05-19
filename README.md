# ☕ Coffee Shop Domain Model

This project models a simple coffee shop system using Object-Oriented Programming (OOP) in Python. It includes three main classes: `Customer`, `Coffee`, and `Order`, along with relationships and logic for managing coffee orders, customer behavior, and basic analytics like most loyal customers and average coffee price.

---

## 📁 Project Structure

coffee_shop/
├── models/
│ ├── customer.py
│ ├── coffee.py
│ └── order.py
├── tests/
│ ├── test_customer.py
│ ├── test_coffee.py
│ └── test_order.py
├── app.py
├── debug.py
├── README.md
└── requirements.txt


---

## 📦 Requirements

- Python 3.10+
- `pytest` for testing

Install dependencies:

```bash
pip install -r requirements.txt

## Running Tests
We use pytest for unit testing. Run the test suite with:
pytest

## Features Implemented
✅ Models
Customer

create_order(coffee, price)

get_orders()

most_aficionado(coffee) (class method)

Coffee

orders()

customers()

num_orders()

average_price()

Order

Stores customer, coffee, and validated price

Ensures price is a float between 1.0 and 10.0

✅ Validations
Coffee names must be strings with at least 3 characters.

Prices must be numbers greater than 0.

Orders must use prices between 1.0 and 10.0 (float).

## Author
Dominic Kipkorir
Moringa School – Software Engineering Track
2025

