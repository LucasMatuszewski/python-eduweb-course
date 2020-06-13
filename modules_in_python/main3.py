# we import directly our function by the name
import pizza_calculator


def main2():
    # define two variables at once. Split provided value by space (default on whitespace):
    price, dimension = input(
        "Provide first pizza price and diameter separated by space:\n").split()
    first_pizza_calculation = pizza_calculator.calculate_pizza_cm(
        float(price), int(dimension))
    price, dimension = input(
        "Provide second pizza price and diameter separated by space:\n").split()
    second_pizza_calculation = pizza_calculator.calculate_pizza_cm(
        float(price), int(dimension))

    if first_pizza_calculation > second_pizza_calculation:
        print("first pizza is cheaper")
    else:
        print("second pizza is cheaper")


# when we import we should not use main function without checking if we are in main file.
# For the file we RUN the name is always "__main__" (even when the file is main3.py)
# but for imported modules the __name__ will be the same as file name.
# So we check if we are in main runned file:
if __name__ == "__main__":
    print(__name__)  # __name__ is a variable with a file name, prints __main__
    main2()
