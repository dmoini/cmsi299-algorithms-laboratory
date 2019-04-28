# 11163 - Jaguar King
import sys
from collections import deque
from queue import PriorityQueue

def generatePossibleKingMoves(data):
    jaguars, p, jumps, h = data[0], data[1], data[2], data[3]
    possible_moves = []
    if p % 4 == 1:
        if p + 1 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 1, jumps, h))
        if p + 3 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 3, jumps, h))
        if p + 4 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 4, jumps, h))
        if p - 4 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 4, jumps, h))
    elif p % 4 == 2:
        if p + 1 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 1, jumps, h))
        if p - 1 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 1, jumps, h))
        if p + 4 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 4, jumps, h))
        if p - 4 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 4, jumps, h))
    elif p % 3 == 4:
        if p + 1 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 1, jumps, h))
        if p - 1 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 1, jumps, h))
        if p + 4 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 4, jumps, h))
        if p - 4 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 4, jumps, h))
    else:  # p % 4 == 0
        if p - 3 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 3, jumps, h))
        if p - 1 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 1, jumps, h))
        if p + 4 <= len(jaguars):
            possible_moves.append(generateNewJaguarData(jaguars, p, p + 4, jumps, h))
        if p - 4 >= 1:
            possible_moves.append(generateNewJaguarData(jaguars, p, p - 4, jumps, h))
    return possible_moves

def generateNewJaguarData(jaguars, p1, p2, jumps, h):
    new_jaguars = jaguars.copy()
    # print(f'P1: {p1} | P2: {p2}')
    # print(p1, new_jaguars[p1 - 1])
    # print(p2, new_jaguars[p2 - 1])
    p1OldPosCorrect = p1 == new_jaguars[p1 - 1]
    p2OldPosCorrect = p2 == new_jaguars[p2 - 1]
    # print(f'NEW JAGUARS: {new_jaguars}')
    new_jaguars[p1 - 1], new_jaguars[p2 - 1] = new_jaguars[p2 - 1], new_jaguars[p1 - 1]
    # print(f'UPDATED NEW JAGUARS: {new_jaguars}')
    p1NewPosCorrect = p1 == new_jaguars[p1 - 1]
    p2NewPosCorrect = p2 == new_jaguars[p2 - 1]
    # print(p1, new_jaguars[p1 - 1])
    # print(p2, new_jaguars[p2 - 1])
    # print(f'POSITIONS | p1Old: {p1OldPosCorrect} | p1New: {p1NewPosCorrect} | p2Old: {p2OldPosCorrect} | p2New: {p2NewPosCorrect}')
    h = calculateSwappedJaguarsHeuristic(p1OldPosCorrect, p1NewPosCorrect, p2OldPosCorrect, p2NewPosCorrect, h)
    return (new_jaguars, p2, jumps + 1, h)

def correctFormation(jaguars):
    for i, j in enumerate(jaguars):
        if i + 1 != j:
            return False
    return True

def calculateSwappedJaguarsHeuristic(p1OldPosCorrect, p1NewPosCorrect, p2OldPosCorrect, p2NewPosCorrect, h):
    if p1OldPosCorrect != p1NewPosCorrect:
        if p1OldPosCorrect:
            h += 1
            # print(f'p1OldPosCorrect {h}')
        else:
            h -= 1
            # print(f'not p1OldPosCorrect {h}')
    if p2OldPosCorrect != p2NewPosCorrect:
        if p2OldPosCorrect:
            h += 1
            # print(f'p2OldPosCorrect {h}')
        else:
            h -= 1
            # print(f'not p2OldPosCorrect {h}')
    # print(f'newly calculated h: {h}')
    return h

def calculateInitialHeuristic(jaguars):
    h = 0
    for i, j in enumerate(jaguars):
        if i + 1 != j:
            h += 1
    return h

# NOTE: do everything by position, not index
set_number = 1
seen_jaguars = set()
while True:
    line = sys.stdin.readline().strip()
    if line == "0":
        break
    initial_jaguars = list(map(int, sys.stdin.readline().strip().split()))
    # print(initial_jaguars)
    initial_pos = initial_jaguars.index(1) + 1
    # NOTE: heuristic = number of jaguars out of position
    initial_heuristic = calculateInitialHeuristic(initial_jaguars)
    initial_data = (initial_jaguars, initial_pos, 0, initial_heuristic)
    q = deque()
    q.append(initial_data)
    seen_jaguars.add(str(initial_jaguars))
    # print(calculateInitialHeuristic(initial_jaguars))
    # print('INITIAL DATA:', initial_data)
    # print('PKM:', generatePossibleKingMoves(initial_data))
    while q:
        jaguar_data = q.popleft()
        # print(jaguar_data)
        # print(jaguar_data)
        # jaguars, curr_pos, jumps, heuristic = jaguar_data        
        if jaguar_data[3] == 0:
            # print(heuristic)
            print(f'Set {set_number}:\n{jaguar_data[2]}')
            break
        for pkm in generatePossibleKingMoves(jaguar_data):
            jaguars_str = str(pkm[0])
            print(f'JAGUAR DATA: {jaguar_data}')
            if jaguars_str not in seen_jaguars:
                print(f'JAGUAR STR: {jaguars_str}')
                seen_jaguars.add(jaguars_str)
            q.append(pkm)
    set_number += 1
        