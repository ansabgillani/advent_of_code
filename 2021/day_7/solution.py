
from math import factorial

def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(int, lines[0].strip().split(',')))


def treachery_of_whales_part_1():
    inputs = get_usable_input()
    minimum, maximum = min(inputs), max(inputs)
    min_dist = 999999999999
    for i in range(minimum, maximum + 1):
        dist = 0
        for j in range(len(inputs)):
            dist += abs(inputs[j] - i)
        min_dist = min(dist, min_dist)

    print(min_dist)


def treachery_of_whales_part_2():
    inputs = get_usable_input()
    minimum, maximum = min(inputs), max(inputs)
    min_dist = 999999999999
    for i in range(minimum, maximum + 1):
        dist = 0
        for j in range(len(inputs)):
            for x in range(abs(inputs[j] - i)+1):
                dist += x
        min_dist = min(dist, min_dist)

    print(min_dist)


treachery_of_whales_part_2()
