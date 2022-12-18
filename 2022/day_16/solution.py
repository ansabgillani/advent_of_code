from collections import defaultdict
from networkx import *
import functools


@functools.cache
def dfs(pos, visited, minutes, elephant):
    if minutes == 0:
        if elephant:
            return dfs("AA", visited, 26, False)
        return 0

    best = 0
    found = False
    for to, dist in graph[pos]:
        if dist >= minutes or to in visited:
            continue
        found = True
        result = dfs(to, visited | {to}, minutes - dist, elephant) + rates[to] * (
            minutes - dist
        )
        if result > best:
            best = result

    if not found and elephant:
        return dfs("AA", visited, 26, False)

    return best


with open("input.txt") as f:
    G = Graph()
    rates = {"AA": 0}
    for line in f.read().splitlines():
        words = line.split()
        name = words[1]
        rate = int(words[4][5:-1])
        if rate > 0:
            rates[name] = rate
        G.add_node(name)
        for to in "".join(words[9:]).split(","):
            G.add_edge(name, to)

    graph = defaultdict(list)
    for fro in rates:
        for to in rates:
            graph[fro].append((to, shortest_path_length(G, fro, to) + 1))

    print("Part 1:", dfs("AA", frozenset(["AA"]), 30, False))
    print("Part 2:", dfs("AA", frozenset(["AA"]), 26, True))
