res1 = 0
res2 = 0

def isInvalid1(num):
    return num[0:len(num)//2] == num[len(num)//2:]

def isInvalid2(num):
    thing = num[0:len(num)//2]
    while len(thing) > 0:
        if thing * int(len(num)/len(thing)) == num:
            return True
        thing = thing[0:-1]
    return False

with open("in2.txt", 'r') as file:
    for line in file:
        ranges = line.strip().split(',')
        for r in ranges:
            i, j = map(int, r.split('-'))
            for num in range(i, j+1):
                if isInvalid1(str(num)):
                    res1 += num
                if isInvalid2(str(num)):
                    res2 += num



print(f"part1: {res1}")

print(f"part2: {res2}")