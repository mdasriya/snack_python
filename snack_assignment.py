# Initialize snack inventory and sales record as dictionaries
snack_inventory = {}
sales_record = {}

# Function to add a snack to the inventory
def add_snack():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    price = float(input("Enter price: "))
    availability = input("Is the snack available? (yes/no): ").lower()

    snack_inventory[snack_id] = {
        "snack_name": snack_name,
        "price": price,
        "availability": availability == "yes"
    }
    print("Snack added to inventory.")

# Function to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter snack ID to remove: ")
    if snack_id in snack_inventory:
        del snack_inventory[snack_id]
        print("Snack removed from inventory.")
    else:
        print("Snack not found in inventory.")

# Function to update snack availability
def update_availability():
    snack_id = input("Enter snack ID to update availability: ")
    if snack_id in snack_inventory:
        new_availability = input("Is the snack available now? (yes/no): ").lower()
        snack_inventory[snack_id]["availability"] = new_availability == "yes"
        print("Snack availability updated.")
    else:
        print("Snack not found in inventory.")

# Function to record a snack sale
def record_sale():
    snack_id = input("Enter snack ID sold: ")
    if snack_id in snack_inventory:
        if snack_inventory[snack_id]["availability"]:
            sales_record[snack_id] = sales_record.get(snack_id, 0) + 1
            snack_inventory[snack_id]["availability"] = False
            print("Sale recorded.")
        else:
            print("Snack is not available.")
    else:
        print("Snack not found in inventory.")

# Main loop for user interaction
while True:
    print("\n===== Mumbai Munchies Canteen Management =====")
    print("1. Add Snack\n2. Remove Snack\n3. Update Snack Availability")
    print("4. Record Sale\n5. Display Inventory\n6. Display Sales Record")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        record_sale()
    elif choice == "5":
        print("\nSnack Inventory:")
        for snack_id, details in snack_inventory.items():
            print(f"ID: {snack_id}, Name: {details['snack_name']}, Price: {details['price']}, Availability: {'Yes' if details['availability'] else 'No'}")
    elif choice == "6":
        print("\nSales Record:")
        for snack_id, quantity in sales_record.items():
            print(f"ID: {snack_id}, Quantity Sold: {quantity}")
    elif choice == "7":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
