         
class File_mouv:
    
    def __init__(self,file=[]):
        """ Instancie une file vide """
        self.file = file #un tableau
		
    def enfiler_mouv(self, element):
        """ Enfile un élément en queue de file """
        self.file.append(element)
		
    def defiler_mouv(self):
        """ Défile ( si la file n'est pas vide ! ) un élément en tête de file, et le renvoie """
        if not self.est_vide():
            return self.file.pop(0)
        
    def defiler_temps(self):
        """ Permet de decrementer le temps d'un cran pour le premier mouvement"""
        if not self.est_ecoule() and not self.est_vide():
            self.file[0]["temps"] -= 1
        
    def est_vide(self):
        """ Renvoie True si la file est vide, False sinon """
        return len(self.file) == 0
    
    def est_ecoule(self):
        """ Verifie que le premier mouvement de la file n'est pas finie"""
        if not self.est_vide():
            return self.file[0]["temps"] == 0

    def affiche(self):
        print(self.file)
    
    def get_mouv(self):
        if not self.est_vide():
            return self.file[0]
    
    def clear(self):
        self.file = []

# Generation de la liste des éléments déplaçables

def generer_liste_elements(elements_deplacables):
    """Trie et génère la liste d'éléments déplaçables"""
    elements_triee = sorted(elements_deplacables, key=lambda elem: elem[1].x)
    liste_elements = []
    for elem in elements_triee:
        if elem[2] == "Real_Game/elem/up-arrow.png":
            mouv = "j"
        elif elem[2] == "Real_Game/elem/right-arrow.png":
            mouv = "r"
        elif elem[2] == "Real_Game/elem/left-arrow.png":
            mouv = "l"
        elif elem[2] == "Real_Game/elem/pause.png":
            mouv = "p"
        
        liste_elements.append({"mouvement": mouv, "temps": elem[3]})
    return liste_elements

def traiter_envoie(genere_liste_elements, elements_deplacables, click_again, ex_tab_mouv, Joueur, block_group):
    """Gère l'envoi d'une liste d'éléments"""
    if not ex_tab_mouv.est_vide():
        Joueur.move_from_File(ex_tab_mouv)
    else:
        click_again = True # Réactive envoie
    

    if genere_liste_elements:
        liste_mouvements = generer_liste_elements(elements_deplacables)  # Retourne la liste des mouvements pour l'utiliser dans Code 3
        print("Mouvements générés :", liste_mouvements)
        for mouvement in liste_mouvements:
            ex_tab_mouv.enfiler_mouv(mouvement)  # Ajoute à la file des mouvements
        genere_liste_elements = False

    return genere_liste_elements, click_again