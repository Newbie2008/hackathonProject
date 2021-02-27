import pygame
from settings import *
import random

class Particle(pygame.sprite.Sprite):

    def __init__(self, game, x, y, img=None):
        self.groups = game.all_sprites
        self.x = x
        self.y = y
        self.timeOnscreen = 100
        if img:
            self.img = pygame.image.load(img)
        else:
            self.img = pygame.surface((TILESIZE/8, TILESIZE/8))
        
        self.rect = pygame.img.get_rect()
        
    def update(self):
        self.
        self.timeOnscreen -= 1
        if self.timeOnscreen <= 0:
            self.kill
        self.animate()
    
    def animate(self):
        pass