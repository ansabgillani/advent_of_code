def rock_paper_scissor_part_1():
    with open('input.txt') as f:
        lines = f.readlines()

    choice_points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    winning_combo = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
    draw_combo = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    total_points = 0
    for line in lines:
        choice_1, choice_2 = line.strip().split()
        point = 0
        point += choice_points[choice_2]
        if winning_combo[choice_1] == choice_2:
            point += 6
        elif draw_combo[choice_1] == choice_2:
            point += 3
        else:
            point += 0
        total_points += point
    print(f"Answer to first part: {total_points}")


def rock_paper_scissor_part_2():
    with open('input.txt') as f:
        lines = f.readlines()

    choice_points = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    winning_combo = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }
    lose_combo = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    total_points = 0
    for line in lines:
        choice_1, outcome = line.strip().split()
        points = 0
        if outcome == 'X':
            points += 0
            choice_2 = lose_combo[choice_1]
            points += choice_points[choice_2]
        elif outcome == 'Y':
            points += 3
            points += choice_points[choice_1]
        else:
            points += 6
            choice_2 = winning_combo[choice_1]
            points += choice_points[choice_2]
        total_points += points

    print(f"Answer to second part: {total_points}")


rock_paper_scissor_part_1()
rock_paper_scissor_part_2()
