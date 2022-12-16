import collections


def get_usable_input():
    sensors = []
    beacons_in_row = collections.defaultdict(set)
    for line in open("input.txt"):
        row = line.split()
        sx, sy, bx, by = map(int, (row[2][2:-1], row[3][2:-1], row[8][2:-1], row[9][2:]))
        sensors.append((sx, sy, abs(sx - bx) + abs(sy - by)))
        beacons_in_row[by].add(bx)

    return sensors, beacons_in_row


class BeaconExclusionZone:
    def union(self, intervals):
        intervals.sort()
        current = intervals[0]
        for ivl in intervals[1:]:
            if current[1] < ivl[0]:
                yield current
                current = ivl
            elif ivl[1] > current[1]:
                current[1] = ivl[1]
        yield current

    def intersect_with(self, intervals, ivl):
        return [[max(iv[0], ivl[0]), min(iv[1], ivl[1])] for iv in intervals]

    def empty_intervals_in_line(self, Y, sensors):
        return [[x - d + vd, x + d - vd] for x, y, d in sensors if (vd := abs(Y - y)) <= d]

    def part_1(self):
        # Part 1
        sensors, beacons_in_row = get_usable_input()
        Y = 2_000_000
        p1 = sum(
            x1 - x0 + 1 - sum(x0 <= bx <= x1 for bx in beacons_in_row[Y])
            for x0, x1 in self.union(self.empty_intervals_in_line(Y, sensors))
        )
        print(p1)

    def part_2(self):
        # Part 2
        sensors, beacons_in_row = get_usable_input()

        def solution(maxY, startY):
            for Y in range(startY, maxY + 1):
                intervals = list(self.union(self.intersect_with(self.empty_intervals_in_line(Y, sensors), [0, maxY])))
                if len(intervals) == 2:
                    return maxY * (intervals[0][1] + 1) + Y

        p2 = solution(4_000_000, 2_634_000)
        print(p2)


BeaconExclusionZone().part_1()
BeaconExclusionZone().part_2()
