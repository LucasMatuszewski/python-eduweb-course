# CLASSES and Object Oriented Programming in Python
from entry_parent import Entry


class Service(Entry):
    # Class Constructor with __init__ and "self" keyword + our own parameters:
    def __init__(self, name, price, guests_number):
        # super() calls parent class and let us inherit attributes from it:
        super().__init__(name, price)
        # self is little like "this" in JS. Below we add parameters to a class constructor:
        self.guests_number = guests_number

# Self correspond to Object of a Class created with constructor
