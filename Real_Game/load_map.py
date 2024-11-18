import pygame
from sys import exit
from pytmx.util_pygame import load_pygame
RIGHT,LEFT,BOTTOM,TOP = 0,1,2,3
class Tile(pygame.sprite.Sprite):
    #sera toutes les tuiles construisant la map
    def __init__(self, pos, surf, groups):
        super().__init__(groups)#utilise une classe parenté de pygame pour creer les groupes dans les sprite
        self.image = pygame.transform.scale(surf,(32,32))
        self.rect = self.image.get_rect(topleft = pos)
    
    def get_rect(self):
        return self.rect

class Solid_Block(Tile):
    #classe des blocks collisionables
    def __init__(self, pos, surf, groups):
        super().__init__(pos = pos, surf = surf, groups = groups)
    
    def udate(self, player):
        if self.rect.colliderect(player.get_rect()):
            pass
            

class Fatal_Block(Tile):
    #classe des blocks fatals
    def __init__(self, pos, surf, groups):
        super().__init__(pos = pos, surf = surf, groups = groups)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("Visi301_Mathieu_Teva/Tuile/Image/Sprite_Player_72x72/tile011.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos
        self.blocked = [False for i in range(4)]#represente les 4 sens où le joueur peut être bloqué(right,left,bottom,top)
        
        #______affichage_____
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.is_jumping, self.on_ground = False, False

        self.pos =  pygame.math.Vector2(pos)
        self.vitesse = pygame.math.Vector2(0,0)
        self.force = pygame.math.Vector2(0,0) 
    
    def show(self):
        screen.blit(self.image, self.rect)
        
    def get_rect(self):
        return self.rect
        
    def update(self):
        group_collision = pygame.sprite.spritecollide(self,block_group,False)
        
        self.collisiondroite(group_collision)
        self.collisiongauche(group_collision)
        print(self.blocked)
    
    def collisiondroite(self,group_col:list):
        i = 0
        res = False
        while not res and i < len(group_col):
            block = group_col[i].get_rect()
            if (self.rect.right >= block.left and not self.rect.right > block.right) and not( self.rect.bottom < block.top or self.rect.top > block.bottom):
                #verfie dans un premier temps que la collision s'effectue bien à droite et ensuite que le bloque est bien à la hauteur du joueur
                res = True
                self.rect.right = block.left
            i+=1
        self.blocked[RIGHT] = res
    
    def collisiongauche(self,group_col):
        i = 0
        res = False
        while not res and i < len(group_col):
            block = group_col[i].get_rect()
            if (self.rect.left <= block.right and not self.rect.left < block.left) and not( self.rect.bottom < block.top or self.rect.top > block.bottom):
                res = True
                self.rect.left = block.right
            i+=1
        self.blocked[LEFT] = res
    
    def collisiony(self,group_col):
        pass
        
    def move(self,sens:str):
        assert sens in ('j','l','r','d'), "Doit appartenir à un mouvement connu"
        match sens:
            case 'r':
                if not self.blocked[RIGHT]:#s'il n'y a pas de block à droite
                    self.rect.x += 5
            case 'l':
                if not self.blocked[LEFT]:#s'il n'y a pas de block à droite
                    self.rect.x -= 5
            case 'j':
                if not self.blocked[TOP]:
                    self.rect.y -= 5
            case 'd':
                    if not self.blocked[TOP]:
                        self.rect.y += 5

    
pygame.init()
screen = pygame.display.set_mode((800,672))
clock = pygame.time.Clock()
fps = 60
size_tileset = 32
map = load_pygame('Visi301_Mathieu_Teva/map/map_test.tmx')
sprite_group = pygame.sprite.Group()#groupe regroupant toutes les tuiles de la map
block_group = pygame.sprite.Group()

def creer_tuile(tuiles, attribut:str=''):
    for x,y,surf in tuiles:#creer une tuile
            pos = (x * size_tileset, y * size_tileset)
            match attribut:
                case 'block':
                    block = Solid_Block(pos = pos, surf = surf, groups = sprite_group)
                    block_group.add(block)
                case 'fatal':
                    Fatal_Block(pos = pos, surf = surf, groups = sprite_group)
                case _:
                    Tile(pos = pos, surf = surf, groups = sprite_group)

# parcours toutes les couches
for layer in map.visible_layers:
    if layer.name == 'Block':
        creer_tuile(layer.tiles(),'block')
    elif layer.name == 'Deathful':
        creer_tuile(layer.tiles(),'fatal')
    elif hasattr(layer,'data'):#si la couche a des données alors
        creer_tuile(layer.tiles())
            
Joueur = Player((0,640))

while True:
    deltatime = clock.tick(60) * .001 * fps #stabilise les frames de l'image à 60 fps
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
            
        
    sprite_group.draw(screen)
    Joueur.show()
    Joueur.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        Joueur.move('r')
    if keys[pygame.K_q]:
        Joueur.move('l')
    if keys[pygame.K_z]:
        Joueur.move('j')
    if keys[pygame.K_s]:
        Joueur.move('d')
    
    pygame.display.flip() #update tout l'ecran
    
