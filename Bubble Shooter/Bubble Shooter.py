# -*- coding: utf-8 -*-

# Déclaration de la fonction

import pygame
import sys
import Classes

# Lancement des modules inclus dans pygame
pygame.init()

# Création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()


# Initialisation des groupes de sprite
all_sprites = pygame.sprite.Group()
bubbles = pygame.sprite.Group()

# Rajout du curseur dans le groupe all_sprites
curseur = Classes.Curseur()
all_sprites.add(curseur)

# Création des rangées de bulles qui apparaissent dès le début du jeu
for j in range(5):
    for i in range(16):
        new_bubble = Classes.Bubble(50*i,50*j)
        all_sprites.add(new_bubble)
        bubbles.add(new_bubble)


### BOUCLE DE JEU  ###
running = True # Variable pour laisser la fenêtre ouverte
while running: # Boucle infinie pour laisser la fenêtre ouverte
    
    # Dessin du fond
    screen.fill((173,216,230))
    all_sprites.draw(screen)
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement


    # Vérification des collisions entre le curseur et les bulles
    hits = pygame.sprite.spritecollide(curseur, bubbles, True)
    for hit in hits:
        all_sprites.remove(hit)

    all_sprites.update()
    
    clock.tick(60)
    
    pygame.display.update() # Pour ajouter tout changement à l'écran

