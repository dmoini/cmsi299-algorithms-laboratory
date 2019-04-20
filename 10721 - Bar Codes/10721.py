import sys

while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    n, k, m = map(int, line.split())
    dp = [[0 for _ in range(64)] for _ in range(64)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for l in range(1, m + 1):
                if j - l >= 0:
                    dp[i][j] += dp[i - 1][j - l]
    print(dp[k][n])