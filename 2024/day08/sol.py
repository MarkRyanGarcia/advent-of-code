with open("in.txt", 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

# def pgrid(input_grid):
#     for row in input_grid:
#         print(''.join(row))


m = len(grid)
n = len(grid[0])

def part1():
    locs = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                continue
            char = grid[i][j]
            for k in range(m):
                for l in range(n):
                    if grid[k][l] == '.' or (i == k and j == l):
                        continue
                    if grid[k][l] == char:
                        anti1 = 2*i-k, 2*j-l
                        anti2 = 2*k-i, 2*l-j
                        if anti1[0] in range(m) and anti1[1] in range(n):
                            locs.add(anti1)
                        if anti2[0] in range(m) and anti2[1] in range(n):
                            locs.add(anti2)
    return len(locs)


print(f"part1: {part1()}")


def part2():
    locs = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                continue
            char = grid[i][j]
            for k in range(m):
                for l in range(n):
                    if grid[k][l] == '.' or (i == k and j == l):
                        continue
                    if grid[k][l] == char:
                        locs.add((k,l))
                        locs.add((i,j))
                        vec = i-k, j-l

                        x, y = i, j
                        while x in range(m) and y in range(n):
                            if x + vec[0] in range(m) and y + vec[1] in range(n):
                                x, y = x + vec[0], y + vec[1]
                                locs.add((x, y))

                            else:
                                x, y = x + vec[0], y + vec[1]

                        x, y = k, l
                        while x in range(m) and y in range(n):
                            if x - vec[0] in range(m) and y - vec[1] in range(n):
                                x, y = x - vec[0], y - vec[1]
                                locs.add((x, y))
                            else:
                                x, y = x - vec[0], y - vec[1]
    return len(locs)


print(f"part2: {part2()}")
