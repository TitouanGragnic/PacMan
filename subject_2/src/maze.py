import pygame

from src.generator import *

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DB = (0, 0, 138)


class Maze:
    def __init__(self, screen, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.maze, self.point = transpose_maze(generate_maze(width, height))
        self.screen = screen

    def check_end(self):
        # TODO
        return True

    def print(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j]:
                    pygame.draw.rect(self.screen, DB,
                                     pygame.Rect( i * self.size, j * self.size,
                                                  self.size, self.size))
                if self.point[i][j] == 1:
                    pygame.draw.circle(self.screen, WHITE, (int((i + 0.5) * self.size), int((j + 0.5) * self.size)), int(self.size / 4))
                if self.point[i][j] == 2:
                    pygame.draw.circle(self.screen, GREEN, (int((i + 0.5) * self.size), int((j + 0.5) * self.size)), int(self.size / 4))
