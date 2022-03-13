from const import *

class Dinosaure(pygame.sprite.Sprite):
    #Definition du Constructeur
    def __init__(self, xPos, yPos, grid):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])

        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos

        self.case_x = xPos
        self.case_y = yPos

        self.image.fill(RED)

    def seDeplace(self,direction):
        if direction[pygame.K_DOWN]:
            if self.case_y < (HEIGHT):
                self.case_y += 1
                self.rect.y = self.case_y * 21
        if direction[pygame.K_UP]:
            if self.case_y > 0:
                self.case_y -= 1
                self.rect.y = self.case_y * 21
        if direction[pygame.K_LEFT]:
            if self.case_x > 0:
                self.case_x -= 1
                self.rect.x = self.case_x * 21
        if direction[pygame.K_RIGHT]:
            if self.case_x < (WIDTH):
                self.case_x += 1
                self.rect.x = self.case_x * 21

class Terrain:
    def __init__(self,screen):
        self.terrain = []

    def lireTerrain(self, fichierTXT):
        pass

    def creationGrille(self):
        for ligne in range(WIDTH+1):
            self.terrain.append([])
            for colonne in range(WIDTH+1):
                self.terrain[ligne].append(0)

    def generate(self,screen):
        for ligne in range(HEIGHT+1):
            for colonne in range(HEIGHT+1):
                color = WHITE
                if self.terrain[ligne][colonne] == 1:
                    color = RED
                pygame.draw.rect(screen,color,[(WIDTH)*colonne,(HEIGHT)*ligne,WIDTH,HEIGHT])
