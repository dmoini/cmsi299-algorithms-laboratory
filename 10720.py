# 10720 - Graph Construction
import sys

def isValidDegreeSequence(sequence):
    if sequence[-1] < 0 or sum(sequence) % 2 != 0:
        return False      
    for i in range(1, len(sequence) + 1):
        sumOfDegree = sum(sequence[:(i)])          
        partialSum = i * (i - 1)
        for j in range(i + 1, len(sequence) + 1):
            partialSum += min(i, sequence[j - 1])
        if sumOfDegree > partialSum:
            return False
    return True

while True:
    sequence = sys.stdin.readline().strip()
    if sequence == '0':
        break
    sequence = list(map(int, sequence.split()))
    sequence.sort(key=lambda x: -x)
    if isValidDegreeSequence(sequence[1:]):
        print('Possible')
    else:
        print('Not possible')