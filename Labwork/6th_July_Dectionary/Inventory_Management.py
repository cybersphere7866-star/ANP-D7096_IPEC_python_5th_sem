# Inventory Management using a dictionary

inventory = {
    'Laptop': 15,
    'Mouse': 40,
    'Keyboard': 25,
    'Monitor': 10
}

while True:
    print("\nInventory Management")
    print("1. Add a new product")
    print("2. Update stock of an existing product")
    print("3. Remove a product")
    print("4. Display products with stock less than 20")
    print("5. Display total items in inventory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        product = input("Enter product name: ")
        stock = int(input("Enter stock quantity: "))
        inventory[product] = stock
        print("Product added successfully.")

    elif choice == '2':
        product = input("Enter product name to update: ")
        if product in inventory:
            stock = int(input("Enter new stock quantity: "))
            inventory[product] = stock
            print("Stock updated successfully.")
        else:
            print("Product not found.")

    elif choice == '3':
        product = input("Enter product name to remove: ")
        if product in inventory:
            del inventory[product]
            print("Product removed successfully.")
        else:
            print("Product not found.")

    elif choice == '4':
        print("Products with stock less than 20:")
        found = False
        for product, stock in inventory.items():
            if stock < 20:
                print(product, "->", stock)
                found = True
        if not found:
            print("No products found with stock less than 20.")

    elif choice == '5':
        total_items = sum(inventory.values())
        print("Total number of items in inventory:", total_items)

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")

