import sys
import math

cases = sys.stdin.readlines()
for case in cases:
    a, b, c = map(float, case.strip().split())
    if a <= 0 or b <= 0 or c <= 0:
        print('The radius of the round table is: 0.000')
        continue
    hp = (a + b + c) / 2
    area = math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))
    perim = a + b + c
    radius = 2 * area / perim
    print('The radius of the round table is: {:.3f}'.format(radius))