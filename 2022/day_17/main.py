def get_usable_input():
    stream = open('input.txt').read().strip()
    return stream

def solution():
    data = get_usable_input()

    R = set([(x, 0) for x in range(7)])
    L = 1000000000000

    def get_piece(type, y):
        pieces = {
            0: {(2, y), (3, y), (4, y), (5, y)},
            1: {(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)},
            2: {(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)},
            3: {(2, y), (2, y + 1), (2, y + 2), (2, y + 3)},
            4: {(2, y + 1), (2, y), (3, y + 1), (3, y)}
        }
        return pieces[type]

    def move_left(piece):
        if any([x == 0 for (x, y) in piece]):
            return piece
        return set([(x - 1, y) for (x, y) in piece])

    def move_right(piece):
        if any([x == 6 for (x, y) in piece]):
            return piece
        return set([(x + 1, y) for (x, y) in piece])

    def move_down(piece):
        return set([(x, y - 1) for (x, y) in piece])

    def move_up(piece):
        return set([(x, y + 1) for (x, y) in piece])

    def signature(r):
        maxY = max([y for (x, y) in r])
        return frozenset([(x, maxY - y) for (x, y) in r if maxY - y <= 30])

    SEEN = {}
    top = 0
    i = 0
    t = 0
    added = 0
    while t < L:

        piece = get_piece(t % 5, top + 4)

        while True:
            if data[i] == '<':
                piece = move_left(piece)
                if piece & R:
                    piece = move_right(piece)
            else:
                piece = move_right(piece)

                if piece & R:
                    piece = move_left(piece)

            i = (i + 1) % len(data)

            piece = move_down(piece)

            if piece & R:
                piece = move_up(piece)
                R |= piece
                top = max([y for (x, y) in R])

                SR = (i, t % 5, signature(R))
                if SR in SEEN and t >= 2022:
                    (oldt, oldy) = SEEN[SR]
                    dy = top - oldy
                    dt = t - oldt
                    amt = (L - t) // dt
                    added += amt * dy
                    t += amt * dt

                SEEN[SR] = (t, top)
                break
        t += 1

        if t == 2022:
            print(top)
    print(top + added)


solution()
