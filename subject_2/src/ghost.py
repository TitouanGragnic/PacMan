import pygame
import random
import heapq
import math

RED = (255, 0, 0)

class Ghost:
    def __init__(self, screen, maze, size):
        self.screen = screen
        self.speed = 200
        self.dt = 0
        self.size = size
        self.maze = maze
        self.path = []
        self.pos = [screen.get_width() / 2, screen.get_height() / 2]
        self.real_pos = (int(self.pos[0] / self.size), int(self.pos[1] / self.size))

    def move_up(self):
        # TODO
        pass

    def move_down(self):
        # TODO
        pass

    def move_left(self):
        # TODO
        pass

    def move_right(self):
        # TODO
        pass

    def kill(self):
        # TODO
        pass

    def print(self):
        pygame.draw.circle(self.screen, RED, (int(self.pos[0]), int(self.pos[1])), int(self.size * 0.45))

    def action(self, dt):
        self.dt = dt
        self.print()
        # TODO
