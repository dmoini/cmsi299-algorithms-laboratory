import sys

while True:
    n, d, r = map(int, sys.stdin.readline().strip().split())
    if n == d == r == 0:
        break
    morning = list(map(int, sys.stdin.readline().strip().split()))
    morning.sort()
    evening = list(map(int, sys.stdin.readline().strip().split()))
    evening.sort(reverse=True)
    overtime = 0
    for i in range(n):
        route_hours = morning[i] + evening[i]
        if route_hours > d:
            overtime += route_hours - d
    print(overtime * r)