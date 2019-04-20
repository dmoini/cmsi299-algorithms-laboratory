# 10491 - Cows and Cars
import sys

while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    cows, cars, show = map(int, line.split())
    doors = cows + cars
    unopened_doors = doors - show - 1
    ans = (cows / doors) * (cars / unopened_doors) + (cars / doors) * ((cars - 1) / unopened_doors)
    print(f'{ans:.5f}')
