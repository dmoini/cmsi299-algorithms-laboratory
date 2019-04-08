import sys

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    line = list(map(int, line.split()))
    path, best = [], [0, 0]
    max_tape_size, N = line[0], line[1]
    line = line[2:]

    def backtrack(total, step):
        if total > max_tape_size:
            return
        if step == N:
            if total >= best[1]:
                best[0] = list(path)
                best[1] = sum(path)
            return
        backtrack(total, step + 1)
        path.append(line[step])
        backtrack(total + line[step], step + 1)
        path.pop()

    backtrack(0, 0)
    print(' '.join(list(map(str, best[0]))), 'sum:' + str(best[1]))