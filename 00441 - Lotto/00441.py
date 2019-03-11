import sys

first_line = True
while True:
    line = sys.stdin.readline().strip()
    if line == '0':
        break
    if not first_line:
        print()
    first_line = False
    line = list(map(int, line.split()))
    length, line = line[0], line[1:]
    l = len(line)
    ans = [-1] * 6
    for a in range(l):
        ans[0] = line[a]
        for b in range(a + 1, l):
            ans[1] = line[b]
            for c in range(b + 1, l):
                ans[2] = line[c]
                for d in range(c + 1, l):
                    ans[3] = line[d]
                    for e in range(d + 1, l):
                        ans[4] = line[e]
                        for f in range(e + 1, l):
                            ans[5] = line[f]
                            print(' '.join(str(x) for x in ans))