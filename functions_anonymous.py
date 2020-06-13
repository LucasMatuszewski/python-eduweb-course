# lambda is a small anonymous function. But is not recommended to use.
# lambda could tak many arguments but only one expresion:
# lambda arguments : expression

# anonymous functions has to be assigned to a variable:
add_numbers = lambda x, y: x+y
print(add_numbers(10, 5))

# or... we can use it immediately:
net_prices = [100, 52, 84]
print(list(map(lambda x: x * 1.23, net_prices)))
# map returns object, we have to change it to a list to print numbers

# list = array in JS [1, 2, 5]
# dictionary = object in JS with {key: value} pairs
