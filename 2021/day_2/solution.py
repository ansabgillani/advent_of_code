def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()

    inputs = []
    for line in lines:
        line = line.strip().split()
        line[1] = int(line[1])
        inputs.append(line)
    return inputs


def dive_part_1():
    inputs = get_usable_input()
    horizontal, depth = 0, 0
    for direction, value in inputs:
        if direction == 'forward':
            horizontal += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value
    product = horizontal * depth
    print(f"Answer to the first part: {product}")


def dive_part_2():
    inputs = get_usable_input()
    horizontal, depth, aim = 0, 0, 0
    for direction, value in inputs:
        if direction == 'forward':
            horizontal += value
            depth += (aim * value)
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    product = horizontal * depth
    print(f"Answer to the second part: {product}")


dive_part_1()
dive_part_2()
