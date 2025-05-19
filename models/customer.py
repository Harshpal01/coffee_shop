from models.order import Order
from models.coffee import Coffee  # Import for type checking

class Customer:
    all_customers = []

    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders = []
        Customer.all_customers.append(self)

    def add_order(self, order):
        if isinstance(order, Order):
            self.orders.append(order)

    def get_orders(self):
        return self.orders

    def create_order(self, coffee: Coffee, price: float):
        """
        Create a new Order for this customer and the specified coffee at given price.
        """
        order = Order(self, coffee, price)
        self.add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee: Coffee):
        """
        Returns the Customer instance who has spent the most money on the given coffee.
        Returns None if no customers have ordered that coffee.
        """
        spending = {}

        for order in Order.all_orders:
            if order.coffee == coffee:
                cust = order.customer
                spending[cust] = spending.get(cust, 0) + order.price

        if not spending:
            return None

        # Return customer with max total spending
        return max(spending, key=spending.get)

    def __repr__(self):
        return f"<Customer {self.customer_id}: {self.name} ({self.email})>"
