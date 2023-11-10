# Example file showing a circle moving on screen
import pygame
from src.pacman import *
from src.maze import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#PacMan Setup


size = 20
width = int(screen.get_width() / size)
height = int(screen.get_height() / size)

maze = Maze(screen, width, height, size)
pacman = PacMan(screen, maze, size)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark blue")

    maze.print()
    pacman.action(dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
