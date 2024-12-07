from itertools import product
from alive_progress import alive_bar

# Initialize totals and vals
totals = []
vals = []

# Parse the input file
with open("in.txt", 'r') as file:
    for line in file:
        x = line.split(':')[0]
        y = line.split(':')[1].strip().split(' ')
        totals.append(int(x))
        vals.append(list(map(int, y)))

def part1():
    data = zip(totals, vals)
    ops = ['+', '*']
    res = 0
    for total, nums in data:
        possibilities = product(ops, repeat=len(nums) - 1)
        for p in possibilities:
            temp = nums[0]
            for n in range(len(nums) - 1):
                if p[n] == '+':
                    temp += nums[n + 1]
                else:
                    temp *= nums[n + 1]
            if temp == total:
                res += total
                break
    return res

print(f"part1: {part1()}")

def part2():
    data = zip(totals, vals)
    ops = ['+', '*', '|']
    res = 0
    total_combinations = sum(3 ** (len(nums) - 1) for nums in vals)

    with alive_bar(total_combinations) as bar:
        for total, nums in data:
            possibilities = product(ops, repeat=len(nums) - 1)
            for p in possibilities:
                temp = nums[0]
                for n in range(len(nums) - 1):
                    if p[n] == '+':
                        temp += nums[n + 1]
                    elif p[n] == '*':
                        temp *= nums[n + 1]
                    else:
                        temp = int(str(temp) + str(nums[n + 1]))
                if temp == total:
                    res += total
                    bar()
                    break
                bar()
    return res

print(f"part2: {part2()}")
