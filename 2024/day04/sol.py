
with open("in.txt", 'r') as file:
    grid = [line.strip() for line in file]

word = "XMAS"

rows, cols = len(grid), len(grid[0])
res = 0
directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-right
    (1, -1),  # Down-left
    (-1, 1),  # Up-right
    (-1, -1)  # Up-left
]

def check_direction(r, c, x, y):
    for i in range(4):
        nr, nc = r + i * x, c + i * y
        if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] != word[i]:
            return False
    return True

for r in range(rows):
    for c in range(cols):
        for i, j in directions:
            if check_direction(r, c, i, j):
                res += 1


print(f"part1: {res}")


word2 = "MAS"
count = 0

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if grid[r][c] != "A":
            continue

        # \
        down_right = grid[r - 1][c - 1] + 'A' + grid[r + 1][c + 1]
        # /
        down_left = grid[r - 1][c + 1] + 'A' + grid[r + 1][c - 1]

        if (down_right == word2 or down_right == word2[::-1]) and (down_left == word2 or down_left == word2[::-1]):
            count += 1

print(f"part2: {count}")
