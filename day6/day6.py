
with open("input.txt", 'r') as inpt:
    line = inpt.read().split("\n\n")

    count = sum([len(set([c for c in group if not c.isspace()])) for group in line])
    print(count)

