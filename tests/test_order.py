import pytest
from models.customer import Customer
from models.coffee import Coffee
from models.order import Order

def setup_module(module):
    # Clear all orders before each test run to avoid interference
    Order.all_orders.clear()

def test_order_initialization():
    customer = Customer(1, "Alice", "alice@example.com")
    coffee = Coffee("Espresso", 3.5)
    order = Order(customer, coffee, 3.5)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5
    assert order in Order.all_orders

def test_order_price_validation():
    customer = Customer(1, "Bob", "bob@example.com")
    coffee = Coffee("Latte", 4.0)
    
    # Assuming Order price must be positive
    with pytest.raises(ValueError):
        Order(customer, coffee, -1)
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 0)

def test_order_associations():
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")
    coffee1 = Coffee("Mocha", 5.0)
    coffee2 = Coffee("Cappuccino", 4.5)
    
    order1 = Order(customer1, coffee1, 5.0)
    order2 = Order(customer2, coffee2, 4.5)
    
    # Check orders belong to correct customer and coffee
    assert order1.customer == customer1
    assert order1.coffee == coffee1
    assert order2.customer == customer2
    assert order2.coffee == coffee2

def test_order_all_orders_list():
    Order.all_orders.clear()
    c1 = Customer(1, "Alice", "alice@example.com")
    cf1 = Coffee("Espresso", 3.5)
    order1 = Order(c1, cf1, 3.5)
    
    assert len(Order.all_orders) == 1
    
    c2 = Customer(2, "Bob", "bob@example.com")
    cf2 = Coffee("Latte", 4.0)
    order2 = Order(c2, cf2, 4.0)
    
    assert len(Order.all_orders) == 2
    assert order1 in Order.all_orders
    assert order2 in Order.all_orders
