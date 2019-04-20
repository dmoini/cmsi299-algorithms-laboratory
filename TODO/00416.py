# 00416 - LED Test
import sys

digits = {'NNNNNNN': -1, 'YYYYYYN': 0, 'NYYNNNN': 1, 'YYNYYNY': 2, 'YYYYNNY': 3, 'NYYNNYY': 4,
         'YNYYNYY': 5, 'YNYYYYY': 6, 'YYYNNNN': 7, 'YYYYYYY': 8, 'YYYYNYY': 9}

while True:
    num_of_lines = sys.stdin.readline().strip()
    # print(f'num_of_lines: {num_of_lines}')
    if num_of_lines == '0':
        break
    countdown = 10
    match = True
    for _ in range(int(num_of_lines)):
        bits = sys.stdin.readline().strip()
        # print(f'bits: {bits}')
        print(digits.get(bits), bits, digits.get(bits) != None, countdown, end=' ')
        if digits.get(bits):
            print(digits.get(bits) < countdown)
        else:
            print()

        if (digits.get(bits) != None and digits.get(bits) < countdown):
            if digits.get(bits) == -1:
                countdown -= 1
            else:
                countdown = digits.get(bits)
        else:
            match = False
    print('MATCH') if match else print('MISMATCH')
    print('========================')