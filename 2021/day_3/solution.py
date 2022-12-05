def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()

    inputs = []
    for line in lines:
        inputs.append(line.strip())
    return inputs


def binary_diagnostics_part_1():
    inputs = get_usable_input()

    bits = [{'0': 0, '1': 0} for i in range(len(inputs[0]))]
    for binary in inputs:
        for i in range(len(binary)):
            bits[i][binary[i]] += 1

    gamma, epsilon = '', ''
    for bit in bits:
        gamma += '1' if bit['1'] >= bit['0'] else '0'
        epsilon += '0' if bit['1'] >= bit['0'] else '1'

    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    power = gamma * epsilon
    print(f"Answer to the first part: {power}")


def binary_diagnostics_part_2():
    inputs = get_usable_input()
    oxygen, carbon = inputs.copy(), inputs.copy()
    for i in range(len(inputs[0])):

        if len(oxygen) > 1:

            bit = {'0': 0, '1': 0}
            for j in range(len(oxygen)):
                bit[oxygen[j][i]] += 1

            significant_bit = '1' if bit['1'] >= bit['0'] else '0'
            oxygen = [num for num in oxygen if num[i] == significant_bit]

        if len(carbon) > 1:

            bit = {'0': 0, '1': 0}
            for j in range(len(carbon)):
                bit[carbon[j][i]] += 1

            least_bit = '0' if bit['1'] >= bit['0'] else '1'
            carbon = [num for num in carbon if num[i] == least_bit]

    oxygen, carbon = int(oxygen.pop(), 2), int(carbon.pop(), 2)
    rating = oxygen * carbon
    print(f"Answer to the second part: {rating}")


binary_diagnostics_part_1()
binary_diagnostics_part_2()
