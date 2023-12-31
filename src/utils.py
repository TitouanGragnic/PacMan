import pygame

def draw_score(screen, height, size, score):
    font = pygame.font.SysFont('didot.ttc', 50)
    img  = font.render('{:0>9}'.format(score), True, 'yellow')
    screen.blit(img, (10, (2 * height + 1.5) * size))