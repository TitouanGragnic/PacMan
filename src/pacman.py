import pygame
import time

YELLOW = (255, 255, 0)

class PacMan:
    def __init__(self, screen, maze, size):
        self.screen = screen
        self.size = size
        self.maze = maze
        self.speed = 300
        self.life = 3
        self.dt = 0
        self.pos = self.start_pos()
        self.score = 0
        #fruit pour manger fantôme
        self.power_up = False
        self.timer = 0

    def start_pos(self):
        self.pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        i = int(self.pos.x / self.size)
        j = int((self.pos.y - self.speed * self.dt - self.size / 2) / self.size)
        while (not self.maze.maze[i][j]):
            i = int(self.pos.x / self.size)
            j = int((self.pos.y + self.speed * self.dt + self.size / 2) / self.size)
            self.pos.y += self.size
        while (self.maze.maze[i][j]):
            i = int(self.pos.x / self.size)
            j = int((self.pos.y + self.speed * self.dt + self.size / 2) / self.size)
            self.pos.y += self.size
        self.pos.y -= self.size
        return self.pos

    def move_up(self):
        i = int(self.pos.x / self.size)
        j = int((self.pos.y - self.speed * self.dt - self.size / 2) / self.size)

        if not self.maze.maze[i][j]:
            self.pos.y -= self.speed * self.dt

    def move_down(self):
        i = int(self.pos.x / self.size)
        j = int((self.pos.y + self.speed * self.dt + self.size / 2) / self.size)

        if not self.maze.maze[i][j]:
            self.pos.y += self.speed * self.dt

    def move_left(self):
        i = int((self.pos.x - self.speed * self.dt - self.size / 2) / self.size)
        j = int(self.pos.y / self.size)

        if not self.maze.maze[i][j]:
            self.pos.x -= self.speed * self.dt

    def move_right(self):
        i = int((self.pos.x + self.speed * self.dt + self.size / 2) / self.size)
        j = int(self.pos.y / self.size)

        if not self.maze.maze[i][j]:
            self.pos.x += self.speed * self.dt

    def print(self):
        pygame.draw.circle(self.screen, YELLOW, (int(self.pos.x), int(self.pos.y)), int(self.size * 0.45))

    def eat(self):
        i = int(self.pos.x / self.size)
        j = int(self.pos.y / self.size)

        if self.maze.point[i][j] == 2:
            self.power_up = True
            self.maze.point[i][j] = 0
            self.score += 50
        if self.maze.point[i][j]:
            self.maze.point[i][j] = 0
            self.score += 15

    def power(self):
        if (self.power_up and self.timer == 0):
            self.timer = time.time()
            return;
        if (self.timer - time.time() <= -10 and self.timer - time.time() >= -11):
            self.power_up = False
            self.timer = 0

    def action(self, dt):
        self.dt = dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_s]  or keys[pygame.K_DOWN]:
            self.move_down()
        if keys[pygame.K_a]  or keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_d]  or keys[pygame.K_RIGHT]:
            self.move_right()
        self.eat()
        self.print()
        self.power()
