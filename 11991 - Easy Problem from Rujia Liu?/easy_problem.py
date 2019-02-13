import sys

while True:
    try:
        size, queries = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))

        g = {}

        for i, x in enumerate(a):
            if x not in g:
                g[x] = []
            g[x].append(i + 1)

        for _ in range(queries):
            k, v = map(int, sys.stdin.readline().split())
            if len(g[v]) < k:
                print(0)
            else:
                print(g[v][k - 1])
    except:
        break