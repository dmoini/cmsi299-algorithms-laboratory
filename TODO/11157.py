# 11157 - Dynamic Frog
import sys

num_of_tests = int(sys.stdin.readline().strip())
case = 1
for _ in range(num_of_tests):
    N, D = map(int, sys.stdin.readline().strip().split())
    rocks = list(map(lambda x: [x[0], int(x[2:]), True], sys.stdin.readline().strip().split()))
    rocks.insert(0, ['L', 0, True])
    rocks.append(['R', D, True])
    max_jump = 0
    for i, r in enumerate(rocks[1:]):
        curr_jump = r[1] - rocks[i][1]
        if r[2]:
            max_jump = max(max_jump, curr_jump)
            if r[0] == 'S':
                r[2] = False
    
    curr_index = len(rocks) - 1
    for i in range(len(rocks) - 2, -1, -1):
        if not rocks[i][2]:
            continue
            # pass
        # print(rocks[i], i)
        curr_jump = rocks[curr_index][1] - rocks[i][1]
        # print(f'cj: {curr_jump}')
        max_jump = max(max_jump, curr_jump)
        curr_index = i
    print(f'Case {case}: {max_jump}')
    case += 1
    
    # print(f'mj: {max_jump} || {rocks}', end='\n=================\n')
    
    # print(list(reversed(rocks[:len(rocks) - 1])))
    # for i, r in enumerate(reversed(rocks[:len(rocks) - 1])):
    #     print(i, r, rocks[len(rocks) - i - 1], end='\n===================\n')
    #     curr_jump = rocks[len(rocks) - i - 1][1] - r[1]
    #     print(f'curr_jump: {curr_jump}')
    
    # for i, r in enumerate(reversed(rocks[:len(rocks) - 1])):
    #     curr_jump = abs(r[1] - rocks[len(rocks) - i][1] - 1)
    #     print(curr_jump)
    # print(f'max_jump: {max_jump}')
    # max_jump = (max_jump, D - rocks[-1][1])