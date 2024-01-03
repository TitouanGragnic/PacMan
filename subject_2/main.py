# Example file showing a circle moving on screen
import pygame
from src.pacman import *
from src.maze import *
from src.utils import *
from src.ghost import *

size = 30
width = 25
height = 15

BLACK = (0, 0, 0)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(((2 * width + 1) * size, (2 * height + 1) * size + 50))
clock = pygame.time.Clock()
running = True
dt = 0

#PacMan Setup

maze = Maze(screen, width, height, size)
pacman = PacMan(screen, maze, size)
ghosts = [] # TODO

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)
    maze.print()
    pacman.action(dt)
    draw_data(screen, height, width, size, pacman)

    for gh in ghosts:
        gh.action(dt)
    if (running):
        running = check_hitbox(pacman, ghosts)
    if (running):
        running = maze.check_end()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

draw_game_over(screen, height, size, pacman.life)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
