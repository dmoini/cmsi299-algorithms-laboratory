import sys
from collections import deque

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    result = deque()
    currStr = []
    tail = True
    for c in line:
        if c == '[':
            if tail:
                result.append(''.join(currStr))
                tail = False
            else:
                result.appendleft(''.join(currStr))
            currStr = []
        elif c == ']':
            if not tail:
                result.appendleft(''.join(currStr))
                tail = True
            else:
                result.append(''.join(currStr))
            currStr = []
        else:
            currStr.append(c)
    result.append(''.join(currStr)) if tail else result.appendleft(''.join(currStr))
    print(''.join(result))