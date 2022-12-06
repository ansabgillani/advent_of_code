def get_usable_input():
    with open('input.txt') as f:
        lines = f.readlines()
    draws = list(map(int, lines[0].strip().split(',')))
    boards = []
    board = []
    for line in lines[2:]:
        if line.strip() == '':
            boards.append(board)
            board = []
        else:
            line = list(map(int, line.strip().split()))
            board.append(line)
    if len(board):
        boards.append(board)
    return draws, boards


class GiantSquid:
    def _check_if_won(self, board, row, col):
        row_flag = True
        col_flag = True
        for i in range(5):
            if board[row][i] != -1:
                row_flag = False
            if board[i][col] != -1:
                col_flag = False
        return row_flag or col_flag

    def _get_row_col(self, board, target):
        for i in range(5):
            for j in range(5):
                if board[i][j] == target:
                    return [i, j]
        return [-1, -1]

    def _get_sum(self, board):
        sum = 0
        for i in range(5):
            for j in range(5):
                if board[i][j] != -1:
                    sum += board[i][j]
        return sum

    def giant_squid_part_1(self):
        draws, boards = get_usable_input()
        for draw in draws:
            for board in boards:
                i, j = self._get_row_col(board, draw)
                if not (i == -1 and j == -1):
                    board[i][j] = -1
                    if self._check_if_won(board, i, j):
                        return self._get_sum(board) * draw

    def giant_squid_part_2(self):
        draws, boards = get_usable_input()
        for draw in draws:
            index = 0
            while index < len(boards):
                i, j = self._get_row_col(boards[index], draw)
                if not (i == -1 and j == -1):
                    boards[index][i][j] = -1
                    if self._check_if_won(boards[index], i, j):
                        if len(boards) == 1:
                            return self._get_sum(boards[0]) * draw
                        else:
                            boards.pop(index)
                    else:
                        index += 1
                else:
                    index += 1


print(GiantSquid().giant_squid_part_2())
