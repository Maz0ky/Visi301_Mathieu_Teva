# Import
import pygame
from pygame.locals import *
from Initialisations import *

# Gestion des évènements

def gestion_evenement_base(screen, event):
    if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def gestion_evenements_accueil(screen, event, level, start_rect):
    gestion_evenement_base(screen, event)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if start_rect.collidepoint(mouse_pos):
            level = 0
    return level

def gestion_evenements_choix_niveau(screen, event, level, level_1_rect, level_2_rect, level_3_rect):
    gestion_evenement_base(screen, event)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if level_1_rect.collidepoint(mouse_pos):
            level = 1
        if level_1_rect.collidepoint(mouse_pos):
            pass
        if level_1_rect.collidepoint(mouse_pos):
            pass
    return level

def gestion_evenements_level_1(screen, event, elements_fixes, elements_deplacables, selected_element, mouse_offset, button_rect, menu_visible, menu_rect, option_supprimer, option_temps, element_concerne, click_again, player_rect, player_surf, menu_temps_rect, option_de_temps, menu_temps_visible, option_fermer_temps, option_moins, option_plus):
    """Gestion des évènements"""
    gestion_evenement_base(screen, event)

    genere_liste_elements = False # Indique si l'on doit envoyer la liste
    # Clic pour sélectionner une surface ou le bouton
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        
        # Vérification des blocs fixes pour créer des blocs déplaçables si besoin
        for element in elements_fixes:
            if element[1].collidepoint(mouse_pos): # element[1] est sa surface
                new_surf, new_rect, new_img = cree_surf_img(element[2], element[1].width, element[1].height, element[1].x, element[1].y)
                temps_default = 10
                elements_deplacables.append([new_surf, new_rect, new_img, temps_default])
                selected_element = (new_surf, new_rect, new_img)
                mouse_offset = (mouse_pos[0] - new_rect.x, mouse_pos[1] - new_rect.y)
                break

        # Vérification des blocs déplaçables pour les déplacer si besoin
        for element in elements_deplacables:
            if element[1].x < -20 or element[1].x > 720:
                elements_deplacables.remove(element)
                break

            if element[1].collidepoint(mouse_pos):
                if event.button == 1: # event.button == 1 désigne le clique gauche
                    selected_element = element
                    mouse_offset = (mouse_pos[0] - element[1].x, mouse_pos[1] - element[1].y)
                    break

                if event.button == 3:  # Clic droit
                    # Afficher un menu contextuel
                    menu_visible = True
                    element_concerne = element
                    menu_rect, option_supprimer, option_temps = affiche_menu(screen, menu_rect)
                    break

    if menu_visible:
        menu_rect, option_supprimer, option_temps = affiche_menu(screen, menu_rect)
        # Gestion du menu
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Gestion du menu
            if menu_rect.collidepoint(mouse_pos):
                # Supprimer l'élément sélectionné si "Supprimer" est cliqué
                if option_supprimer.get_rect(topleft=(menu_rect.x + 10, menu_rect.y + 10)).collidepoint(mouse_pos):
                    elements_deplacables.remove(element_concerne)
                    menu_visible = False
                
                # Modifier le temps si "Modifier le temps" est cliqué
                if option_temps.get_rect(topleft=(menu_rect.x + 10, menu_rect.y + 40)).collidepoint(mouse_pos):
                    # Champ pour saisir le temps
                    

                    menu_temps_rect, element_concerne[3], option_fermer_temps, option_moins, option_plus, option_de_temps = affiche_menu_temps(screen, menu_temps_rect, element_concerne[3], option_fermer_temps, option_moins, option_plus, option_de_temps)

                    menu_visible = False
                    menu_temps_visible = True
        
    if menu_temps_visible:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if option_moins.get_rect(topleft=(menu_temps_rect.x + 10, menu_temps_rect.y + 10)).collidepoint(mouse_pos):
                element_concerne[3] -= 1
                menu_temps_rect, element_concerne[3], option_fermer_temps, option_moins, option_plus, option_de_temps = affiche_menu_temps(screen, menu_temps_rect, element_concerne[3], option_fermer_temps, option_moins, option_plus, option_de_temps)
                
            if option_plus.get_rect(topleft=(menu_temps_rect.x + 85, menu_temps_rect.y + 10)).collidepoint(mouse_pos):
                element_concerne[3] += 1
                menu_temps_rect, element_concerne[3], option_fermer_temps, option_moins, option_plus, option_de_temps = affiche_menu_temps(screen, menu_temps_rect, element_concerne[3], option_fermer_temps, option_moins, option_plus, option_de_temps)

            if option_fermer_temps.get_rect(topleft=(menu_temps_rect.x + 10, menu_temps_rect.y + 40)).collidepoint(mouse_pos):
                menu_temps_visible = False

    # Relâchement du clic gauche : arrêt du déplacement
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        selected_element = None

    if event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()
    # Vérification du clic sur le bouton Envoi
        if button_rect.collidepoint(mouse_pos):
            if click_again == True:
                click_again = False
                player_rect = player_surf.get_rect(midbottom=(880, 300))
                genere_liste_elements = True
    
    # Déplacement de l'élément sélectionné avec la souris
    if selected_element is not None:
        mouse_pos = pygame.mouse.get_pos()
        selected_element[1].x = mouse_pos[0] - mouse_offset[0]
        selected_element[1].y = mouse_pos[1] - mouse_offset[1]

    return elements_deplacables, mouse_offset, genere_liste_elements, selected_element, menu_visible, menu_rect, option_supprimer, option_temps, element_concerne, player_rect, click_again, menu_temps_rect, option_de_temps, menu_temps_visible, option_fermer_temps, option_moins, option_plus

# Les menus de la partie création de liste

def affiche_menu(screen, menu_rect):
    """Affiche un menu contextuel pour l'élément sélectionné."""
    font = pygame.font.Font(None, 36)
    # Création des options de menu
    option_supprimer = font.render("Supprimer", True, (255, 255, 255))
    option_temps = font.render("Modifier temps", True, (255, 255, 255))
    
    # Position du menu contextuel
    menu_rect = pygame.Rect(350, 320, 200, 80)
    pygame.draw.rect(screen, (50, 50, 50), menu_rect)  # Fond du menu contextuel
    pygame.draw.rect(screen, (200, 200, 200), menu_rect, 2)  # Bordure du menu contextuel
    
    return menu_rect, option_supprimer, option_temps

def affiche_menu_temps(screen, menu_temps_rect, temps, option_fermer_temps, option_moins, option_plus, option_de_temps):
    font = pygame.font.Font(None, 36)
    # Création des options de menu
    option_moins  = font.render("-", True, (255, 255, 255))
    option_de_temps = font.render(str(temps), True, (255, 255, 255))
    option_plus = font.render("+", True, (255, 255, 255))
    option_fermer_temps  = font.render("Fermer", True, (255, 255, 255))
    
    # Position du menu contextuel
    menu_temps_rect = pygame.Rect(350, 320, 200, 80)
    pygame.draw.rect(screen, (50, 50, 50), menu_temps_rect)  # Fond du menu contextuel
    pygame.draw.rect(screen, (200, 200, 200), menu_temps_rect, 2)  # Bordure du menu contextuel
    
    return menu_temps_rect, temps, option_fermer_temps, option_moins, option_plus, option_de_temps

# Mise à jour de la page

def mise_a_jour_page_base_debut(screen):
    # Mise à jour de l'affichage
    screen.fill((30, 30, 30))

def mise_a_jour_page_base_fin(clock, fps):
    pygame.display.flip()  # Met à jour l'écran
    clock.tick(fps)  # Limite à 60 FPS

def mise_a_jour_page_accueil(screen, clock, fps, start_surf, start_rect):
    """Met à jour la page"""

    mise_a_jour_page_base_debut(screen)

    screen.blit(start_surf, start_rect)

    mise_a_jour_page_base_fin(clock, fps)

def mise_a_jour_page_choix_niveau(screen, clock, fps, level_1_surf, level_1_rect, level_2_surf, level_2_rect, level_3_surf, level_3_rect):
    """Met à jour la page"""

    mise_a_jour_page_base_debut(screen)

    screen.blit(level_1_surf, level_1_rect)
    screen.blit(level_2_surf, level_2_rect)
    screen.blit(level_3_surf, level_3_rect)

    mise_a_jour_page_base_fin(clock, fps)

def mise_a_jour_page_level_1(screen, elements_fixes, elements_deplacables, button_text, button_rect, menu_visible, menu_rect, option_supprimer, option_temps, player_surf, player_rect, clock, fps, menu_temps_visible, option_moins, option_de_temps, option_plus, option_fermer_temps, menu_temps_rect):
    """Met à jour la page"""

    mise_a_jour_page_base_debut(screen)

    # Séparation des deux interfaces
    pygame.draw.rect(screen, (232,195,158), Rect(0, 0, 800, 800))
    
    # Met à jour les éléments sur la page
    for surf, rect, img in elements_fixes:
        screen.blit(surf, rect)

    for surf, rect, img, tps in elements_deplacables:
        screen.blit(surf, rect)

    # Met à jour le bouton envoie
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 5))

    # Afficher le joueur
    screen.blit(player_surf, player_rect)
    
    # Met à jour le menu si il est affiché
    if menu_visible:
        screen.blit(option_supprimer, (menu_rect.x + 10, menu_rect.y + 10))
        screen.blit(option_temps, (menu_rect.x + 10, menu_rect.y + 40))

    if menu_temps_visible:
        screen.blit(option_moins, (menu_temps_rect.x + 10, menu_temps_rect.y + 10))
        screen.blit(option_de_temps, (menu_temps_rect.x + 40, menu_temps_rect.y + 10))
        screen.blit(option_plus, (menu_temps_rect.x + 85, menu_temps_rect.y + 10))
        screen.blit(option_fermer_temps, (menu_temps_rect.x + 10, menu_temps_rect.y + 40))

    mise_a_jour_page_base_fin(clock, fps)

    return button_rect, menu_visible, menu_rect, option_supprimer, option_temps, menu_temps_rect, option_moins, option_de_temps, option_plus, option_fermer_temps