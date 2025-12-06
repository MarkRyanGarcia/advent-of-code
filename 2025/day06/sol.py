def part1(file):
    nums = []
    for line in file:
        nums.append([x for x in line.strip().split() if x])
    res = 0
    m, n = len(nums), len(nums[0])
    for c in range(n):
        operation = nums[-1][c]
        column = 0 if operation == '+' else 1
        for r in range(m-1):
            if operation == '+':
                column += int(nums[r][c])
            else:
                column *= int(nums[r][c])
        res += column
    return res

def part2(file):
    grid = []
    for line in file:
        grid.append([x for x in line])

    grid = grid[::-1]

    m, n = len(grid), len(grid[0])
    columns = []
    for c in range(n):
        column = 0
        place = 0
        for r in range(1,m):
            if grid[r][c] != ' ':
                column += int(grid[r][c]) * 10**(place)
                place += 1
        columns.append(column)
    operations = [x for x in grid[0] if x != ' ']
    columns.append(0)

    res, i, j = 0, 0, 0
    operation = operations[j]
    local = 0 if operation == '+' else 1
    while i < len(columns):
        if columns[i] == 0:
            res += local
            j += 1
            if j == len(operations):
                break
            operation = operations[j]
            local = 0 if operation == '+' else 1
        else:
            if operation == '+':
                local += columns[i]
            else:
                local *= columns[i]
        i += 1
    return res

with open("in.txt", 'r') as file:
    f = file.readlines()
    print(f"part1: {part1(f)}")
    print(f"part2: {part2(f)}")