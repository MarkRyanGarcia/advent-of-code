with open("in.txt", 'r') as file:
    mat = []
    for line in file:
        n = []
        for i in line.strip().split(' '):
            n.append(int(i))
        mat.append(n)

res = 0
h = []

def is_safe(row):
    inc = True
    dec = True
    c = True
    for j in range(len(row) - 1):
        if row[j] >= row[j + 1]:
            inc = False
        if row[j] <= row[j + 1]:
            dec = False
        if abs(row[j] - row[j + 1]) not in range(1, 4):
            c = False
    return (c and inc) or (c and dec)

for i in mat:
    if is_safe(i):
        res += 1
    else:
        h.append(i)

print(f"part1: {res}")


g = 0
for k in h:
    for u in range(len(k)):
        o = k[:u] + k[u + 1:]
        if is_safe(o):
            g += 1
            break

print(f"part2: {res+g}")