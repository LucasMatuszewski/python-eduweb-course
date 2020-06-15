from meal import Meal


class Bill:
    def __init__(self):
        self.meals = []
        super().__init__()

    # Our own methods for a class
    def add_discount(self, discount):
        # pass  # with "pass" keyword we could add blank function for future
        normal_total = self.calculate()
        return normal_total - normal_total * discount/100

    # Static Method is accessible directly from a Class, not only from an object of a class.
    # Because of this we don't use "self" keyword, which coresponds to an Object.
    @staticmethod
    def check_discount(overall_sum, discount):
        return overall_sum - overall_sum * discount/100

    def calculate(self):
        cost = 0.0
        for meal in self.meals:
            cost += meal.price
        return cost

    def print_to_file(self, filename):
        # option "w+" is for writing and reading + creating new file if not exist
        file = open(filename, "w+")
        # file.write("Hello World") # write anything to a file
        for meal in self.meals:
            # format() methods puts variables in curly brackets {} in the same order
            # it's the same like: f"Product name: {meal.name}"
            file.write("Product name: {}, Price: {} \n".format(
                meal.name, meal.price))
        file.close()  # we should always close a file

    def print_to_file_short(self, filename):
        # Shorter syntax without manual closing a file:
        with open(filename, "w+") as file:
            for meal in self.meals:
                file.write(
                    f"Product name: {meal.name}, Price: {meal.price} \n")

    def add_meal(self, name, price):
        # We can use class to create new object of this class:
        meal = Meal(name, price)
        self.meals.append(meal)
