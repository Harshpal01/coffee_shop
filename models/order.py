class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not hasattr(customer, "orders"):
            raise ValueError("Invalid customer instance")
        if not hasattr(coffee, "orders"):
            raise ValueError("Invalid coffee instance")
        if not isinstance(price, (float, int)) or not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all_orders.append(self)

    def __repr__(self):
        # Safe __repr__ that doesn't fail even if attributes are missing
        cust_name = getattr(self._customer, 'name', 'Unknown Customer')
        coffee_name = getattr(self._coffee, 'name', 'Unknown Coffee')
        price = getattr(self, '_price', 'Unknown Price')
        return f"<Order {cust_name} -> {coffee_name} @ ${price}>"

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
