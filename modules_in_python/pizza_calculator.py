import math  # import a mathematical module from python (preinstalled)
# we can also import only what we need:
from math import pi, pow


def calculate_pizza_cm(price, dimension):
    radius = dimension / 2
    return price / (math.pi * math.pow(radius, 2))  # pow = power


def calculate_pizza_cm2(price, dimension):
    radius = dimension / 2
    return price / (pi * (radius ** 2))  # the same result


# we can use this functions directly or import them in other file (main.py)
print(calculate_pizza_cm(10, 23))
print(calculate_pizza_cm2(10, 23))
