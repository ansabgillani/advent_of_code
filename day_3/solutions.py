def rucksack_reorganization_part_1():
    with open('input.txt') as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        line = line.strip()
        middle = len(line) // 2
        first_rucksack, second_rucksack = set(line[:middle]), set(line[middle:])
        common = first_rucksack.intersection(second_rucksack).pop()
        if ord('a') <= ord(common) <= ord('z'):
            sum += (ord(common) - ord('a') + 1)
        else:
            sum += (ord(common) - ord('A') + 27)
    print(f"Answer to part 1 is: {sum}")


def rucksack_reorganization_part_2():
    with open('input.txt') as f:
        lines = f.readlines()

    sum = 0
    member = 0
    groups = []
    group = []
    for line in lines:
        line = line.strip()
        group.append(set(line))
        member += 1
        if member == 3:
            groups.append(group)
            member = 0
            group = []
    for group in groups:
        common = group[0].intersection(group[1]).intersection(group[2]).pop()
        if ord('a') <= ord(common) <= ord('z'):
            sum += (ord(common) - ord('a') + 1)
        else:
            sum += (ord(common) - ord('A') + 27)
    print(f"Answer to part 2 is: {sum}")


rucksack_reorganization_part_1()
rucksack_reorganization_part_2()
