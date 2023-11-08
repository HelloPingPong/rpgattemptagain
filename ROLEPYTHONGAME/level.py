import pygame
from settings import *
from tile import Tile
# LEVEL CLASS IS CRUCIAL. contains all sprites, objects, and interactions

class Level:
    def __init__(self):
        
        #get the display surface from anywhere in our code
        self.display_surface = pygame.display.get_surface()
        
        #Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def create_map(self): #Creates world maps into positions
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                #Now use this information to create a certain kind of sprite
                if col == 'x':
                    Tile((x,y),[self.visible_sprites])
                # if col == 'x':
                #     Obstacle((col_index * TILESIZE, row_index * TILESIZE), self.obstacle_sprites, self.visible_sprites)
                # if col == 'p':
                #     self.player = Player((col_index * TILESIZE, row_index * TILESIZE), self.visible_sprites)
            print(row_index)
            print(row)
            
    def run(self):
        self.visible_sprites.draw(self.display_surface)