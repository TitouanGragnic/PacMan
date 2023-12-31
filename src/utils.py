import pygame

YELLOW = (255, 255, 0)

def draw_score(screen, height, size, score):
    font = pygame.font.SysFont('didot.ttc', 50)
    img  = font.render('{:0>9}'.format(score), True, YELLOW)
    screen.blit(img, (10, (2 * height + 1.5) * size))

def kill_ghost(gh):
    gh.pos = [gh.screen.get_width() / 2, gh.screen.get_height() / 2]
    gh.real_pos = (int(gh.pos[0] / gh.size), int(gh.pos[1] / gh.size))
    gh.path = []
    return True
def kill_player(pc):
    pc.life -= 1
    pc.pos = pygame.Vector2(pc.screen.get_width() / 2, pc.screen.get_height() / 2)
    if (pc.life == 0):
        return False
    return True

def check_event(player, ghost):
    if (player.power_up == True):
        return kill_ghost(ghost)
    else :
        return kill_player(player)

def check_hitbox(player, ghosts):
    player_pos = (int(player.pos.x / player.size), int(player.pos.y /player.size))
    for elt in ghosts:
        if (elt.real_pos == player_pos):
            return check_event(player, elt)
    return True
            