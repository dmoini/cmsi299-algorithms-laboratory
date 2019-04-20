# 00748 - Exponentiation
import sys

while True:
    try:
        nums = sys.stdin.readline().split()
        R, n = str(nums[0]), int(nums[1])
    except:
        break
    index = R.find('.')
    decimalIndex = (5 - index) * n
    R = int(R.replace('.', ''))
    R = str(R ** n)
    left = R[:-1 * decimalIndex]
    right = R[-1 * decimalIndex:]
    if decimalIndex > len(right):
        right = '0' * (decimalIndex - len(right)) + right
    right = right.rstrip('0')
    print(f'{left}.{right}')