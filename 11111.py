# 11111 - Generalized Matrioshkas
import sys

while True:
    matrioshkas = list(map(int, sys.stdin.readline().strip().split()))
    if not matrioshkas:
        break
    stack = []
    invalid = False
    for m in matrioshkas:
        if m < 0:
            if not stack:
                stack.append([m, abs(m)])
            elif stack[-1][1] > abs(m):
                stack[-1][1] -= abs(m)
                stack.append([m, abs(m)])
            else:
                invalid = True
                break
        else:
            if not stack or stack[-1][0] != m * -1:
                invalid = True
                break
            else:
                stack.pop()
    if invalid or stack:
        print(':-( Try again.')
    else:
        print(':-) Matrioshka!')