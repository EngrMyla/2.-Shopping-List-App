shopping_list = {}

# Helper Functions
## Empty List Check Function
def check_empty_list():
    if not shopping_list:
        print("\nThe shopping list is empty.")
        return True
    return False

## Get Item by Choice Function
def get_item_by_choice(prompt):
    choice = int(input(prompt))
    shopping_items = list(shopping_list.items())
    if choice <= 0 or choice > len(shopping_items):
        print("Invalid item number.")
        return None
    return shopping_items[choice - 1]

## Get Valid Quantity Function
def get_valid_quantity(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity <= 0:
                print("Please enter a valid positive quantity.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid integer for the quantity.")



# 1. Add Item and Quantity Function
def add_item_qty():
    check_empty_list()
    while True:
        shopping_item = input("Enter the item name: ").strip().upper()
        if shopping_item:
            break
        print("Invalid item name. Please enter a name.")
    
    quantity = get_valid_quantity("Enter the new quantity: ")
    shopping_list[shopping_item] = quantity
    print(f"\nAdded {shopping_item} with quantity {quantity} to the shopping list.")

# 2. View List Function
def view_list():
    check_empty_list()
    print("\nShopping List:")
    for index, (shopping_item, quantity) in enumerate(shopping_list.items(), start=1):
            print(f"{index}. {shopping_item}: {quantity}")

# 3. Sort Items by Quantity Function
def sort_items_by_qty():
    if check_empty_list():
        return
    else:
        sorted_items = sorted(shopping_list.items(), key=lambda x: x[1]) #, reverse=True
        print("\nShopping List Sorted by Quantity:")
        for shopping_item, quantity in sorted_items:
            print(f"{shopping_item}: {quantity}")

# 4. Update Item and Quantity Function
def update_item_qty():
    if check_empty_list():
        return
    view_list()

    selected_item = get_item_by_choice("\nEnter the item number to update: ")
    if selected_item is None:
        return

    shopping_item, _ = selected_item
    new_quantity = get_valid_quantity("Enter the new quantity: ")
    
    shopping_list[shopping_item] = new_quantity
    print(f"\nUpdated {shopping_item} with new quantity {new_quantity}.")

# 5. Remove Item from List Function
def remove_item():
    view_list()

    selected_item = get_item_by_choice("\nEnter the item number to update: ")
    if selected_item is None:
        return

    shopping_item, _ = selected_item
    del shopping_list[shopping_item]
    print(f"\nRemoved {shopping_item} from the shopping list.")


# Main Menu Function
def menu():
    while True:
        print("\nShopping List Application Menu:\n")
        print("1. Add item and quantity")
        print("2. View list")
        print("3. Sort items by quantity")
        print("4. Update item and quantity")
        print("5. Remove item from list")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")
        if choice == '1':
            add_item_qty()
        elif choice == '2':
            view_list()
        elif choice == '3':
            sort_items_by_qty()
        elif choice == '4':
            update_item_qty()   
        elif choice == '5':
            remove_item()
        elif choice == '6':
            print("Exiting... Thank you for using this Shopping List Application!\n")
            return
        else:
            print("Invalid choice. Please try again.\n")

menu()