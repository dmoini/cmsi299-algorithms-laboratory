import sys

def allUnique(a, f):
    count = [0 for i in range(10)]
    while a != 0:
        count[a % 10] += 1
        a //= 10
    while f != 0:
        count[f % 10] += 1
        f //= 10
    for c in count:
        if c != 1:
            return False
    return True

first_line = True
while(True):
    line = sys.stdin.readline().strip()
    if line == '0':
        break
    if not first_line:
        print()
    first_line = False
    n = int(line)
    if (n < 2 or n > 79):
        print(f'There are no solutions for {n}.')
        continue
    no_solution = True
    for f in range(1234, 98766):
        a = n * f
        a_print, f_print = 0, 0
        if a > 98765:
            break
        if a < 10000:
            a_print = a * 10
        else:
            a_print = a
        if f < 10000:
            f_print = f * 10
        else:
            f_print = f
        if allUnique(a_print, f_print):
            if a < 10000:
                print(f'0{a} / {f} = {n}')
            elif f < 10000:
                print(f'{a} / 0{f} = {n}')
            else:
                print(f'{a} / {f} = {n}')
            no_solution = False
    if no_solution:
        print(f'There are no solutions for {n}.')
    # print()