from alive_progress import alive_bar

def pgrid(input_grid):
    for row in input_grid:
        print(' '.join(row))

with open("in.txt", 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

m = len(grid)
n = len(grid[0])


directions = [
    (-1, 0),  # Up
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1)   # Left
]


start = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == '^':
            start = (i, j)
            break

def part1(g):
    x, y = start
    di = 0
    while x in range(m) and y in range(n):
        dx, dy = x + directions[di][0], y + directions[di][1]

        if dx in range(m) and dy in range(n) and g[dx][dy] == '#':
            di = (di + 1) % 4
        else:
            g[x][y] = 'X'
            x, y = dx, dy

    return sum(row.count('X') for row in g)

print(f"part1: {part1(grid)}")

def check(g):
    x, y = start
    di = 0
    visited = set()

    while x in range(m) and y in range(n):
        state = (x, y, di)
        if state in visited:
            return True
        visited.add(state)

        dx, dy = x + directions[di][0], y + directions[di][1]

        if dx in range(m) and dy in range(n) and g[dx][dy] == '#':
            di = (di + 1) % 4
        else:
            x, y = dx, dy

    return False

def part2():
    g = [x.copy() for x in grid]
    part1(g)
    result = 0

    with alive_bar(m * n) as bar:
        for i in range(m):
            for j in range(n):
                if g[i][j] == 'X':
                    new_grid = [x.copy() for x in grid]
                    new_grid[i][j] = '#'
                    if check(new_grid):
                        result += 1
                bar()
    return result


print(f"part2: {part2()}")