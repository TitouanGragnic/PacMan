import pygame

RED = (255, 0, 0)

class Ghost:
    def __init__(self, screen, maze, size):
        self.screen = screen
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.speed = 200
        self.dt = 0
        self.size = size
        self.maze = maze

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
        pygame.draw.circle(self.screen, RED, (int(self.pos.x), int(self.pos.y)), int(self.size * 0.45))

    def action(self, dt):
        self.dt = dt
        self.print()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_s]  or keys[pygame.K_DOWN]:
            self.move_down()
        if keys[pygame.K_a]  or keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_d]  or keys[pygame.K_RIGHT]:
            self.move_right()
