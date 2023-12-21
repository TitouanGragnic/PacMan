import pygame
import random
import heapq
import math

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (100, 100, 100)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)

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

def dessiner_labyrinthe(grille, ecran, cellule_taille):
    """Dessine le labyrinthe sur l'écran."""
    hauteur = len(grille)
    largeur = len(grille[0])

    ecran.fill(BLANC)

    for i in range(hauteur):
        for j in range(largeur):
            cellule = grille[i][j]
            x = j * 2 * cellule_taille + cellule_taille
            y = i * 2 * cellule_taille + cellule_taille
            if cellule["nord"]:
                pygame.draw.rect(ecran, GRIS, pygame.Rect(x - cellule_taille, y - cellule_taille, 3 * cellule_taille, cellule_taille))
            if cellule["sud"]:
                pygame.draw.rect(ecran, GRIS, pygame.Rect(x - cellule_taille, y + cellule_taille, 3 * cellule_taille, cellule_taille))
            if cellule["est"]:
                pygame.draw.rect(ecran, GRIS, pygame.Rect(x + cellule_taille, y - cellule_taille, cellule_taille, 3 * cellule_taille))
            if cellule["ouest"]:
                pygame.draw.rect(ecran, GRIS, pygame.Rect(x - cellule_taille, y - cellule_taille, cellule_taille, 3 * cellule_taille))

    pygame.draw.rect(ecran, BLANC, pygame.Rect(0, cellule_taille, cellule_taille, cellule_taille))
    pygame.draw.rect(ecran, BLANC, pygame.Rect(2 * largeur * cellule_taille, (2 * hauteur - 1) * cellule_taille, cellule_taille, cellule_taille))
    pygame.draw.rect(ecran, BLANC, pygame.Rect(((2 * largeur) // 3 - 3) * cellule_taille, ((2 * hauteur) // 3 - 2) * cellule_taille, cellule_taille * largeur, cellule_taille * hauteur))


    pygame.display.flip()

def main() :

    # Initialiser Pygame.
    pygame.init()

    # Définir les dimensions de l'écran et la taille de chaque cellule.
    largeur = 15
    hauteur = 25
    cellule_taille = 20
    dimensions = (2 * hauteur * cellule_taille + cellule_taille, 2 * largeur * cellule_taille + cellule_taille)
    ecran = pygame.display.set_mode(dimensions)

    # Générer le labyrinthe et le dessiner sur l'écran.
    grille = generate_maze(hauteur, largeur)
    dessiner_labyrinthe(grille, ecran, cellule_taille)

    # Boucle principale du programme.
    while True:
        # Attendre un événement de Pygame.
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                # Si l'utilisateur ferme la fenêtre, quitter le programme.
                pygame.quit()
                return
main()
