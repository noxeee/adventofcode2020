
with open("example.txt", 'r') as inpt:
    line = inpt.read().split("\n\n")

    count = sum([len(set([c for c in group if not c.isspace()])) for group in line])
    print(count)

    print([group for group in line])

    interesct_count = [len([person for person in group.split('\n')]) for group in line]

    intersect_cnt = 0
    checked_c = []
    for group in line:
        persons = group.split('\n')
        for person in persons:
            for c in person:
                if c.isspace():
                    continue
                if c in checked_c:
                    continue
                checked_c.append(c)
                if person.find(c) != -1:
                    
                if num_c == len(persons):
                    intersect_cnt = intersect_cnt + 1
        checked_c = []

    print(intersect_cnt)
