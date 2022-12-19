from collections import deque


def get_usable_input():
    lines = open('input.txt').readlines()
    inputs = []
    for line in lines:
        line = line.strip().split()
        id = int(line[1][:-1])
        ore_cost = int(line[6])
        clay_cost = int(line[12])
        obsidian_cost = [int(line[18]), int(line[21])]
        geode_cost = [int(line[27]), int(line[30])]
        line = {
            'id': id,
            'ore_cost': ore_cost,
            'clay_cost': clay_cost,
            'obsidian_cost': obsidian_cost,
            'geode_cost': geode_cost
        }
        inputs.append(line)
    return inputs


def solve(blueprint, time):
    ore_cost = blueprint['ore_cost']
    clay_cost = blueprint['clay_cost']
    obsidian_cost = blueprint['obsidian_cost']
    geode_cost = blueprint['geode_cost']

    best = 0

    initial_state = (0, 0, 0, 0, 1, 0, 0, 0, time)
    queue = deque([initial_state])
    visited = set()

    while queue:
        state = queue.popleft()
        ores, clays, obsidians, geodes, current_ore, current_clay, current_obsidian, current_geode, current_time = state

        best = max(best, geodes)
        if current_time == 0:
            continue

        max_cost = max([ore_cost, clay_cost, obsidian_cost[0], geode_cost[0]])
        if current_ore >= max_cost:
            current_ore = max_cost

        if current_clay >= obsidian_cost[1]:
            current_clay = obsidian_cost[1]

        if current_obsidian >= geode_cost[1]:
            current_obsidian = geode_cost[1]

        if ores >= current_time * max_cost - current_ore * (current_time - 1):
            ores = current_time * max_cost - current_ore * (current_time - 1)

        if clays >= current_time * obsidian_cost[1] - current_clay * (current_time - 1):
            clays = current_time * obsidian_cost[1] - current_clay * (current_time - 1)

        if obsidians >= current_time * geode_cost[1] - current_obsidian * (current_time - 1):
            obsidians = current_time * geode_cost[1] - current_obsidian * (current_time - 1)

        state = (
            ores, clays, obsidians, geodes,
            current_ore, current_clay, current_obsidian, current_geode,
            current_time
        )

        if state in visited:
            continue
        visited.add(state)

        queue.append(
            (
                ores + current_ore, clays + current_clay, obsidians + current_obsidian, geodes + current_geode,
                current_ore, current_clay, current_obsidian, current_geode,
                current_time - 1
            )
        )
        if ores >= ore_cost:
            queue.append(
                (
                    ores - ore_cost + current_ore, clays + current_clay,
                    obsidians + current_obsidian, geodes + current_geode,
                    current_ore + 1, current_clay, current_obsidian, current_geode,
                    current_time - 1
                )
            )
        if ores >= clay_cost:
            queue.append(
                (
                    ores - clay_cost + current_ore, clays + current_clay,
                    obsidians + current_obsidian, geodes + current_geode,
                    current_ore, current_clay + 1, current_obsidian, current_geode, current_time - 1
                )
            )
        if ores >= obsidian_cost[0] and clays >= obsidian_cost[1]:
            queue.append(
                (
                    ores - obsidian_cost[0] + current_ore, clays - obsidian_cost[1] + current_clay,
                    obsidians + current_obsidian, geodes + current_geode,
                    current_ore, current_clay, current_obsidian + 1, current_geode,
                    current_time - 1
                )
            )
        if ores >= geode_cost[0] and obsidians >= geode_cost[1]:
            queue.append(
                (
                    ores - geode_cost[0] + current_ore, clays + current_clay,
                    obsidians - geode_cost[1] + current_obsidian, geodes + current_geode,
                    current_ore, current_clay, current_obsidian, current_geode + 1,
                    current_time - 1
                )
            )
    return best


def part_1():
    answer = 0
    blueprints = get_usable_input()
    for blueprint in blueprints:
        sol = solve(blueprint, 24)
        answer += blueprint['id'] * sol
    print(answer)


def part_2():
    answer = 1
    blueprints = get_usable_input()
    for i in range(len(blueprints)):
        if i < 3:
            sol = solve(blueprints[i], 32)
            answer *= sol
    print(answer)


part_1()
part_2()
