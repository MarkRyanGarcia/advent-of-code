from collections import Counter

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def distance(box1, box2):
    x1,y1,z1 = box1[1]
    x2,y2,z2 = box2[1]
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

def part1(boxes, pairs_to_connect=1000):
    n = len(boxes)
    connections = []
    for i in range(n):
        for j in range(i+1, n):
            connections.append((distance(boxes[i], boxes[j]), i, j))
    connections.sort()

    uf = UnionFind(n)
    for idx, (dist, i, j) in enumerate(connections[:pairs_to_connect]):
        uf.union(i, j)

    comp_sizes = Counter()
    for i in range(n):
        root = uf.find(i)
        comp_sizes[root] += 1

    largest = sorted(comp_sizes.values(), reverse=True)[:3]
    while len(largest) < 3:
        largest.append(1)
    return largest[0] * largest[1] * largest[2]

def part2(boxes):
    n = len(boxes)
    connections = []
    for i in range(n):
        for j in range(i+1, n):
            connections.append((distance(boxes[i], boxes[j]), i, j))
    connections.sort()

    uf = UnionFind(n)
    connections_left = n

    for dist, i, j in connections:
        if uf.union(i, j):
            connections_left -= 1
            if connections_left == 1:
                x1 = boxes[i][1][0]
                x2 = boxes[j][1][0]
                return x1 * x2

    return None

lines = open("in.txt").readlines()
boxes = []
boxId = 0
for line in lines:
    boxes.append((boxId, [int(x) for x in line.rstrip('\n').split(',')]))
    boxId += 1
print(f"part1: {part1(boxes, 1000)}")


print(f"part2: {part2(boxes)}")