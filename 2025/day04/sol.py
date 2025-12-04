from copy import deepcopy

directions = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
    ]
    
grid = []

def part1(g):
    res = 0
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '@':
                neighbors = 0
                for dx, dy in directions:
                    i, j = r+dx, c+dy
                    if i in range(len(g)) and j in range(len(g[0])) and g[i][j] == '@':
                        neighbors += 1
                if neighbors < 4:
                    res += 1
    return res

def part2(g):
    res = 0
    temp2 = deepcopy(g)
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '@':
                neighbors = 0
                for dx, dy in directions:
                    i, j = r+dx, c+dy
                    if i in range(len(g)) and j in range(len(g[0])) and (g[i][j] == '@'):
                        neighbors += 1
                if neighbors < 4:
                    res += 1
                    g[r][c] = 'x'
    return res + part2(g) if temp2 != g else res

with open("in.txt", 'r') as file:
    for line in file:
        grid.append([x for x in line.strip()])

print(f"part1: {part1(grid)}")
print(f"part2: {part2(grid)}")
