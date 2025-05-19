import pytest
from models.customer import Customer
from models.coffee import Coffee
from models.order import Order

def setup_module(module):
    # Clear global lists before tests
    Customer.all_customers.clear()
    Order.all_orders.clear()
    Coffee.all_coffees.clear()

def test_create_order():
    customer = Customer(1, "Alice", "alice@example.com")
    coffee = Coffee("Espresso", 3.5)

    order = customer.create_order(coffee, 3.5)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5
    assert order in customer.get_orders()

def test_most_aficionado_returns_none_when_no_orders():
    coffee = Coffee("Mocha", 4.0)
    assert Customer.most_aficionado(coffee) is None

def test_most_aficionado_returns_correct_customer():
    # Setup customers and coffee
    coffee = Coffee("Latte", 4.0)
    customer1 = Customer(1, "Bob", "bob@example.com")
    customer2 = Customer(2, "Carol", "carol@example.com")

    # Create orders
    customer1.create_order(coffee, 4.0)
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 10.0)

    # customer1 total = 9.0, customer2 total = 10.0 -> customer2 is most aficionado
    most = Customer.most_aficionado(coffee)
    assert most == customer2

def test_most_aficionado_with_multiple_coffees():
    coffee1 = Coffee("Americano", 3.0)
    coffee2 = Coffee("Flat White", 4.0)
    customer1 = Customer(1, "Dave", "dave@example.com")
    customer2 = Customer(2, "Eve", "eve@example.com")

    customer1.create_order(coffee1, 3.0)
    customer1.create_order(coffee2, 4.0)
    customer2.create_order(coffee1, 6.0)  # customer2 spent more on coffee1
    customer2.create_order(coffee2, 2.0)  # customer2 spent less on coffee2

    # For coffee1, customer2 should be top
    assert Customer.most_aficionado(coffee1) == customer2
    # For coffee2, customer1 should be top
    assert Customer.most_aficionado(coffee2) == customer1
