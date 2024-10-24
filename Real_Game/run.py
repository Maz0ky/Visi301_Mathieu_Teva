import pygame
from mouvement import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Zeta Jeu de la muerta")
clock = pygame.time.Clock()
fps = 60
speed = 10

sky_surf = pygame.image.load(path_for_files + '/graphics/Sky.png').convert()
ground_surf = pygame.image.load(path_for_files + '/graphics/ground.png').convert()

player_surf = pygame.image.load(path_for_files + '/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #assigne un rect à player un sprite où le midbottom sera aux co 80 300
player_gravity = 0

#[{"mouvement":str,"temps":int},{}]
ex_tab_mouv = File_mouv([{"mouvement":"r","temps":30}, {"mouvement":"l","temps":3},
{"mouvement":"j","temps":4}, {"mouvement":"l","temps":23}])

def bouge(mouv,rect):
    global player_gravity
    if mouv == "r":#droite
        rect.right += speed
    elif mouv == "l":#gauche
        rect.right -= speed
    elif mouv == "j":#jump
        player_gravity = -15

def traite_mouv(File:File_mouv,rect):
    mouv = File.get_mouv()["mouvement"]
    File.affiche()
    if File.est_ecoule():
        File.defiler_mouv()
        mouv = File.get_mouv()
    File.defiler_temps()
    bouge(mouv,rect)


def tick_mouv(periode):
    tps = periode * fps #car nous sommes en 60fps
    pass
            
            

list_moving = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -15
    
    screen.blit(sky_surf,(0,0))#pose une surface sur l'ecran du jeu
    screen.blit(ground_surf,(0,300))
    
    player_gravity += 0.5
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
    
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
    #     player_rect.right += speed
    # if keys[pygame.K_LEFT] or keys[pygame.K_q]:
    #     player_rect.right -= speed
    
    if not ex_tab_mouv.est_vide():
        traite_mouv(ex_tab_mouv, player_rect)
    
    
    screen.blit(player_surf, player_rect)
        
    pygame.display.flip() #update tout l'ecran
    clock.tick(fps) # max 60fps pour le jeu