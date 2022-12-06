def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    inputs = []
    for line in lines:
        a, b = line.strip().split(' -> ')
        a, b = list(map(int, a.split(','))), list(map(int, b.split(',')))
        inputs.append([a,b])
    return inputs


def hydrothermal_venture_part_1(size):
    grid = []
    for i in range(size):
        grid.append([0 for j in range(size)])

    inputs = get_usable_input()

    for start, end in inputs:
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]), max(start[1], end[1])+1):
                grid[i][start[0]] += 1
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
                grid[start[1]][i] += 1

    count = 0

    for i in range(size):
        for j in range(size):
            if grid[i][j] >=2:
                count += 1
    print(count)


def hydrothermal_venture_part_2(size):
    grid = []
    for i in range(size):
        grid.append([0 for j in range(size)])

    inputs = get_usable_input()

    for start, end in inputs:
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]), max(start[1], end[1])+1):
                grid[i][start[0]] += 1
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
                grid[start[1]][i] += 1
        else:
            if start[0] < end[0] and start[1] < end[1]:
                i, j = start[0], start[1]
                while i <= end[0] and j <= end[1]:
                    grid[j][i] += 1
                    i += 1
                    j += 1
            elif start[0] < end[0] and start[1] > end[1]:
                i, j = start[0], start[1]
                while i <= end[0] and j >= end[1]:
                    grid[j][i] += 1
                    i += 1
                    j -= 1
            elif start[0] > end[0] and start[1] < end[1]:
                i, j = start[0], start[1]
                while i >= end[0] and j <= end[1]:
                    grid[j][i] += 1
                    i -= 1
                    j += 1
            elif start[0] > end[0] and start[1] > end[1]:
                i, j = start[0], start[1]
                while i >= end[0] and j >= end[1]:
                    grid[j][i] += 1
                    i -= 1
                    j -= 1
    count = 0

    for i in range(size):
        for j in range(size):
            if grid[i][j] >= 2:
                count += 1
    print(count)


hydrothermal_venture_part_1(1000)
hydrothermal_venture_part_2(1000)
