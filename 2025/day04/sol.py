directions = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
    ]

grid = []

def part1(g):
    res = 0
    m, n = len(g), len(g[0])
    for r in range(m):
        for c in range(n):
            if g[r][c] == '@':
                neighbors = 0
                for dx, dy in directions:
                    i, j = r+dx, c+dy
                    if i in range(m) and j in range(n) and g[i][j] == '@':
                        neighbors += 1
                if neighbors < 4:
                    res += 1
    return res

def part2(g):
    res = 0
    m, n = len(g), len(g[0])
    while True:
        temp = res
        for r in range(m):
            for c in range(n):
                if g[r][c] == '@':
                    neighbors = 0
                    for dx, dy in directions:
                        i, j = r+dx, c+dy
                        if i in range(m) and j in range(n) and (g[i][j] == '@'):
                            neighbors += 1
                    if neighbors < 4:
                        res += 1
                        g[r][c] = 'x'
        if temp == res:
            break
    return res

with open("in.txt", 'r') as file:
    for line in file:
        grid.append([x for x in line.strip()])

print(f"part1: {part1(grid)}")
print(f"part2: {part2(grid)}")
