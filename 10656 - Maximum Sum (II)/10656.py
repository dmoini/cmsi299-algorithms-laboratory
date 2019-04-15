import sys

while True:
    line = int(sys.stdin.readline().strip())
    if line == 0:
        break
    nums = [0 for x in range(line)]
    for i in range(line):
        nums[i] = int(sys.stdin.readline().strip())
    nums = [n for n in nums if n != 0]
    print(' '.join(str(n) for n in nums)) if nums else print('0')