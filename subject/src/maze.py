import pygame
import random
import heapq
import math

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DB = (0, 0, 138)

def generate_maze(width, height):
    #TODO
    # Créer une grille pleine avec tous les murs
    ########## Part 1 ##########

    # Créer une liste d'arêtes
    ########## Part 2 ##########

    # Mélanger la liste d'arêtes
    #random.shuffle(list_of_edge)

    # Parcourir toutes les arêtes
    # Extraire les deux cellules adjacentes
    # Trouver les ensembles correspondants
    # Si les cellules sont dans des ensembles différents, fusionner les ensembles
    # Retirer le mur entre les cellules
    ########## Part 3 ##########

    # Retourner le labyrinthe généré
    return [[]]

def transpose_maze(maze):
    res = [[0 for _ in range(len(maze) * 2 + 1)] for _ in range(len(maze[0]) * 2 + 1)]

    for i in range(len(maze)):
            for j in range(len(maze[0])):
                cell = maze[i][j]
                x = j * 2 + 1
                y = i * 2 + 1
                if cell["nord"]:
                    res[x - 1][y - 1] = 1
                    res[x + 1][y - 1] = 1
                    res[x][y - 1] = 1
                if cell["sud"]:
                    res[x - 1][y + 1] = 1
                    res[x + 1][y + 1] = 1
                    res[x][y + 1] = 1
                if cell["est"]:
                    res[x + 1][y + 1] = 1
                    res[x + 1][y - 1] = 1
                    res[x + 1][y] = 1
                if cell["ouest"]:
                    res[x - 1][y + 1] = 1
                    res[x - 1][y - 1] = 1
                    res[x - 1][y] = 1

    tmp = [[ not k for k in line] for line in res]

    for i in range(int(len(res)/6 * 2), int(len(res)/6 * 4)):
        for j in range(int(len(res[0])/6 * 2), int(len(res[0])/6 * 4)):
            res[i][j] = 0
            tmp[i][j] = 1 if j in [int(len(res[0])/6 * 2), int(len(res[0])/6 * 4) - 1] or i in [int(len(res)/6 * 2), int(len(res)/6 * 4) -1] else 0
    #TODO
    #peux etre ajouter une supression de case random pour ouvrir un peut  plus le labirinte?

    for i in range(int(len(res)/3)+1, int(len(res)/3 * 2)-2):
        res[i][int(len(res[0])/3) + 1] = 1
        res[i][int(len(res[0])/3 * 2) - 2] = 1

    for j in range(int(len(res[0])/6 * 2 + 1), int(len(res[0])/6 * 4 - 1)):
            res[int(len(res)/3)+ 1][j] = 1
            res[int(len(res)/3*2)-2][j] = 1

    i = int(len(res)/6)
    j = int(len(res[0])/6)
    
    res[int(len(res)/2)][int(len(res[0])/3) + 1] = 0

    res[i][j] = 0
    tmp[i][j] = 2

    res[i][j*5] = 0
    tmp[i][j*5] = 2

    res[i*5][j] = 0
    tmp[i*5][j] = 2

    res[i*5][j*5] = 0
    tmp[i*5][j*5] = 2

    return res, tmp

class Maze:
    def __init__(self, screen, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.maze, self.point = transpose_maze(generate_maze(width, height))
        self.screen = screen
        
    def check_end(self):
        #Return if it's possible to get more point
        #TODO
        return False

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
