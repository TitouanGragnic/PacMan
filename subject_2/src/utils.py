import pygame

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_game_over(screen, height, size, life):
    font = pygame.font.SysFont('didot.ttc', 200)
    img  = font.render('Game Over', True, GREEN if life else RED )
    screen.blit(img, (10, (height + 1.5) * size))


def draw_score(screen, height, size, score):
    font = pygame.font.SysFont('didot.ttc', 50)
    img  = font.render('{:0>9}'.format(score), True, YELLOW)
    screen.blit(img, (10, (2 * height + 1.5) * size))

def draw_life(screen, height, width, size, life):
    for x in range(2 * width, 2 * width - life, -1):
        pygame.draw.circle(screen, GREEN,
                           (int(x * size), int((2 * height + 1.5) * size)),
                           int(size * 0.45))


def draw_data(screen, height, width, size, pacman):
    draw_score(screen, height, size, pacman.score)
    draw_life(screen, height, width, size, pacman.life)

def check_event(player, ghost):
    if player.power_up:
        player.score += 100
        ghost.kill()
    else :
        player.score -= 150
        player.kill()
    return player.life != 0

def check_hitbox(player, ghosts):
    # TODO
    return True
