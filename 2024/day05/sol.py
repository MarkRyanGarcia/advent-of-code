
with open("in.txt", 'r') as file:
    r, u = file.read().split("\n\n")

rules = {tuple(map(int, line.split("|"))) for line in r.splitlines()}
updates = [list(map(int, line.split(","))) for line in u.splitlines()]


def isOrdered(update):
    for i in range(len(update)-1):
        for j in range(i, len(update)):
            if (update[j],update[i]) in rules:
                return False
    return True

good_updates = []
bad_updates = []

for update in updates:
    if isOrdered(update):
        good_updates.append(update)
    else:
        bad_updates.append(update)

res = 0
for update in good_updates:
    res += update[len(update)//2]

print(f"part1: {res}")


def fix_update(update):
    fixed = update.copy()
    swapped = True    
    while swapped:
        swapped = False
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if (fixed[j], fixed[i]) in rules:
                    fixed[i], fixed[j] = fixed[j], fixed[i]
                    swapped = True
    return fixed


res2 = 0
for update in bad_updates:
    new = fix_update(update)
    if new:
        res2 += new[len(new)//2]

print(f"part2: {res2}")