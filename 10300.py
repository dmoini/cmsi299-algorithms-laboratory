# 10300 - Ecological Premium
import sys

lines = [lines.strip() for lines in sys.stdin.readlines()]
i = 1
while i < len(lines):
    farmers = int(lines[i])
    i += 1
    cost = 0
    for _ in range(farmers):
        footage, animals, friendliness = [int(x) for x in lines[i].split()]
        cost += footage * friendliness
        i += 1
    print(cost)