# List in outer scope:
ski_jumpers = [{"Małysz": "PL"},
               {"Stoch": "PL"},
               {"Kraft": "AU"},
               {"ktos": "?"}]

# We define functions with def word:


def print_all(ski_jumpers):
    for jumper in ski_jumpers:
        print(jumper)
    # we change list in inner function scope by adding new jumper:
    ski_jumpers.append({"Timi Zajc": "SVN"})


# List all jumpers:
print_all(ski_jumpers)
print(ski_jumpers)  # our list from outer scope has changed !

# function variables in Python are referrals to original variable (not a copies)
# function argument "ski_jumpers" shadows original "ski_jumpers" from outer scope
