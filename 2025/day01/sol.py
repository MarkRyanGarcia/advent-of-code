i = 50
res1 = 0
res2 = 0

with open("in.txt", 'r') as file:
    for line in file:
        if line[0] == 'L':
            for j in range(int(line[1:])):
                i -= 1
                if i == 0:
                    res2 += 1
                elif i == -1:
                    i = 99
        elif line[0] == 'R':
            for j in range(int(line[1:])):
                i += 1
                if i == 100:
                    i = 0
                    res2 += 1
        if i == 0:
            res1 += 1

print(f"part1: {res1}")

print(f"part2: {res2}")