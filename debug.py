from models.customer import Customer
from models.coffee import Coffee

def main():
    # Create some coffee objects
    espresso = Coffee("Espresso", 3.0)
    latte = Coffee("Latte", 4.5)

    # Create some customers
    alice = Customer(1, "Alice", "alice@example.com")
    bob = Customer(2, "Bob", "bob@example.com")

    # Alice orders an espresso
    order1 = alice.create_order(espresso, 3.0)
    # Bob orders two lattes
    order2 = bob.create_order(latte, 4.0)
    order3 = bob.create_order(latte, 4.5)

    # Print all orders for Bob
    print(f"Bob's orders: {bob.get_orders()}")

    # Print total number of orders for Latte
    print(f"Number of Latte orders: {latte.num_orders()}")

    # Print average price for Latte
    print(f"Average Latte price: ${latte.average_price():.2f}")

    # Find who is the most aficionado of Latte
    top_customer = Customer.most_aficionado(latte)
    print(f"Most aficionado of Latte: {top_customer}")

if __name__ == "__main__":
    main()
