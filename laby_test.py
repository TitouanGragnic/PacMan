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

def astar(maze, start, end):
    # Initialisation
    heap = []
    visited = set()
    parents = {}
    costs = {start: 0}
    heapq.heappush(heap, (0, start))
    
        # Boucle principale
    while heap:
        # Sélection du nœud ayant le score F le plus faible
        f, node = heapq.heappop(heap)
        if node in visited:
            continue
        # Vérification de l'arrivée
        if node == end:
            path = []
            while node in parents:
                path.append(node)
                node = parents[node]
            path.append(start)
            path.reverse()
            return path

        # Génération des voisins
        visited.add(node)
        x, y = node
        for dx, dy, direction in [(0, -1, "ouest"), (0, 1, "est"), (-1, 0, "nord"), (1, 0, "sud")] :
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(maze) or ny >= len(maze[0]):
                continue
            if not(maze[x][y][direction]):
                g = costs[node] + 1
                h = math.sqrt((nx - end[0]) ** 2 + (ny - end[1]) ** 2)
                f = g + h
                neighbor = (nx, ny)
                if neighbor not in costs or g < costs[neighbor]:
                    costs[neighbor] = g
                    parents[neighbor] = node
                    heapq.heappush(heap, (f, neighbor))

    return None

    

def dessiner_labyrinthe(grille, ecran, cellule_taille, path):
    """Dessine le labyrinthe sur l'écran."""
    hauteur = len(grille)
    largeur = len(grille[0])
    
    ecran.fill(BLANC)

    for i in range(hauteur):
        for j in range(largeur):
            cellule = grille[i][j]
            x = j * cellule_taille+5
            y = i * cellule_taille+5
            if cellule["nord"]:
                pygame.draw.line(ecran, NOIR, (x, y), (x + cellule_taille, y), 1)
            if cellule["sud"]:
                pygame.draw.line(ecran, NOIR, (x, y + cellule_taille), (x + cellule_taille, y + cellule_taille), 1)
            if cellule["est"]:
                pygame.draw.line(ecran, NOIR, (x + cellule_taille, y), (x + cellule_taille, y + cellule_taille), 1)
            if cellule["ouest"]:
                pygame.draw.line(ecran, NOIR, (x, y), (x, y + cellule_taille), 1)
    
    if path:
        for c in path :
            x = c[1] * cellule_taille +5
            y = c[0] * cellule_taille +5
            pygame.draw.line(ecran, ROUGE, (x, y), (x + cellule_taille, y + cellule_taille), 1)
            pygame.draw.line(ecran, ROUGE, (x+ cellule_taille, y), (x , y + cellule_taille), 1)

    pygame.display.flip()
def main() :
    
    # Initialiser Pygame.
    pygame.init()
    
    # Définir les dimensions de l'écran et la taille de chaque cellule.
    largeur = 20
    hauteur = 20
    cellule_taille = 30
    dimensions = (hauteur * cellule_taille+10, largeur * cellule_taille+10)
    ecran = pygame.display.set_mode(dimensions)

    # Générer le labyrinthe et le dessiner sur l'écran.
    grille = generate_maze(hauteur, largeur)
    path = astar(grille, (0,0), (largeur-1,hauteur-1))
    dessiner_labyrinthe(grille, ecran, cellule_taille, path)

    # Boucle principale du programme.
    while True:
        # Attendre un événement de Pygame.
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                # Si l'utilisateur ferme la fenêtre, quitter le programme.
                pygame.quit()
                return
main()