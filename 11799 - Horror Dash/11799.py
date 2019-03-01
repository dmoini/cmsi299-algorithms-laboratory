import sys

num_of_lines = int(sys.stdin.readline().strip())
for i in range(num_of_lines):
    line = sys.stdin.readline().strip()
    arr = line.split()
    arr = list(map(int, arr))
    print(f'Case {i + 1}: {max(arr[1:])}')