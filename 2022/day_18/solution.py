from collections import deque


def get_usable_input():
    lines = open('input.txt').readlines()
    input = []
    for line in lines:
        line = tuple(map(int, line.strip().split(',')))
        input.append(line)

    return input


P = set(get_usable_input())

def reaches_outside(x, y, z, inner, outer, trapped):
    if (x, y, z) in outer:
        return True
    if (x, y, z) in inner:
        return False

    visited = set()
    queue = deque([(x, y, z)])

    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in P:
            continue
        if (x, y, z) in visited:
            continue

        visited.add((x, y, z))

        if len(visited) > (5000 if trapped else 0):
            for p in visited:
                outer.add(p)
            return True

        for _ in [-1, 1]:
            queue.append((x + 1, y, z))
            queue.append((x - 1, y, z))
            queue.append((x, y + 1, z))
            queue.append((x, y - 1, z))
            queue.append((x, y, z + 1))
            queue.append((x, y, z - 1))

    for p in visited:
        inner.add(p)

    return False


def solve(trapped):
    inner, outer = set(), set()
    ans = 0
    for (x, y, z) in P:
        movements = (
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        )
        for movement in movements:
            if reaches_outside(movement[0], movement[1], movement[2], inner, outer, trapped):
                ans += 1
    return ans


print(solve(False))
print(solve(True))
