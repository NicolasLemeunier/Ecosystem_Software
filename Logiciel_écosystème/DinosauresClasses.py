import pygame

import const

import random

#---------------Dinosaures---------------

class Dinosaures(pygame.sprite.Sprite):


    def __init__(self, life, pregnant, xPos, yPos, grid, espece, sexe):

        self.life = life

        self.pregnant = pregnant


        pygame.sprite.Sprite.__init__(self)
        # Definition d'un pseudo-pixel de 15 * 15 pxl
        self.image = pygame.Surface([const.SPRITE,const.SPRITE])
        # Variable d'emplacement du sprite dans chaques cases
        self.case_x = xPos
        self.case_y = yPos

        self.pre_x = xPos
        self.pre_y = yPos

        # Variable de position du sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.case_x * const.SPRITE
        self.rect.y = self.case_y * const.SPRITE


        self.grid = grid
        self.dimX = 27
        self.dimY = 27

        # Ces valeurs sont temporaire
        self.espece = espece
        self.sexe = sexe
        self.valeur = ''
        self.valeurOppose = ''
        self.reWrite()
        


    def changeCouleur(self, couleur):
        self.image.fill(couleur)


    def attributionEspece(self):

        couleur = 0

        if self.espece == "Triceratops":

            if self.sexe == 'Male':
                self.valeur = 'a'
                self.valeurOppose = 'b'
                couleur = const.DARKBLUE

            elif self.sexe == "Femelle":
                self.valeur = 'b'
                self.valeurOppose = 'a'
                couleur = const.BLUE

        elif self.espece == "Stegosauridae":

            if self.sexe == 'Male':
                self.valeur = 'c'
                self.valeurOppose = 'd'
                couleur = const.DARKCYAN

            elif self.sexe == 'Femelle':
                self.valeur = 'd'
                self.valeurOppose = 'c'
                couleur = const.CYAN

        elif self.espece == "Tyrannosaure":

            if self.sexe == 'Male':
                self.valeur = 'e'
                self.valeurOppose = 'f'
                couleur = const.DARKRED

            elif self.sexe == 'Femelle':
                self.valeur = 'f'
                self.valeurOppose = 'e'
                couleur = const.RED

        elif self.espece == "Allosaurus":

            if self.sexe == 'Male':
                self.valeur = 'g'
                self.valeurOppose = 'h'
                couleur = const.DARKPURPLE

            elif self.sexe == 'Femelle':
                self.valeur = 'h'
                self.valeurOppose = 'g'
                couleur = const.PURPLE


        self.changeCouleur(couleur)
        

    # Fonction de déplacement sur l'écran
    # A noter que le déplacement sera dirigé par une IA

    def seDeplace(self, direction):
        # Si il se dirige vers le bas
        if direction == "S":
            if self.case_y < (self.dimY-1):
                #if self.grid.grid[self.case_y+1][self.case_x] != '1' and self.grid.grid[self.case_y+1][self.case_x] != '2':
                if self.grid.grid[self.case_y+1][self.case_x] == '0':
                    self.pre_y = self.case_y
                    self.pre_x = self.case_x
                    self.case_y += 1
                    self.rect.y = self.case_y * const.SPRITE
        # Si il se dirige vers le haut
        elif direction == "N":
            if self.case_y > 0:
                #if self.grid.grid[self.case_y-1][self.case_x] != '1' and self.grid.grid[self.case_y-1][self.case_x] != '2':
                if self.grid.grid[self.case_y-1][self.case_x] == '0':
                    self.pre_y = self.case_y
                    self.pre_x = self.case_x
                    self.case_y -= 1
                    self.rect.y = self.case_y * const.SPRITE
        # Si il se dirige vers la droite
        elif direction == "O":
            if self.case_x > 0:
                #if self.grid.grid[self.case_y][self.case_x-1] != '1' and self.grid.grid[self.case_y][self.case_x-1] != '2':
                if self.grid.grid[self.case_y][self.case_x-1] == '0':
                    self.pre_x = self.case_x
                    self.pre_y = self.case_y
                    self.case_x -= 1
                    self.rect.x = self.case_x * const.SPRITE
        # Si il se dirige vers la gauche
        elif direction == "E":
            if self.case_x < (self.dimX-1):
                #if self.grid.grid[self.case_y][self.case_x+1] != '1' and self.grid.grid[self.case_y][self.case_x+1] != '2' :
                if self.grid.grid[self.case_y][self.case_x+1] == '0':
                    self.pre_x = self.case_x
                    self.pre_y = self.case_y
                    self.case_x += 1
                    self.rect.x = self.case_x * const.SPRITE
        self.reWrite()

    def reWrite(self):
        self.grid.grid[self.pre_y][self.pre_x] = '0'
        self.grid.grid[self.case_y][self.case_x] = self.valeur
        


    def mesCoordonnees(self):
        coor = []
        coor.append(self.case_x)
        coor.append(self.case_y)
        return coor

    # cette fonction detecte si il y a quelq'un à coté de lui
    # cette valeur doit être différente de 0 ou 1
    def intervalleGrid(self):

        self.lieux = []

        # HAUT
        # XOO
        if self.grid.grid[self.case_y-1][self.case_x-1] != '0' and self.grid.grid[self.case_y-1][self.case_x-1] != '1':
            self.lieux.append(self.grid.grid[self.case_y-1][self.case_x-1])
        # OXO
        if self.grid.grid[self.case_y-1][self.case_x] != '0' and self.grid.grid[self.case_y-1][self.case_x] != '1':
            self.lieux.append(self.grid.grid[self.case_y-1][self.case_x])
        #OOX
        if self.grid.grid[self.case_y-1][self.case_x+1] != '0' and self.grid.grid[self.case_y-1][self.case_x+1] != '1':
            self.lieux.append(self.grid.grid[self.case_y-1][self.case_x+1])

        # MILIEU
        # OOX
        if self.grid.grid[self.case_y][self.case_x+1] != '0' and self.grid.grid[self.case_y][self.case_x+1] != '1':
            self.lieux.append(self.grid.grid[self.case_y][self.case_x+1])
        # XOO
        if self.grid.grid[self.case_y][self.case_x-1] != '0' and self.grid.grid[self.case_y][self.case_x-1] != '1':
            self.lieux.append(self.grid.grid[self.case_y][self.case_x-1])

        # BAS
        # XOO
        if self.grid.grid[self.case_y+1][self.case_x-1] != '0' and self.grid.grid[self.case_y+1][self.case_x-1] != '1':
            self.lieux.append(self.grid.grid[self.case_y+1][self.case_x-1])
        # OXO
        if self.grid.grid[self.case_y+1][self.case_x] != '0' and self.grid.grid[self.case_y+1][self.case_x] != '1':
            self.lieux.append(self.grid.grid[self.case_y+1][self.case_x])
        # OOX
        if self.grid.grid[self.case_y+1][self.case_x+1] != '0' and self.grid.grid[self.case_y+1][self.case_x+1] != '1':
            self.lieux.append(self.grid.grid[self.case_y+1][self.case_x+1])

        return self.lieux
        

    #-------------------------------------------

    def reproduction(self, life):
        self.life = -10
        self.pregnant = True



class Terrain:
    # Constructeur du Terrain
    def __init__(self,fichier):
        #Creation de variable pour la grille terrain
        #ancienne version :self.grid = []
        self.grid = 0
        self.fichier = fichier


    def generate(self):
        with open(self.fichier, "r") as fichier:
            struct_niv = []
            for ligne in fichier:
                ligne_niveau = []
                for colonne in ligne:
                    if colonne != '\n':
                        ligne_niveau.append(colonne)
                struct_niv.append(ligne_niveau)
            self.grid = struct_niv

    def displayGrid(self, screen):

        nbLigne = 0
        for ligne in self.grid:
            nbColonne = 0
            for colonne in ligne:

                if colonne == '0':
                    color = const.WHITE
                    pygame.draw.rect(screen,color,[const.SPRITE*nbColonne, const.SPRITE*nbLigne,const.SPRITE,const.SPRITE])
                elif colonne == '1':
                    color = const.BLACK
                    pygame.draw.rect(screen,color,[const.SPRITE*nbColonne, const.SPRITE*nbLigne,const.SPRITE,const.SPRITE])
                nbColonne += 1
            nbLigne += 1
            


    # Cette fonction retourne vrai ou faux si une case avec des coordonnées donnée est libre ou non
    def caseEstLibre(self, x , y):
        return self.grid[y][x] == '0'






#---------------HERBIVORES---------------

class Herbivore(Dinosaures):

    def __init__(self, life, pregnant, xPos, yPos, grid, espece, sexe):


        Dinosaures.__init__(self, life, pregnant, xPos, yPos, grid, espece, sexe)

        self.my_sprite = pygame.sprite.Group()


    def Eat(self):
        """

        self.life = self.life + 10

        if self.life > 100:

            self.life = 100

        if self.life < 0:

            self.life = 0
        """
        pass

#---------------Triceratops---------------

class Triceratops(Herbivore):

    def __init__(self, life, pregnant, xPos, yPos, grid, espece, sexe):

        Herbivore.__init__(self, life, pregnant, xPos, yPos, grid, espece, sexe)



#---------------Stegosauridae---------------

class Stegosauridae(Herbivore):

    def __init__(self, life, pregnant, xPos, yPos, grid, espece, sexe):

        Herbivore.__init__(self, life, pregnant, xPos, yPos, grid, espece, sexe)

   
#---------------CARNIVORES---------------

class Carnivore(Dinosaures):

    def __init__(self, life, pregnant, xPos, yPos, grid, espece, sexe):


        Dinosaures.__init__(self, life, pregnant, xPos, yPos, grid, espece, sexe)

        self.my_sprite = pygame.sprite.Group()


    """
    def Eat(self):

        self.lieux = self.intervalleGrid()

        self.cible = random.choice(self.lieux)


        if cible == a:
            listeTriceratopsMa[listeTriceratops.index(cible)]
            cible.remove() #On supprime l'objet
        del listeTriceratops[listeTriceratops.index(cible)] #On supprime l'objet de la liste d'objets
    """
#---------------Tyrannosaure---------------

class Tyrannosaure(Carnivore):

    def __init__(self, life, pregnant, xPos, yPos, grid, espece, sexe):

        Carnivore.__init__(self, life, pregnant, xPos, yPos, grid, espece, sexe)

  

#---------------Allosaurus---------------

class Allosaurus(Carnivore):

    def __init__(self, life, pregnant, xPos, yPos, grid, espece, sexe):


        Carnivore.__init__(self, life, pregnant, xPos, yPos, grid, espece, sexe)





class Plant(pygame.sprite.Sprite):
    #Definition du Constructeur
    def __init__(self, xPos, yPos,grid):
        pygame.sprite.Sprite.__init__(self)
        # Definition d'un pseudo-pixel de 15 * 15 pxl
        self.image = pygame.Surface([const.SPRITE,const.SPRITE])
        # Variable d'emplacement du sprite dans chaques cases
        self.case_x = xPos
        self.case_y = yPos

        # Variable de position du sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.case_x * const.SPRITE
        self.rect.y = self.case_y * const.SPRITE

        self.grid = grid
        self.dimX = 27
        self.dimY = 27

        self.image.fill((0,255,0))

        

    def vanishing(self):
        self.grid.grid[self.case_y][self.case_x] = '0'

    def appear(self):
        self.grid.grid[self.case_y][self.case_x] = 'p'
