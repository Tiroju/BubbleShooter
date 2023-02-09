# -*- coding: utf-8 -*-

# Déclaration de la fonction

import pygame
import sys
import math
import random
import Classes


# Lancement des modules inclus dans pygame
pygame.init()


#MUSIQUE ET SONS
mixer.init()
mixer.music.load("Pop.mp3")


font = pygame.font.Font('freesansbold.ttf', 20)
score = 0

# Création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bubble Shooter") 

clock = pygame.time.Clock()

tir = False
tirx = 0
tiry = 0

# Initialisation des groupes de sprite
all_sprites = pygame.sprite.Group()
bubbles = pygame.sprite.Group()

# Rajout du curseur dans le groupe all_sprites
canon = Classes.Canon(random.randint(0,6))
all_sprites.add(canon)

# Création des rangées de bulles qui apparaissent dès le début du jeu
for j in range(5):
    for i in range(16):
        new_bubble = Classes.Bubble(49.75*i,49.75*j, random.randint(1,6))
        all_sprites.add(new_bubble)
        bubbles.add(new_bubble)


### BOUCLE DE JEU  ###
running = True # Variable pour laisser la fenêtre ouverte
while running: # Boucle infinie pour laisser la fenêtre ouverte
    
    # Dessin du fond et des bulles
    screen.fill((173,216,230))
    all_sprites.draw(screen)
    
    
    #Affichage des textes pour l'or et la vie à l'écran
    text = font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(text, (0, 580))
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            tirx, tiry = canon.direction()
            tirx = (canon.rect.x - tirx)
            tiry = (canon.rect.y - tiry)
            tir = True
    
    canon.update()
    
    ax, ay = canon.direction()
    screen.blit(canon.imageFleche,[ax,ay])
    
    # Calcule l'angle entre la flèche et le curseur
    angle = math.atan2(canon.y - canon.rectFleche.centery, canon.x - canon.rectFleche.centerx)
    # Tourne le sprite de la flèche
    rotated_image = pygame.transform.rotate(canon.imageFleche, -math.degrees(angle))
    rotated_rect = rotated_image.get_rect()
    rotated_rect.center = canon.rectFleche.center
    screen.blit(rotated_image, rotated_rect)
    
    if canon.tir(tirx,tiry,tir):
        # Si la bulle tirée va dépasser l'écran, alors elle s'arrête, devient une bulle normale et le joueur tire avec
        # une autre bulle
        if not 0 < canon.rect.x < 750:
            # Pour recadrer la bulle bien au bord de l'écran
            if canon.rect.x < 0:
                canon.rect.x = 0
            elif canon.rect.x > 750:
                canon.rect.x = 750
                
            new_bubble = Classes.Bubble(canon.rect.x,canon.rect.y,canon.couleur)
            all_sprites.add(new_bubble)
            bubbles.add(new_bubble)
            all_sprites.remove(canon)
            canon = Classes.Canon(random.randint(1,6))
            all_sprites.add(canon)
            tir = False
        
        elif not 0 < canon.rect.y < 550:
            # Pour recadrer la bulle bien au bord de l'écran
            if canon.rect.y < 0:
                canon.rect.y = 0
            elif canon.rect.y > 550:
                canon.rect.y = 550
                
            new_bubble = Classes.Bubble(canon.rect.x,canon.rect.y,canon.couleur)
            all_sprites.add(new_bubble)
            bubbles.add(new_bubble)
            all_sprites.remove(canon)
            canon = Classes.Canon(random.randint(1,6))
            all_sprites.add(canon)
            tir = False
            
        # Vérification des collisions entre la bulle tirée et les bulles
        hits = pygame.sprite.spritecollide(canon, bubbles, False)
        for hit in hits:
            if canon.type == hit.type:
                canon.kill()
                canon = Classes.Canon(random.randint(1,6))
                all_sprites.add(canon)
                tir = False
                if hit.eclate(bubbles):
                    score += 2
                    mixer.music.play(1)
                else:
                    if (canon.rect.x - 1) < hit.rect.x:
                        canon.rect.x = (hit.rect.x - 49.75)
                    elif (canon.rect.x + 1) > hit.rect.x:
                        canon.rect.x = (hit.rect.x + 49.75)
                    else:
                        canon.rect.x = hit.rect.x
                    canon.rect.y = hit.rect.y + 49.75
                    
                    new_bubble = Classes.Bubble(canon.rect.x,canon.rect.y,canon.couleur)
                    all_sprites.add(new_bubble)
                    bubbles.add(new_bubble)
                    canon.kill()
                    canon = Classes.Canon(random.randint(1,6))
                    all_sprites.add(canon)
            else:
                tir = False
                if (canon.rect.x - 1) < hit.rect.x:
                    canon.rect.x = (hit.rect.x - 49.75)
                elif (canon.rect.x + 1) > hit.rect.x:
                    canon.rect.x = (hit.rect.x + 49.75)
                else:
                    canon.rect.x = hit.rect.x
                canon.rect.y = hit.rect.y + 49.75
                
                new_bubble = Classes.Bubble(canon.rect.x,canon.rect.y,canon.couleur)
                all_sprites.add(new_bubble)
                bubbles.add(new_bubble)
                canon.kill()
                canon = Classes.Canon(random.randint(1,6))
                all_sprites.add(canon)

            
            
            
    clock.tick(60)
    
    pygame.display.update() # Pour ajouter tout changement à l'écran

