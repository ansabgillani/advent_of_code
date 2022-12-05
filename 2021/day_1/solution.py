def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()

    inputs = []
    for line in lines:
        inputs.append(int(line.strip()))
    return inputs


def sonar_sweep_part_1():
    inputs = get_usable_input()
    starting = inputs[0]
    count = 0
    for i in range(1, len(inputs)):
        if inputs[i] > starting:
            count += 1
        starting = inputs[i]
    print(f"Answer to the first part: {count}")


def sonar_sweep_part_2():
    inputs = get_usable_input()

    starting = inputs[0] + inputs[1] + inputs[2]
    count = 0

    for i in range(1, len(inputs) - 2):
        sum = inputs[i] + inputs[i + 1] + inputs[i + 2]
        if sum > starting:
            count += 1
        starting = sum
    print(f"Answer to the second part: {count}")


sonar_sweep_part_1()
sonar_sweep_part_2()
