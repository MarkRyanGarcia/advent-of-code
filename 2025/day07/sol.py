from copy import deepcopy
def part1(grid):
    m, n = len(grid), len(grid[0])
    s_idx = n//2
    grid[1][s_idx] = '|'
    beams = [(1,s_idx)]
    row = 1
    res = 0
    while row in range(m-1):
        next_beams = []
        for r, c in beams:
            if grid[r+1][c] == '.':
                grid[r+1][c] = '|'
                next_beams.append((r+1,c))
            elif grid[r+1][c] == '^':
                grid[r+1][c-1] = '|'
                grid[r+1][c+1] = '|'
                next_beams.append((r+1,c-1))
                next_beams.append((r+1,c+1))
                res += 1
        beams = next_beams
        row += 1
    return res

def part2(grid) -> int:
    m, n = len(grid), len(grid[0])
    s_idx = n//2
    grid[1][s_idx] = '|'
    counts = [[0] * n for _ in range(m)]
    counts[1][s_idx] = 1

    for r in range(1, m-1):
        for c in range(n):
            i = counts[r][c]
            if i == 0:
                continue
            below = grid[r+1][c]
            if below == '.':
                counts[r+1][c] += i
            elif below == '^':
                if c-1 in range(n):
                    counts[r+1][c-1] += i
                if c+1 in range(n):
                    counts[r+1][c+1] += i
    return sum(counts[m-1])

lines = open("in.txt").readlines()
grid = []
for line in lines:
    grid.append([x for x in line.rstrip('\n')])
grid2 = deepcopy(grid)
print(f"part1: {part1(grid)}")
print(f"part2: {part2(grid2)}")
