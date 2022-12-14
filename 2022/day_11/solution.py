import math


def get_usable_input():
    return [
        {
            "items": [64, 89, 65, 95],
            "op": lambda n: n * 7,
            "next": lambda n: 1 if n % 3 else 4,
        },
        {
            "items": [76, 66, 74, 87, 70, 56, 51, 66],
            "op": lambda n: n + 5,
            "next": lambda n: 3 if n % 13 else 7,
        },
        {
            "items": [91, 60, 63],
            "op": lambda n: n * n,
            "next": lambda n: 5 if n % 2 else 6,
        },
        {
            "items": [92, 61, 79, 97, 79],
            "op": lambda n: n + 6,
            "next": lambda n: 6 if n % 11 else 2,
        },
        {
            "items": [93, 54],
            "op": lambda n: n * 11,
            "next": lambda n: 7 if n % 5 else 1,
        },
        {
            "items": [60, 79, 92, 69, 88, 82, 70],
            "op": lambda n: n + 8,
            "next": lambda n: 0 if n % 17 else 4,
        },
        {
            "items": [64, 57, 73, 89, 55, 53],
            "op": lambda n: n + 1,
            "next": lambda n: 5 if n % 19 else 0,
        },
        {
            "items": [62],
            "op": lambda n: n + 4,
            "next": lambda n: 2 if n % 7 else 3,
        },
    ]


class MiddleMonkey:

    def simulate(self, rounds, limiting_function):
        monkeys = get_usable_input()

        inspections = [0] * len(monkeys)
        for _ in range(rounds):
            for i, m in enumerate(monkeys):
                for item in m["items"]:
                    inspections[i] += 1
                    new = limiting_function(m["op"](item))
                    monkeys[m["next"](new)]["items"].append(new)
                m["items"] = []
        return inspections

    def part_1(self):
        inspections = self.simulate(20, lambda n: n // 3)
        p1 = math.prod(sorted(inspections)[-2:])
        print(p1)

    def part_2(self):
        inspections = self.simulate(10000, lambda n: n % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19))
        p2 = math.prod(sorted(inspections)[-2:])
        print(p2)


MiddleMonkey().part_1()
MiddleMonkey().part_2()
