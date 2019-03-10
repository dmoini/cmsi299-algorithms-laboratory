import sys

class Disjoint_Set():
    def __init__(self):
        self.network = {}
    def add(self, x):
        if x not in self.network:
            self.network[x] = [x, None, 1]
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return x_root[2]
        if x_root[2] < y_root[2]:
            x_root, y_root = y_root, x_root
        y_root[1] = x_root[0]
        x_root[2] += y_root[2]
        return x_root[2]
    def find(self, x):
        if self.network[x][1] is not None:
            self.network[x] = self.find(self.network[x][1])
        return self.network[x]

cases = int(sys.stdin.readline())
sys.stdin.readline()

for _ in range(cases):
    if _ != 0:
        print()
    num_computers = int(sys.stdin.readline())
    network = Disjoint_Set()
    for c in range(1, num_computers + 1):
        network.add(c)
    found, not_found = 0, 0
    while True:
        try:
            letter, computerA, computerB = sys.stdin.readline().split()
        except:
            break
        computerA, computerB = int(computerA), int(computerB)
        if letter == 'c':
            network.union(computerA, computerB)
        elif letter == 'q':
            connectionA, connectionB = network.find(computerA), network.find(computerB)
            if connectionA != connectionB:
                not_found += 1
            else:
                found += 1
    print(f'{found},{not_found}')