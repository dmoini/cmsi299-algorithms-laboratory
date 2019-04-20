# 11235 - Frequent values
import sys
from collections import Counter

while True:
    try:
        data = list(map(int, sys.stdin.readline().split()))
        if len(data) == 1:
            break
    except:
        break
    values = list(map(int, sys.stdin.readline().split()))
    for _ in range(data[1]):
        l, r = list(map(int, sys.stdin.readline().split()))
        counter = Counter(values[l - 1:r])
        print(max(counter.values()))