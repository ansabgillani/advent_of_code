def get_usable_input():
    inputs = []
    for line in open('input.txt').readlines():
        inputs.append(line.strip().split())
    return inputs


class CathodeRay:
    def solve(self):
        inputs = get_usable_input()
        executions = []
        circuit_cycles, X = 1, 1

        for action in inputs:
            circuit_cycles += 1
            executions.append(X)

            if action[0] == 'addx':
                circuit_cycles += 1
                executions.append(X)
                X += int(action[1])

        return executions

    def part_1(self):
        executions = self.solve()
        signal_strength = sum(i * executions[i - 1] for i in [20, 60, 100, 140, 180, 220])
        print(signal_strength)

    def part_2(self):
        executions = self.solve()
        for i in range(6):
            for j in range(40):
                print("#" if abs(j - executions[i * 40 + j]) < 2 else ".", end="")
            print()


CathodeRay().part_1()
CathodeRay().part_2()
