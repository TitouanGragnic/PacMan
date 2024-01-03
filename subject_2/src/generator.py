import random
import heapq
import math

def generate_maze(width, height):
    # Créer une grille pleine avec tous les murs
    maze = [[{"nord": True, "sud": True, "est": True, "ouest": True} for j in range(width)] for i in range(height)]

    # Créer une liste d'arêtes
    edges = []
    sets = []
    for i in range(height):
        for j in range(width):
            sets.append(set([(i, j)]))
            if i > 0:
                edges.append(((i, j), (i-1, j)))
            if j > 0:
                edges.append(((i, j), (i, j-1)))

    # Mélanger la liste d'arêtes
    random.shuffle(edges)

    # Parcourir toutes les arêtes
    for edge in edges:
        # Extraire les deux cellules adjacentes
        cell1, cell2 = edge

        # Trouver les ensembles correspondants
        set1 = None
        set2 = None
        for i in range(len(sets)):
            if cell1 in sets[i]:
                set1 = i
            if cell2 in sets[i]:
                set2 = i

        # Si les cellules sont dans des ensembles différents, fusionner les ensembles
        if set1 != set2:
            sets[set1] = sets[set1].union(sets[set2])
            sets.pop(set2)

            # Retirer le mur entre les cellules
            if cell1[0] == cell2[0]:
                if cell1[1] > cell2[1]:
                    maze[cell1[0]][cell1[1]]["ouest"] = False
                    maze[cell1[0]][cell2[1]]["est"] = False
                else:
                    maze[cell1[0]][cell1[1]]["est"] = False
                    maze[cell1[0]][cell2[1]]["ouest"] = False
            else:
                if cell1[0] > cell2[0]:
                    maze[cell1[0]][cell1[1]]["nord"] = False
                    maze[cell2[0]][cell1[1]]["sud"] = False
                else:
                    maze[cell1[0]][cell1[1]]["sud"] = False
                    maze[cell2[0]][cell1[1]]["nord"] = False
    # Retourner le labyrinthe généré
    return maze

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
