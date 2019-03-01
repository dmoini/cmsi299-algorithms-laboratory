import sys
line_counter = 0
lines = sys.stdin.readlines()

while line_counter < len(lines):
    people, budget, hotels, _ = [int(x) for x in lines[line_counter].split(' ')]
    line_counter += 1
    costs = []
    for i in range(hotels):
        price = int(lines[line_counter])
        line_counter += 1
        max_beds = max([int(x) for x in lines[line_counter].split(' ')])
        line_counter += 1
        if max_beds < people:
            continue
        costs.append(price * people)
    if len(costs) == 0 or min(costs) > budget:
        print('stay home')
    else:
        print(min(costs))