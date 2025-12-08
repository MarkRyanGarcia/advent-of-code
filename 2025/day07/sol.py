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
            below = grid[r+1][c]
            if below == '.':
                grid[r+1][c] = '|'
                next_beams.append((r+1,c))
            elif below == '^':
                grid[r+1][c-1] = '|'
                next_beams.append((r+1,c-1))
                next_beams.append((r+1,c+1))
                res += 1
        beams = next_beams
        row += 1
    return res

def part2(grid) -> int:
    m, n = len(grid), len(grid[0])
    grid[1][n//2] = 1
    for r in range(1, m-1):
        for c in range(n):
            i = grid[r][c] if type(grid[r][c]) == int else 0
            if i == 0:
                continue
            below = grid[r+1][c]
            if below != '^':
                if type(grid[r+1][c]) == int:
                    grid[r+1][c] += i
                else:
                    grid[r+1][c] = i
            elif below == '^':
                if c-1 in range(n):
                    if type(grid[r+1][c-1]) == int:
                        grid[r+1][c-1] += i
                    else:
                        grid[r+1][c-1] = i
                if c+1 in range(n):
                    if type(grid[r+1][c+1]) == int:
                        grid[r+1][c+1] += i
                    else:
                        grid[r+1][c+1] = i
    return sum([x for x in grid[m-1] if type(x) == int])

def printgrid(grid):
    for row in grid:
        r = [str(x) for x in row]
        print(r)

lines = open("in.txt").readlines()
grid = []
for line in lines:
    grid.append([x for x in line.rstrip('\n')])
grid2 = deepcopy(grid)
print(f"part1: {part1(grid)}")
print(f"part2: {part2(grid2)}")
