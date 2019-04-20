# 10420 - List of Conquests
import fileinput

countries_map = {}
for line in fileinput.input():
    line = line.rstrip()
    if line[0].isdigit():
        continue
    space_index = line.find(' ')
    country = line[:space_index]
    countries_map[country] = countries_map.get(country, 0) + 1
ans = []
for k, v in countries_map.items():
    ans.append(k + ' ' + str(v))
ans.sort()
print('\n'.join(ans))