from models.customer import Customer
from models.coffee import Coffee

def main():
    # Create some customers
    alice = Customer(1, "Dominic", "dominickipkorir@gmail.com")
    bob = Customer(2, "Bob", "bob@example.com")
    carol = Customer(3, "Carol", "carol@example.com")

    # Create some coffee types
    espresso = Coffee("Espresso", 3.0)
    latte = Coffee("Latte", 4.0)
    mocha = Coffee("Mocha", 4.5)

    # Customers place orders
    alice.create_order(espresso, 3.0)
    alice.create_order(latte, 4.0)
    bob.create_order(latte, 4.5)
    bob.create_order(latte, 4.0)
    carol.create_order(mocha, 4.5)
    carol.create_order(espresso, 3.0)

    # Show coffee order summaries
    for coffee in Coffee.all_coffees:
        print(f"{coffee.name}:")
        print(f"  Number of orders: {coffee.num_orders()}")
        print(f"  Average price: ${coffee.average_price():.2f}")
        print(f"  Customers: {[c.name for c in coffee.customers()]}")
        print()

    # Show most aficionado for Latte
    most = Customer.most_aficionado(latte)
    if most:
        print(f"Most aficionado for {latte.name}: {most.name}")
    else:
        print(f"No orders for {latte.name}")

if __name__ == "__main__":
    main()
