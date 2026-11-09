shopping_list = {}

# Main Menu Function
def menu():
    while True:
        print("\nShopping List Application Menu:")
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
            print("Exiting...\n")
            return
        else:
            print("Invalid choice. Please try again.\n")

menu()