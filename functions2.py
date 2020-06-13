# List of dictionaries in outer scope:
ski_jumpers = [{"Małysz": "PL"},
               {"Stoch": "PL"},
               {"Kraft": "AU"},
               {"ktos": "?"}]


def find_jumper(jumper_name="Stoch"):  # function with default argument
    for jumper in ski_jumpers:  # we use variable directly from outer scope
        if list(jumper.keys())[0] == jumper_name:
            print("Jumper found by name:", jumper)
            break


def find_by_nationality(ski_jumpers, nationality):
    for jumper in ski_jumpers:
        if list(jumper.values())[0] == nationality:
            print("Jumper found by nation:", jumper)
            # break


def print_jumper(*ski_jumpers):  # star = multiple arguments
    for jumper in ski_jumpers:
        print("\n****", jumper, "****")


find_jumper()  # call function with default argument

# arguments used by keys in differend order:
find_by_nationality(nationality="PL", ski_jumpers=ski_jumpers)

# we use two arguments for this function with help of star operator
print(print_jumper("Skoczek 1", "Skoczek 2", ski_jumpers))
# in Python functions returns "None" by default (printed on the end)
