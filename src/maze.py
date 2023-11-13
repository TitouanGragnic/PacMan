import pygame
import random

def count_cels(x, y, T):
    res = 0
    if T[x-1][y] == 0:
        res += 1
    if T[x+1][y] == 0:
        res += 1
    if T[x][y-1] == 0:
        res += 1
    if T[x][y+1] == 0:
        res == 1
    return res

def make_walls(T, h, w):
    for i in range (w):
        for j in range(h):
            if (T[i][j] == -1):
                T[i][j] = 1
    return T

def generate_maze(width, height):
    T= [[ -1 for _ in range(height)] for _ in range(width)]
    T[2][2] = 0
    walls = []
    walls.append((1, 2))
    walls.append((2, 1))
    walls.append((2, 3))
    walls.append((3,2))
    T[1][2] = 1
    T[2][1] = 1
    T[2][3] = 1
    T[3][2] = 1
    while walls:
        print(walls)
        x,y = walls[int(random.random() * len(walls))-1]
        if y != 0 and y != len(T[0]) - 1:
            if T[x][y-1] == -1 and T[x][y+1] == 0:
                tst = count_cels(x,y,T)
                if tst < 2:
                    T[x][y] = 0
                    if x != 0:
                        if T[x-1][y] != 0:
                            T[x-1][y] = 1
                        if T[x-1][y] not in walls:
                            walls.append((x-1, y))
                walls.remove((x,y))
            continue
        if y != 0 and y != len(T[0]) - 1:
            if T[x][y+1] == -1 and T[x][y-1] == 0:
                tst = count_cels(x,y,T)
                if tst < 2:
                    T[x][y] = 0
                    if x != 0:
                        if T[x-1][y] != 0:
                            T[x-1][y] = 1
                        if T[x-1][y] not in walls:
                            walls.append((x-1, y))
                walls.remove((x,y))
            continue
        if x != 0 and x != len(T) - 1:
            if T[x+1][y] == -1 and T[x-1][y] == 0:
                tst = count_cels(x,y,T)
                if tst < 2:
                    T[x][y] = 0
                    if y != 0:
                        if T[x][y-1] != 0:
                            T[x][y-1] = 1
                        if T[x][y-1] not in walls:
                            walls.append((x, y-1))
                walls.remove((x,y))
            continue
        if x != 0 and x != len(T) - 1:
            if T[x-1][y] == -1 and T[x+1][y] == 0:
                tst = count_cels(x,y,T)
                if tst < 2:
                    T[x][y] = 0
                    if y != 0:
                        if T[x][y-1] != 0:
                            T[x][y-1] = 1
                        if T[x][y-1] not in walls:
                            walls.append((x, y-1))
                walls.remove((x,y))
            continue
        walls.remove((x,y))
    T = make_walls(T, height, width)
    return T

class Maze:
    def __init__(self, screen, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.maze = generate_maze(width, height)
        self.screen = screen

    def print(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.maze[i][j]:
                    wall = pygame.Rect(i * self.size, j * self. size, self.size, self.size)
                    pygame.draw.rect(self.screen, "grey", wall)
