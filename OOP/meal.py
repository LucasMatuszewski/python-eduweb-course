# CLASSES and Object Oriented Programming in Python

class Meal:
    # Class Constructor with __init__ and "self" keyword + our own parameters:
    def __init__(self, name, price):
        # self is little like "this" in JS. Below we add parameters to a class constructor:
        self.name = name
        self.price = price
        super().__init__()

# Self correspond to Object of a Class created with constructor