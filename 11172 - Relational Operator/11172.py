import sys

first = True
for line in sys.stdin:
    line = line.strip()
    if first:
        first = False
        continue
    line = list(map(int, line.strip().split()))
    x, y = line[0], line[1]
    print('<') if x < y else print('>') if x > y else print('=')