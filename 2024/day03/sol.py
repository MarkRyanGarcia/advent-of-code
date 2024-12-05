import re

res = 0
pattern = r"mul\((\d+),(\d+)\)"
k = []
with open("in.txt", 'r') as file:
    for line in file:
        m = re.findall(pattern, line)
        k.append(m)
        # print(m)
for m in k:
    for n in m:
        i, j = int(n[0]), int(n[1])
        res += i * j


print(f"part1: {res}")


pattern2 = r"(do\(\)|don't\(\))"
res2 = 0
b = True

with open("in.txt", "r") as file:
    for line in file:
        for i in re.finditer(rf"{pattern2}|{pattern}", line):
            k = i.group()
            if k == "do()":
                b = True
            elif k == "don't()":
                b = False
            elif b and re.match(pattern, k):
                x, y = map(int, re.findall(r"\d+", k))
                res2 += x * y

print(f"part2: {res2}")
