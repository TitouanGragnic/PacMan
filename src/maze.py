import pygame

def generate_maze(width, height):
    T= [[ 0 for _ in range(height)] for _ in range(width)]
    for i in range(width):
        T[i][0] = 1
        T[i][-1] = 1
    for i in range(height):
        T[0][i] = 1
        T[-1][i] = 1

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
