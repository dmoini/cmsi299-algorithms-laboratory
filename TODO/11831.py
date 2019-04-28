# 11831 - Sticker Collector Robot
import sys

# Directions
# D ==> turn right 90 degrees
# E ==> turn left 90 degrees
# F ==> move forward one cell

# Compass:
# N ==> N
# L ==> E
# S ==> S
# O ==> W

COLUMN = '#'
STICKER = '*'
NORMAL = '.'

class Robot():
    def __init__(self, r, c, direction, arena):
        self.r = r
        self.c = c
        self.direction = direction
        self.stickers = 0
        
        self.compass = ['N', 'L', 'S', 'O']
        self.c_num = self.compass.index(direction)

        self.arena = arena
        self.arena_height = len(arena)
        self.arena_width = len(arena[0])

    def __str__(self):
        return f'r: {self.r} || c: {self.c} || direction: {self.direction} || stickers: {self.stickers} || c_num: {self.c_num}'

    def facing_boundary(self):
        return ((self.direction == 'N' and self.r == 0) or (self.direction == 'L' and self.c == M - 1) 
            or (self.direction == 'S' and self.r == N - 1) or (self.direction == 'O' and self.c == 0))

    def facing_pole(self):
        if self.direction == 'N':
            return self.arena[self.r - 1][self.c] == COLUMN
        elif self.direction == 'L':
            return self.arena[self.r][self.c + 1] == COLUMN
        elif self.direction == 'S':
            return self.arena[self.r + 1][self.c] == COLUMN
        else:
            return self.arena[self.r][self.c - 1] == COLUMN

    def can_move(self):
        return not (self.facing_pole() or self.facing_boundary())

    def move_forward(self):
        if self.direction == 'N':
            self.c -= 1
        elif self.direction == 'L':
            self.r += 1
        elif self.direction == 'S':
            self.c += 1
        else:
            self.r -= 1

    def on_sticker(self):
        return self.arena[self.r][self.c] == STICKER
            
    def pick_up_sticker(self):
        self.arena[self.r][self.c] = NORMAL
        self.stickers += 1

    def rotate(self, rotation):
        if rotation == 'D':
            self.c_num = self.c_num + 1 if self.c_num < 3 else 0
            self.direction = self.compass[self.c_num]
        else:
            self.c_num = self.c_num - 1 if self.c_num > 0 else 3
            self.direction = self.compass[self.c_num]

while True:
    N, M, S = map(int, sys.stdin.readline().strip().split())
    if N == M == S == 0:
        break
    arena = []
    found_starting_position = False
    start_row, start_col, start_direc = None, None, None
    for i in range(N):
        row = sys.stdin.readline().strip()
        if not found_starting_position:
            if 'N' in row:
                start_row, start_col, start_direc = i, row.find('N'), 'N'
                found_starting_position = True
            elif 'L' in row:
                start_row, start_col, start_direc = i, row.find('L'), 'L'
                found_starting_position = True
            elif 'S' in row:
                start_row, start_col, start_direc = i, row.find('S'), 'S'
                found_starting_position = True
            elif 'O' in row:
                start_row, start_col, start_direc = i, row.find('O'), 'O'
                found_starting_position = True
        arena.append(row)
    instructions = sys.stdin.readline().strip()
    print(N, M, arena, instructions, start_row, start_col, start_direc)
    robot = Robot(start_row, start_col, start_direc, arena)
    # print(robot)
    # print()
    print(instructions)
    print(f'ROBOT: {robot}')
    for i in instructions:
        if i in 'DE':
            robot.rotate(i)
        elif robot.can_move():
            robot.move_forward()
            if robot.on_sticker():
                robot.pick_up_sticker()
        print(f'{i} *** ROBOT: {robot}')
    print(robot.stickers)
    print("=======================")