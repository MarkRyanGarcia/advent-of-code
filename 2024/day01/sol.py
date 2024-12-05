a = []
b = []

with open("in.txt", 'r') as file:
    for line in file:
        i, j = line.split('   ')
        a.append(int(i))
        b.append(int(j))

a.sort()
b.sort()
res1 = 0
for i in range(len(a)):
    res1 += abs(a[i]-b[i])

print(f"part1: {res1}")


d = {}
res2 = 0
for i in b:
    if i not in d:
        d[i] = 0
    d[i] += 1

for i in a:
    try:
        res2 += i * d[i]
    except:
        continue

print(f"part2: {res2}")