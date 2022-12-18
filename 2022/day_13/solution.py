from functools import cmp_to_key

# Read input
def get_usable_input():
    return [eval(line) for line in open("input.txt") if line.strip()]


class DistressSignal:

    def comp(self, a, b):
        def dfs(a, b):
            if type(a) == type(b) == int:
                return a - b
            if type(a) == int:
                return dfs([a], b)
            if type(b) == int:
                return dfs(a, [b])
            if len(a) > 0 and len(b) > 0:
                return dfs(a[0], b[0]) if dfs(a[0], b[0]) else dfs(a[1:], b[1:])
            return len(a) - len(b)
        return dfs(a, b)

    def part_1(self):
        PS = get_usable_input()
        p1 = sum(i + 1 for i, (a, b) in enumerate(zip(PS[::2], PS[1::2])) if self.comp(a, b) < 0)
        print(p1)

    def part_2(self):
        PS = get_usable_input()
        PS = sorted(PS + [[[2]], [[6]]], key=cmp_to_key(self.comp))
        p2 = (PS.index([[2]]) + 1) * (PS.index([[6]]) + 1)
        print(p2)


DistressSignal().part_1()
DistressSignal().part_2()
