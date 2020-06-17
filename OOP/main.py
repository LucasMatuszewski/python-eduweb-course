# We have main.py in subfolder which is not a standard.
# For autocomplete we have to add extraPaths in .vscode/settings.json
from bill import Bill
import view


def main():
    # now we can use Meal Constructor to create Object of our class:
    # eggs = Meal("Eggs", 6.99)
    # print(eggs.name)

    # Create new instance/object of our class Bill:
    # bill = Bill()
    # bill.add_meal("Eggs", 6.99)
    # bill.add_meal("Coffee", 3.99)

    # print(bill.calculate())
    # print(bill.add_discount(10))  # price with 10% discount
    bill = Bill()
    action = "Start"

    while action != "End":
        action = input(
            "What do you want to do? [Add , Sum, Discount, Check, Save, End]")

        if action == "Add":
            # ask_for_meal returns 2 variables and we can save them like this:
            name, price = view.ask_for_meal()
            bill.add_meal(name, price)
        elif action == "Service":
            name, price, guests_number = view.ask_for_service()
            bill.add_service(name, price, guests_number)
        elif action == "Sum":
            print(bill.calculate())
        elif action == "Discount":
            discount = view.ask_for_discount()
            print(bill.add_discount(discount))
        elif action == "Check":
            # When we call Static Method we use Class itself (Bill), not an object (bill)
            print(Bill.check_discount(100, 10))
        elif action == "Save":
            filename = view.ask_for_filename()
            bill.print_to_file_short(filename)


if __name__ == '__main__':
    main()
