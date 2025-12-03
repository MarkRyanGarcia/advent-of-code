res1 = 0
res2 = 0

def getLargestVoltage1(bank):
    voltage = int(bank[0:2])
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):    
            voltage = max(voltage, int(bank[i] + bank[j]))
    return int(voltage)

def getLargestVoltage2(bank):
    voltage = int(bank[0:12])
    for i in range(12,len(bank)):
        thing = str(voltage)
        for j in range(11):
            if int(thing[j+1]) > int(thing[j]):
                thing = thing[0:j] + thing[j+1:] + bank[i]
                break
        voltage = max(voltage, int(''.join(c for i, c in enumerate(str(voltage)) if i != str(voltage).find(min(str(voltage)))) + bank[i]), int(thing))
    return int(voltage)


with open("in.txt", 'r') as file:
    for line in file:
        res1 += getLargestVoltage1(line.strip())
        res2 += getLargestVoltage2(line.strip())

print(f"part1: {res1}")

print(f"part2: {res2}")