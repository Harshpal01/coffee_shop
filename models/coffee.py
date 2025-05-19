from models.order import Order

class Coffee:
    all_coffees = []

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        Coffee.all_coffees.append(self)

    def __repr__(self):
        return f"<Coffee {self.name} @ ${self.price:.2f}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (float, int)) and value > 0:
            self._price = float(value)
        else:
            raise ValueError("Price must be a number greater than 0")

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
