def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()

    """
            [F] [Q]         [Q]        
    [B]     [Q] [V] [D]     [S]        
    [S] [P] [T] [R] [M]     [D]        
    [J] [V] [W] [M] [F]     [J]     [J]
    [Z] [G] [S] [W] [N] [D] [R]     [T]
    [V] [M] [B] [G] [S] [C] [T] [V] [S]
    [D] [S] [L] [J] [L] [G] [G] [F] [R]
    [G] [Z] [C] [H] [C] [R] [H] [P] [D]
     1   2   3   4   5   6   7   8   9 
    """
    stack_state = [
        'GDVZJSB',
        'ZSMGVP',
        'CLBSWTQF',
        'HJGWMRVQ',
        'CLSNFMD',
        'RGCD',
        'HGTRJDSQ',
        'PFV',
        'DRSTJ',
    ]

    for i in range(len(stack_state)):
        stack_state[i] = list(stack_state[i])

    inputs = []
    for line in lines:
        line = line.strip().split()
        inputs.append({
            'size': int(line[1]),
            'source': int(line[3]) - 1,
            'target': int(line[5]) - 1
        })

    return stack_state, inputs


def supply_stacks_part_1():
    stack_state, inputs = get_usable_input()
    for input in inputs:
        for i in range(input['size']):
            stack_state[input['target']].append(stack_state[input['source']][-1])
            stack_state[input['source']].pop()
    result = ''
    for stack in stack_state:
        result += stack[-1]
    print(f"Answer to the first part: {result}")


def supply_stacks_part_2():
    stack_state, inputs = get_usable_input()
    for input in inputs:
        stack_state[input['target']].extend(
            stack_state[
                input['source']
            ][len(stack_state[input['source']]) - input['size']:]
        )
        stack_state[input['source']] = stack_state[
                                           input['source']
                                       ][: len(stack_state[input['source']]) - input['size']]
    result = ''
    for stack in stack_state:
        result += stack[-1]
    print(f"Answer to the second part: {result}")


supply_stacks_part_1()
supply_stacks_part_2()
