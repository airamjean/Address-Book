# Define a class that is a blueprint for creating the 'Address Book'.
class AddressBook:
    # Define the function for class and assign a parameter (self).
    def __init__(self):
        self.contacts = []

    # The contact class is for the inputs, and the address book class is the one that updates when a contact is added.
    # Define the function 'add_contact' and assign a parameter (self)
    def add_contact(self):
        # Use the len() function to return the list of an object.
        if len(self.contacts) < 100:  # Use if function to allow the user to add_contact up to 100.
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input("Enter address: ")
            contact_number = input("Enter contact number: ")
            new_contact = Contact(first_name, last_name, address, contact_number)
            # Use the append() function to add new_contact to the end of the existing list.
            self.contacts.append(new_contact)
            print(f"Contact added successfully.")
        else:
            print("Address book is full.")  # Otherwise, it has reached the maximum capacity.

    # Define the function 'edit_contact' and assign a parameter (self).
    def edit_contact(self):
        entry_number = int(input("Enter the entry number you want to edit: ")) - 1
        # Use if function to check whether the value of entry_number is less than the length of self.contacts.
        if 0 <= entry_number < len(self.contacts):
            contact = self.contacts[entry_number]
            print(f"Editing contact: {contact}")
            contact.first_name = input("Enter new first name: ")
            contact.last_name = input("Enter new last name: ")
            contact.address = input("Enter new address: ")
            contact.contact_number = input("Enter new contact number: ")
            print("Contact updated successfully.")
        else:  # Otherwise, the entry_number is invalid.
            print("Invalid entry number. Contact not found.")

    # Define the function 'delete_contact' and assign a parameter (self).
    def delete_contact(self):
        entry_number = int(input("Enter the entry number you want to delete: ")) - 1
        # Use if function to check whether the value of entry_number is less than the length of self.contacts.
        if 0 <= entry_number < len(self.contacts):
            deleted_contact = self.contacts.pop(entry_number)
            print(f"Deleted contact: {deleted_contact}")
        else:  # Otherwise, the entry_number is invalid.
            print("Invalid entry number. Contact not found.")

    # Define the function 'view_contacts' and assign a parameter (self).
    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")

    # 'i' for index.
    # Use enumerate() function to return both the index (i) and the corresponding value (contact) from the list.
    # The start=1 argument specifies that the index should start from 1 (instead of the default 0).

    # Define the function 'search_contacts' and assign parameters.
    def search_contacts(self, query):
        results = []  # Assign empty list for variable 'results'.
        for contact in self.contacts:
            # Use if function and assign a boolean condition that will search for the query.
            if query in contact.first_name.capitalize() or query in contact.last_name.capitalize() or query in contact.address.capitalize() or query in contact.contact_number:
                results.append(contact)
        # Use len() function to identify the length or the number of elements
        if len(results) == 0:  # If results is equal to zero the boolean condition is true.
            print("No matching contacts found.")
        else:  # Otherwise, it is false and a contact was found.
            print("Contacts found:")
            # Display the collected list.
            for i, contact in enumerate(results):
                print(f"{i}: {contact.first_name} {contact.last_name}, {contact.address}, {contact.contact_number}")
