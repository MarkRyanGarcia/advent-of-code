from intervaltree import Interval, IntervalTree

def part1(ranges, ids):
    res = 0
    for i in ids:
        for r1, r2 in ranges:
            if i in range(r1, r2+1):
                res += 1
                break
    return res

def part2(ranges):
    tree = IntervalTree.from_tuples((r1, r2+1) for r1, r2 in ranges)
    tree.merge_overlaps()
    combined = sorted([(interval.begin, interval.end) for interval in tree])

    res = 0
    for c1, c2 in combined:
        res += c2-c1

    return res

with open("in.txt", 'r') as file:
    ranges = []
    ids = []
    for line in file:
        if '-' in line.strip():
            r1, r2 = map(int, line.strip().split('-'))

            ranges.append((r1, r2))
        elif len(line.strip()) > 0:
            ids.append(int(line.strip()))
    ranges.sort()
    print(f"part1: {part1(ranges, ids)}")
    print(f"part2: {part2(ranges)}")