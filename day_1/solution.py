

def count_max_calories_part_1():
    with open('input.txt') as f:
        lines = f.readlines()

    weights_carried = []
    weight_sum = 0
    for line in lines:
        if line.strip() != '':
            weight_sum += int(line.strip())
        else:
            weights_carried.append(weight_sum)
            weight_sum = 0

    print(f"Answer to the first part: {max(weights_carried)}")



def count_max_calories_part_2():
    with open('input.txt') as f:
        lines = f.readlines()

    weights_carried = []
    weight_sum = 0
    for line in lines:
        if line.strip() != '':
            weight_sum += int(line.strip())
        else:
            weights_carried.append(weight_sum)
            weight_sum = 0
    if weight_sum:
        weights_carried.append(weight_sum)
    weights_carried.sort()
    print(f"Answer to the second part: {weights_carried[-1] + weights_carried[-2] + weights_carried[-3]}")


count_max_calories_part_1()
count_max_calories_part_2()
