# 00514 - Rails
import sys

first = True
while True:
    train_num = int(sys.stdin.readline().strip())
    if train_num == 0:
        break
    if not first:
        print()
    first = False
    while True:
        line = sys.stdin.readline().strip()
        if line == '0':
            break
        incoming_trains = [x for x in range(train_num, 0, -1)]
        outgoing_trains = list(reversed(list(map(int, line.split()))))
        stack = []
        while incoming_trains:
            stack.append(incoming_trains.pop())
            while len(outgoing_trains) and len(stack) and outgoing_trains[-1] == stack[-1]:
                outgoing_trains.pop()
                stack.pop()
        print('No') if len(stack) else print('Yes')
print()