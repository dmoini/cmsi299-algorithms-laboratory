# 11503 - Virtual Friends
import sys

class DisjointSet():
    def __init__(self):
        self.network = {}
    def add(self, x):
        if x not in self.network:
            self.network[x] = [x, None, 1]
    def union(self, x, y): # return the size of the new group
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
for _ in range(cases):
   num_connections = int(sys.stdin.readline())
   s = DisjointSet()
   for connections in range(num_connections):
       friends = sys.stdin.readline().strip().split()
       s.add(friends[0])
       s.add(friends[1])
       print(s.union(friends[0], friends[1]))