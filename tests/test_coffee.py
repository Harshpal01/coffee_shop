import pytest
from models.customer import Customer
from models.coffee import Coffee
from models.order import Order


def setup_module(module):
    # Clean up class-level data before each module run
    Order.all_orders.clear()
    Coffee.all_coffees.clear()


def test_coffee_initialization():
    coffee = Coffee("Espresso", 3.5)
    assert coffee.name == "Espresso"
    assert coffee.price == 3.5


def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("ab", 2.5)  # name too short


def test_coffee_price_validation():
    with pytest.raises(ValueError):
        Coffee("Latte", 0.0)  # price zero not allowed

    with pytest.raises(ValueError):
        Coffee("Latte", -1.0)  # price negative not allowed


def test_orders_and_customers_methods():
    # Setup customers and coffee
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")
    coffee = Coffee("Cappuccino", 4.0)

    # Create orders
    order1 = Order(customer1, coffee, 4.0)
    order2 = Order(customer2, coffee, 3.5)

    # Test orders()
    orders = coffee.orders()
    assert order1 in orders
    assert order2 in orders

    # Test customers()
    customers = coffee.customers()
    assert customer1 in customers
    assert customer2 in customers
    assert len(customers) == 2


def test_num_orders_and_average_price():
    customer1 = Customer(3, "Charlie", "charlie@example.com")
    customer2 = Customer(4, "Dana", "dana@example.com")
    coffee = Coffee("Mocha", 5.0)

    Order.all_orders.clear()  # reset orders

    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 4.0)
    Order(customer1, coffee, 6.0)

    assert coffee.num_orders() == 3
    assert abs(coffee.average_price() - 5.0) < 0.01
