# This is our UI for CLI app: I/O = Input/Output

def ask_for_meal():
    name = input("Provide meal name: ")
    price = input("Provide meal price: ")
    # In Python we can return multiple values, which is unique for Python.
    # In most other languages we would have to return an list or dictionary / object
    return name, float(price)


def ask_for_service():
    name = input("Provide meal name: ")
    price = input("Provide meal price: ")
    guests_number = input("Provide number of guests: ")
    return name, float(price), guests_number


def ask_for_discount():
    discount = input("Provide discount level (%): ")
    return float(discount)


def ask_for_filename():
    filename = input("Provide filename: ")
    return filename
