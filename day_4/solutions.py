
def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    inputs = []
    for line in lines:
        inputs.append([list(map(int, i.split('-'))) for i in line.strip().split(',')])
    return inputs


def camp_cleanup_part_1():
    answer = 0
    inputs = get_usable_input()
    for a, b in inputs:
        if (b[0] <= a[0] and b[1] >= a[1]) or (a[0] <= b[0] and a[1] >= b[1]):
            answer += 1
    print(f"Answer to part 1 is: {answer}")


def camp_cleanup_part_2():
    inputs = get_usable_input()
    answer = 0
    for a, b in inputs:
        if (a[0] <= b[0] <= a[1]) or (b[0] <= a[0] <= b[1]):
            answer += 1
    print(f"Answer to part 2 is: {answer}")


camp_cleanup_part_1()
camp_cleanup_part_2()
