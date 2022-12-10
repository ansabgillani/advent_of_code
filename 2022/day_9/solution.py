def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    inputs = []
    for line in lines:
        line = list(line.strip().split())
        inputs.append([line[0], int(line[1])])
    return inputs


class RopeBridge:
    DIR = {"L": -1, "R": 1, "U": -1j, "D": 1j}

    def __solution(self, knots):
        tail_position = set()
        inputs = get_usable_input()
        for d, steps in inputs:
            for _ in range(steps):
                knots[0] += self.DIR[d]

                for i, (h, t) in enumerate(zip(knots, knots[1:])):
                    if abs(h.real - t.real) >= 2 or abs(h.imag - t.imag) >= 2:
                        if h.real != t.real:
                            t += (h.real - t.real) / abs(h.real - t.real)
                        if h.imag != t.imag:
                            t += 1j * (h.imag - t.imag) / abs(h.imag - t.imag)
                        knots[i + 1] = t

                tail_position.add(knots[-1])
        print(len(tail_position))

    def rope_bridge_part_1(self):
        knots = [0] * 2
        self.__solution(knots)

    def rope_bridge_part_2(self):
        knots = [0] * 10
        self.__solution(knots)


RopeBridge().rope_bridge_part_1()
RopeBridge().rope_bridge_part_2()
