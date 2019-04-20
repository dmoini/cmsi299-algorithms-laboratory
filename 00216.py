# 216 - Getting in Line
import sys
import math
from itertools import permutations

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

case = 1
while True:
    num_points = int(sys.stdin.readline().strip())
    if num_points == 0:
        break
    points = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(num_points)]
    graph = [[0 for _ in range(num_points)] for _ in range(num_points)]
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            graph[i][j] = graph[j][i] = get_distance(points[i][0], points[i][1], points[j][0], points[j][1])
    
    min_perm, min_dist = None, math.inf
    for p in permutations(range(num_points)):
        dist = sum(graph[p[i]][p[i + 1]] for i in range(num_points - 1))
        if dist < min_dist:
            min_dist, min_perm = dist, p

    print('**********************************************************')
    print(f'Network #{case}')
    for i in range(num_points - 1):
        a, b = min_perm[i], min_perm[i + 1]
        x1, y1 = points[a]
        x2, y2 = points[b]
        print(f'Cable requirement to connect ({x1},{y1}) to ({x2},{y2}) is {graph[a][b] + 16:.2f} feet.')
    print(f'Number of feet of cable required is {min_dist + (num_points - 1) * 16:.2f}.')
    case += 1