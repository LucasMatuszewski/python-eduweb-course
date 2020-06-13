ski_jumpers = [{"Małysz": "PL"},
               {"Stoch": "PL"},
               {"Kraft": "AU"},
               {"ktos": "?"}]

for jumper in ski_jumpers:
    print("Skoczek", jumper)

index = 0
while index < len(ski_jumpers):
    print(ski_jumpers[index], ski_jumpers[index + 1])
    index += 2

for jumper in ski_jumpers:
    jumper_list = list(jumper.keys())
    if jumper_list[0] == "Stoch":
        print("Kamil", jumper_list[0])
        break

for jumper in ski_jumpers:
    if list(jumper.values())[0] == "PL":
        print("Polish:", jumper)

polish = [jumper for jumper in ski_jumpers if list(jumper.values())[0] == "PL"]
print("Polish: ", polish)
