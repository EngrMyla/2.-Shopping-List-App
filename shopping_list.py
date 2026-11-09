shopping_list = []

# Main Menu Function
def menu():
    while True:
        print("\nShopping List Application Menu:")
        print("1. Add item and quantity")
        print("2. View list")
        print("3. Update item and quantity")
        print("4. Remove item from list")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_item_qty()
        elif choice == '2':
            view_list()
        elif choice == '3':
            update_item_qty()   
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting...\n")
            exit()
        else:
            print("Invalid choice. Please try again.\n")

menu()