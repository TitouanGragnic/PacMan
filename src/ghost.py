import pygame
import random
import heapq
import math

RED = (255, 0, 0)

class Ghost:
    def __init__(self, screen, maze, size):
        self.screen = screen
        self.speed = 200
        self.dt = 0
        self.size = size
        self.maze = maze
        self.path = []
        self.pos = [screen.get_width() / 2, screen.get_height() / 2]
        self.real_pos = (int(self.pos[0] / self.size), int(self.pos[1] / self.size))

    def move_up(self):
        i = int(self.pos[0] / self.size)
        j = int((self.pos[1] - self.speed * self.dt - self.size / 2) / self.size)

        #if not self.maze.maze[i][j]:
        self.pos[1] -= self.speed * self.dt

    def move_down(self):
        i = int(self.pos[0] / self.size)
        j = int((self.pos[1] + self.speed * self.dt + self.size / 2) / self.size)

        #if not self.maze.maze[i][j]:
        self.pos[1] += self.speed * self.dt

    def move_left(self):
        i = int((self.pos[0] - self.speed * self.dt - self.size / 2) / self.size)
        j = int(self.pos[1] / self.size)

        #if not self.maze.maze[i][j]:
        self.pos[0] -= self.speed * self.dt

    def move_right(self):
        i = int((self.pos[0] + self.speed * self.dt + self.size / 2) / self.size)
        j = int(self.pos[1] / self.size)

        #if not self.maze.maze[i][j]:
        self.pos[0] += self.speed * self.dt

    def print(self):
        pygame.draw.circle(self.screen, RED, (int(self.pos[0]), int(self.pos[1])), int(self.size * 0.45))

    def astar(self, maze, start, end):
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
                #path.reverse()
                return path

            # Génération des voisins
            visited.add(node)
            x, y = node
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)] :
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(maze) or ny >= len(maze[0]):
                    continue
                
                if maze[nx][ny] == 0:
                    g = costs[node] + 1
                    h = math.sqrt((nx - end[0]) ** 2 + (ny - end[1]) ** 2)
                    f = g + h
                    neighbor = (nx, ny)
                    if neighbor not in costs or g < costs[neighbor]:
                        costs[neighbor] = g
                        parents[neighbor] = node
                        heapq.heappush(heap, (f, neighbor))

        return []

    def find_pos(self):
        i = 0
        x = -1
        y = -1
        while (i == 0):
            x = random.randint(0, len(self.maze.maze)-1)
            y = random.randint(0, len(self.maze.maze[0])-1)
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)] :
                x += dx
                y += dy
                #print(x,y, self.maze.maze[x][y])
                if (self.maze.maze[x][y] == 0):
                    return(x, y)
        return (x, y)

    def action(self, dt):
        self.dt = dt
        self.print()

        while (len(self.path) < 2):
            self.path = self.astar(self.maze.maze, self.real_pos, self.find_pos())

        if (self.real_pos == self.path[-1]):
            self.path.pop()
        
        tmp = self.path[-1]
        
        #print(self.real_pos, path)
        if (tmp[0] > self.real_pos[0]):
            self.move_right()
        elif (tmp[0] < self.real_pos[0]):
            self.move_left()
        elif (tmp[1] > self.real_pos[1]):
            self.move_down()
        elif (tmp[1] < self.real_pos[1]):
            self.move_up()
        self.real_pos = (int(self.pos[0] / self.size), int(self.pos[1] / self.size))
