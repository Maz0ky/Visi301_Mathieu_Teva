# Import
from mouvement import *
from gestion_page import *
from initialisations import *
from sys import exit

# Game loop principal
while True:
    
    if level == -2: # Accueil

        # [DEBUT] Gestion des évènements
        for event in pygame.event.get():
            level = gestion_evenements_end(event, level, retour_from_end_rect)

        # [FIN] Mise à Jour de la page
        mise_a_jour_page_end(screen, clock, fps, retour_from_end_surf, retour_from_end_rect)
    
    if level == -1: # Accueil

        # [DEBUT] Gestion des évènements
        for event in pygame.event.get():
            level = gestion_evenements_accueil(event, level, start_rect)

        # [FIN] Mise à Jour de la page
        mise_a_jour_page_accueil(screen, clock, fps, start_surf, start_rect)

    elif level == 0: # Choix niveaux

        # [DEBUT] Gestion des évènements
        for event in pygame.event.get():
            level, Joueur = gestion_evenements_choix_niveau(event, level, button_retour_de_choixlvl, levels_info)

        # [FIN] Mise à Jour de la page
        mise_a_jour_page_choix_niveau(screen, clock, fps, button_retour_de_choixlvl, levels_info)

    elif level == 1:
        if Joueur != None and Joueur.is_finish():
            Joueur.respawn()
            Joueur.reset()  
            levels_info[1][3] = True
            level = 0
            genere_liste_elements = False
            file_mouvement.clear()
            elements_deplacables = []
        elif Joueur != None:
            # [DEBUT] Gestion des évènements
            for event in pygame.event.get():
                elements_deplacables, mouse_offset, genere_liste_elements, selected_element, player_rect, click_again, level = gestion_evenements_level_1(screen, event, level, elements_fixes, elements_deplacables, selected_element, mouse_offset, bouton_envoi, click_again, player_rect, player_surf, button_retour_de_page, Joueur, menu)

            # [2] Traite l'envoie d'une liste d'éléments
            genere_liste_elements, click_again, elem_actuel = traiter_envoie(genere_liste_elements, elements_deplacables, click_again, file_mouvement, Joueur)

            # [FIN] Mise à jour de la page
            mise_a_jour_page_level_1(screen, elements_fixes, elements_deplacables, bouton_envoi, clock, fps, button_retour_de_page, Joueur, menu, barres_separations_interface, file_mouvement, elem_actuel)

    elif level == 2:
        if Joueur != None and Joueur.is_finish():
            Joueur.respawn()
            Joueur.reset()
            levels_info[2][3] = True
            level = 0
            genere_liste_elements = False
            file_mouvement.clear()
            elements_deplacables = []
        elif Joueur != None:
            # [DEBUT] Gestion des évènements
            for event in pygame.event.get():
                elements_deplacables, mouse_offset, genere_liste_elements, selected_element, player_rect, click_again, level = gestion_evenements_level_1(screen, event, level, elements_fixes, elements_deplacables, selected_element, mouse_offset, bouton_envoi, click_again, player_rect, player_surf, button_retour_de_page, Joueur, menu)

            # [2] Traite l'envoie d'une liste d'éléments
            genere_liste_elements, click_again, elem_actuel = traiter_envoie(genere_liste_elements, elements_deplacables, click_again, file_mouvement, Joueur)

            # [FIN] Mise à jour de la page
            mise_a_jour_page_level_1(screen, elements_fixes, elements_deplacables, bouton_envoi, clock, fps,  button_retour_de_page, Joueur, menu, barres_separations_interface, file_mouvement, elem_actuel)

    elif level == 3:
        if Joueur != None and Joueur.is_finish():
            Joueur.respawn()
            Joueur.reset()
            levels_info[3][3] = True
            level = 0
            genere_liste_elements = False
            file_mouvement.clear()
            elements_deplacables = []

        else:
            # [DEBUT] Gestion des évènements
            for event in pygame.event.get():
                elements_deplacables, mouse_offset, genere_liste_elements, selected_element, player_rect, click_again, level = gestion_evenements_level_1(screen, event, level, elements_fixes, elements_deplacables, selected_element, mouse_offset, bouton_envoi, click_again, player_rect, player_surf, button_retour_de_page, Joueur, menu)

            # [2] Traite l'envoie d'une liste d'éléments
            genere_liste_elements, click_again, elem_actuel = traiter_envoie(genere_liste_elements, elements_deplacables, click_again, file_mouvement, Joueur)

            # [FIN] Mise à jour de la page
            mise_a_jour_page_level_1(screen, elements_fixes, elements_deplacables, bouton_envoi, clock, fps,  button_retour_de_page, Joueur, menu, barres_separations_interface, file_mouvement, elem_actuel)

    elif level == 4:
        if Joueur != None and Joueur.is_finish():
            Joueur.respawn()
            Joueur.reset()
            levels_info[4][3] = True
            level = 0
            genere_liste_elements = False
            file_mouvement.clear()
            elements_deplacables = []

        else:
            # [DEBUT] Gestion des évènements
            for event in pygame.event.get():
                elements_deplacables, mouse_offset, genere_liste_elements, selected_element, player_rect, click_again, level = gestion_evenements_level_1(screen, event, level, elements_fixes, elements_deplacables, selected_element, mouse_offset, bouton_envoi, click_again, player_rect, player_surf, button_retour_de_page, Joueur, menu)

            # [2] Traite l'envoie d'une liste d'éléments
            genere_liste_elements, click_again, elem_actuel = traiter_envoie(genere_liste_elements, elements_deplacables, click_again, file_mouvement, Joueur)

            # [FIN] Mise à jour de la page
            mise_a_jour_page_level_1(screen, elements_fixes, elements_deplacables, bouton_envoi, clock, fps,  button_retour_de_page, Joueur, menu, barres_separations_interface, file_mouvement, elem_actuel)

    elif level == 5:
        if Joueur != None and Joueur.is_finish():
            Joueur.respawn()
            Joueur.reset()
            level = -2
            genere_liste_elements = False
            file_mouvement.clear()
            elements_deplacables = []

        else:
            # [DEBUT] Gestion des évènements
            for event in pygame.event.get():
                elements_deplacables, mouse_offset, genere_liste_elements, selected_element, player_rect, click_again, level = gestion_evenements_level_1(screen, event, level, elements_fixes, elements_deplacables, selected_element, mouse_offset, bouton_envoi, click_again, player_rect, player_surf, button_retour_de_page, Joueur, menu)

            # [2] Traite l'envoie d'une liste d'éléments
            genere_liste_elements, click_again, elem_actuel = traiter_envoie(genere_liste_elements, elements_deplacables, click_again, file_mouvement, Joueur)

            # [FIN] Mise à jour de la page
            mise_a_jour_page_level_1(screen, elements_fixes, elements_deplacables, bouton_envoi, clock, fps,  button_retour_de_page, Joueur, menu, barres_separations_interface, file_mouvement, elem_actuel)