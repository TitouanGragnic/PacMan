# PacMan

Durant ce TP vou allez apprendre a :
  - manipuler les lists
 - les base de la programation orienter objet
 - creer une IA

Vous aller etre ammener a utilisser la lybrary python **pygame** pour ceci il vous faut travailler sur un shell ou la commande suivante a ete executer :

```sh
nix-shell -p python311Packages.pygame
```

## Partie 1: src/pacman.py

### le mouvement

ici nous vous proposont de diviser les diferent mouvemtn en sous fonction pour la lisibilieter du code (vous pouver rajouter autant de sous fonction que vous desirer pour alaiger le code)

pour adapter le mouvement a la frequnece d'image et que la puissance du pc ne modifie pas la rapiditer du jeu nous utilisons une variable dt qui est un delta du temps permetant d'harmoniser la vitesse avec le temps.

pour utiliser ce dt il suffit de multiplier la variable ajouter a votre position par dt comme ceci:
```py
self.pos.x += self.speed * self.dt
```

**Il est important de verifier si la case suivante est un mur ou non avant d'avancer!**

### PacMan.kill()
cette fonction est appeler quand le pacman est tue et doit reduire la vie de 1, reinitialiser la position a celle de depart

### PacMan.eat()
Cette fonction permet de mager les petit points blanc afin de ganger des points, il faut donc verifier si l'on peut manger le point et ensuite ajouter les points.
s'il sagit d'un point special il faut mettre le Pacman en mode Power *True*

### PacMan.Power()
Cet Fonction doit permettre a PacMan de garder son powerup durant environ dix secondes. Pour ce faire vous pouvez utiliser la librairie time de python et de la fonction timer de cette librairie.

## Partie 2: src/maze.py src/utils.py

### src/maze.py
Ici rien de tres compliquer la generation du labyrinte est donner, il manque la methode **Maze.check_end** qui renvoie *False* si il n'y a plus de point a recuperer dans le labyrinte *True* sinon.

### src/utils.py
ce fichier permet d'avoir 2-3 fonction utils au programe qui ne necicite pas de fichier a part entiere

#### check_hitbox(player, gh)
test si le pacman est en colision avec un des fantome et appele check_event pour resoudre la colision et tuer l'un des deux
de plus la fonction renvoi *False* si la partie est fini, *True* sinon

## Partie 3: ghost.py

### le mouvement
de meme qu'avec pacman implementer les diferent methode de deplacement

### Ghost.action()
implementer une IA basic ou plus evoluer pour que le fantome choisise sont prochain deplacment
pour essayer votre code vous pouver ajouter un deplacement aleatoir et ensuite chercher un deplacemnt plus fluide et inteligent
