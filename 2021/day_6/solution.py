def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(int, lines[0].strip().split(',')))


def lanternfish(days):
    inputs = get_usable_input()

    hashmap = {i: 0 for i in range(9)}

    for input in inputs:
        hashmap[input] += 1

    for i in range(days):
        dying_fishes = hashmap[0]
        for j in range(1, 9):
            hashmap[j - 1] = hashmap[j]
        hashmap[6] += dying_fishes
        hashmap[8] = dying_fishes

    count = 0
    for i in range(9):
        count += hashmap[i]

    print(count)


def part_1():
    lanternfish(days=80)


def part_2():
    lanternfish(days=256)


part_1()
part_2()
