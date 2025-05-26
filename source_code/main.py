from address_book import AddressBook
from contact import Contact

if __name__ == "__main__":
    address_book = AddressBook()  # Invoke function AddressBook and assign it as address_book.

    # Adding some random contacts for demonstration
    address_book.contacts.append(Contact("Ralph Andrei", "Castillo", "123 Buklod St.", "099112341234"))
    address_book.contacts.append(Contact("Arthur", "Morgan", "456 Elm St", "8944646"))

    # Use a while loop that is assigned True
    while True:
        print("\n1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. View Contacts\n5. Search Address Book\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            address_book.add_contact()  # Invoke function add_contact
        elif choice == '2':
            address_book.edit_contact()  # Invoke function edit_contact
        elif choice == '3':
            address_book.delete_contact()  # Invoke function delete_contact
        elif choice == '4':
            address_book.view_contacts()  # Invoke function view_contact
        elif choice == '5':
            search = input("Enter name, address, or contact number: ")
            address_book.search_contacts(search)  # Invoke function search_contacts
        elif choice == '6':
            print("Exiting the program.")
            break  # Use break to terminate the program.
        else:  # Invalid user input.
            print("Invalid choice. Please select a valid option.")
