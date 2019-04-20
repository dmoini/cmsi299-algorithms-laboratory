# 11060 - Beverages
import sys
from collections import OrderedDict

case = 1

while True:
    num_of_drinks = sys.stdin.readline()
    if num_of_drinks == '':
        break
    drinks = OrderedDict()
    ordered_drinks = []
    for _ in range(int(num_of_drinks)):
        drinks.update({sys.stdin.readline().strip(): [0, []]})
    for _ in range(int(sys.stdin.readline())):
        first_drink, second_drink = sys.stdin.readline().strip().split()
        drinks.get(first_drink)[1].append(second_drink)
        drinks.get(second_drink)[0] += 1

    while drinks:
        for k, v in drinks.items():
            if v[0] == 0:
                for successor in range(len(v[1])):
                    drinks.get(v[1][successor])[0] -= 1
                ordered_drinks.append(k)
                drinks.pop(k)
                break
    
    print(f'Case #{case}: Dilbert should drink beverages in this order: ', end='')
    print(*ordered_drinks, end='.\n\n')
    case += 1

    sys.stdin.readline()