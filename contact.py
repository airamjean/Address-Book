# Class function is used to define a class - in this case, a blueprint for creating 'contact'.
class Contact:
    # Define the function for class and assign a parameter.
    def __init__(self, first_name, last_name, address, contact_number):  # Assign values to Object Properties
        # Use 'self' as reference and initiate each Contact variables.
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.contact_number = contact_number

    def __str__(self):  # Use __str__ function to return the class object function represented as a string.

        return f"{self.first_name} {self.last_name}, {self.address}, {self.contact_number}"
    # Numbers can also be interpreted as string, in the case of contact number