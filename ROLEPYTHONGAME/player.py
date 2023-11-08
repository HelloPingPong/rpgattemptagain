import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups) # Call Sprite initializer - super() is used to inherit from the Sprite class in pygame
        self.image = pygame.image.load('../graphics/test/placeholder.png').convert_alpha() # Create image
        self.rect = self.image.get_rect(topleft = pos) # Create rectangle