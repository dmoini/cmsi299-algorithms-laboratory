import sys

while True:
    try:
        nums = sys.stdin.readline().split()
        r, n = float(nums[0]), int(nums[1])
    except:
        break
    # print(r, n)
    print(r ** n)