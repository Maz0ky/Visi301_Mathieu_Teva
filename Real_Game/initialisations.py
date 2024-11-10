# Import
import pygame
from mouvement import *

# Initialisations

def init():
    elements_fixes, elements_deplacables, selected_element, mouse_offset, click_again, ex_tab_mouv = initialisation_de_base()
    button_font, button_text, button_rect = initialiser_bouton_envoi()
    menu_visible, menu_rect, option_supprimer, option_temps, element_concerne = initialisation_menu()
    player_surf, player_rect, player_gravity, speed = initialisation_joueur()
    return elements_fixes, elements_deplacables, selected_element, mouse_offset, click_again,button_font, button_text, button_rect, menu_visible, menu_rect, option_supprimer, option_temps, element_concerne, ex_tab_mouv, player_surf, player_rect, player_gravity, speed

# Initialisation des éléments de bases

def initialisation_de_base():
    elements_fixes = initaliser_elements_fixes()
    elements_deplacables = []
    selected_element = None # Correspond à l'élément séléctionné
    mouse_offset = (0, 0)
    click_again = True # Indique si l'on peut cliquer à nouveau
    ex_tab_mouv = File_mouv([]) # Initialisation de la file des mouvements
    return elements_fixes, elements_deplacables, selected_element, mouse_offset, click_again, ex_tab_mouv

def initaliser_elements_fixes():
    """Création des éléments de mouvements"""
    surf_1, rect_1, img1 = cree_surf_img('elem/left-arrow.png', 100, 100, 40 , 300)
    surf_2, rect_2, img2 = cree_surf_img('elem/up-arrow.png', 100, 100, 120, 300)
    surf_3, rect_3, img3 = cree_surf_img('elem/right-arrow.png', 100, 100, 200, 300)
    elements_fixes = [(surf_1, rect_1, img1), (surf_2, rect_2, img2), (surf_3, rect_3, img3)]
    return elements_fixes

def cree_surf_img(chemin: str, width, height, pos_x, pos_y):
    """Création des éléments fixes (mouvements)"""
    surf = pygame.image.load(chemin).convert_alpha()
    surf = pygame.transform.scale(surf, (width, height))
    rect = surf.get_rect(topleft=(pos_x, pos_y))
    return surf, rect, chemin

# Initialisation du bouton d'envoi

def initialiser_bouton_envoi():
    """Création du bouton "Envoi"""
    button_font = pygame.font.Font(None, 36)
    button_text = button_font.render("Envoie", True, (255, 255, 255))
    button_rect = pygame.Rect(700, 360, 90, 40)
    return button_font, button_text, button_rect

# Initialisation du menu (suppression et temps)

def initialisation_menu():
    menu_visible = False # Indique si le menu (temps et suppression) doit être affiché
    element_concerne = None
    menu_rect, option_supprimer, option_temps = None, None, None # A l'état "None" puisque Faux par défaut
    return menu_visible, menu_rect, option_supprimer, option_temps, element_concerne

# Initialisation du joueur et de sa vitesse

def initialisation_joueur():
    player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom=(880, 300))  # Position initiale du joueur
    player_gravity = 0
    speed = 10
    return player_surf, player_rect, player_gravity, speed