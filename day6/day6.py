
with open("input.txt", 'r') as inpt:
    line = inpt.read().split("\n\n")

    count = sum([len(set([c for c in group if not c.isspace()])) for group in line])
    print("Part 1:")
    print(count)


groups = [[set(person) for person in group.splitlines()] for group in line]

intersections = sum(len(set.intersection(*group)) for group in groups)

print("Part 2: ")
print(intersections)

