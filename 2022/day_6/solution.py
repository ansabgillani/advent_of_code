from collections import deque


def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    inputs = []
    for line in lines:
        inputs.append(line.strip())
    return inputs


def tuning_trouble_part_1():
    strings = get_usable_input()

    def solution(string):
        window = deque()
        for i, character in enumerate(string):
            while character in window:
                window.popleft()
            window.append(character)
            if len(window) == 4:
                return i + 1
        return -1

    for string in strings:
        print(solution(string))


def tuning_trouble_part_2():
    strings = get_usable_input()

    def solution(string):
        window = deque()
        for i, character in enumerate(string):
            while character in window:
                window.popleft()
            window.append(character)
            if len(window) == 14:
                return i + 1
        return -1

    for string in strings:
        print(solution(string))


tuning_trouble_part_2()
