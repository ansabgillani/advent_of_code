def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        line = list(line.strip())
        grid.append(list(map(int, line)))
    return grid


def treetop_part_1():
    grid = get_usable_input()
    count = 0

    def is_visible(k, l):
        left, right = l - 1, l + 1
        top, bottom = k - 1, k + 1

        while left >= 0 and grid[k][left] < grid[k][l]:
            left -= 1

        while right < len(grid[0]) and grid[k][right] < grid[k][l]:
            right += 1

        while top >= 0 and grid[top][l] < grid[k][l]:
            top -= 1

        while bottom < len(grid) and grid[bottom][l] < grid[k][l]:
            bottom += 1

        return left < 0 or right == len(grid[0]) or top < 0 or bottom == len(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_visible(i, j):
                count += 1
    print(count)



def treetop_part_2():
    grid = get_usable_input()
    count = -1

    def count_visibility(k, l):

        if l == 0 or l == len(grid[0]) - 1 or k == 0 or k == len(grid) - 1:
            return 0

        left, right = l - 1, l + 1
        top, bottom = k - 1, k + 1
        a, b, c, d = 0, 0, 0, 0

        while left >= 0:
            a += 1
            if grid[k][left] >= grid[k][l]:
                break
            left -= 1

        while right < len(grid[0]):
            b += 1
            if grid[k][right] >= grid[k][l]:
                break
            right += 1

        while top >= 0:
            c += 1
            if grid[top][l] >= grid[k][l]:
                break
            top -= 1

        while bottom < len(grid):
            d += 1
            if grid[bottom][l] >= grid[k][l]:
                break
            bottom += 1

        return a * b * c * d

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count = max(count, count_visibility(i, j))
    print(count)


treetop_part_1()
treetop_part_2()
