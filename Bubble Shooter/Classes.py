import pygame
import math

# Classe pour les bulles
class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y, couleur):
        super().__init__()
        
        if couleur == 1:
            self.type = "Red"
        elif couleur == 2:
            self.type = "Green"
        elif couleur == 3:
            self.type = "Blue"
        elif couleur == 4:
            self.type = "Cyan"
        elif couleur == 5:
            self.type = "Magenta"
        else:
            self.type = "Yellow"
        
        self.image = pygame.image.load(self.type + "Bubble.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def eclate(self,bubbles,eclat = False):
        """ Permet de vérifier si les bulles voisines sont de la même couleur et donc de les faire éclater s'il y en a
            au moins 3
        """
        bubbles.remove(self)
        hits = pygame.sprite.spritecollide(self, bubbles, False)
        for hit in hits:
            if self.type == hit.type:
                eclat = hit.eclate(bubbles,True)
        
        if eclat:
            self.kill()
            return True
        else:
            bubbles.add(self)
            return False


# Classe pour le curseur du joueur
class Canon(pygame.sprite.Sprite):
    def __init__(self, couleur):
        super().__init__()
        
        if couleur == 1:
            self.type = "Red"
            self.couleur = 1
        elif couleur == 2:
            self.type = "Green"
            self.couleur = 2
        elif couleur == 3:
            self.type = "Blue"
            self.couleur = 3
        elif couleur == 4:
            self.type = "Cyan"
            self.couleur = 4
        elif couleur == 5:
            self.type = "Magenta"
            self.couleur = 5
        else:
            self.type = "Yellow"
            self.couleur = 6
        
        self.image = pygame.image.load(self.type + "Bubble.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.imageFleche = pygame.image.load("arrow.png")
        self.imageFleche = pygame.transform.scale(self.imageFleche, (50, 100))
        
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 525
        
        self.rectFleche = self.imageFleche.get_rect()
        self.rectFleche.center = (375,525)


    def update(self):
        """ Permet d'obtenir la position du curseur lorsque le joueur bouge la souris
        """
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        
        
    def direction(self):
        """ Fonction qui permet de faire tourner le sprite de la flèche autour de la bulle que l'on va tirer
        """
        if self.rect.x == self.x and self.rect.y == self.y:
            return self.rect.x, self.rect.y

        A = pygame.math.Vector2(self.rect.x, self.rect.y)
        B = pygame.math.Vector2(self.x, self.y)

        V = B - A
        V.scale_to_length(90)

        C = A + V
        return C.x, C.y
    
    def tir(self,x,y,avance):
        """ Fonction pour faire avancer la bulle une fois qu'on l'a tirée
        """
        if avance == True:
            self.rect.x -= x*0.25
            self.rect.y -= y*0.25
            return True
        return False
    