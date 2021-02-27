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
            self.image = pygame.image.load(img)
        else:
            self.image = pygame.Surface((TILESIZE/2, TILESIZE/2))
            self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = self.x, self.y
        #self.timeOnscreen -= 1
        #if self.timeOnscreen <= 0:
        #    self.kill
        self.animate()
    
    def animate(self):
        pygame.transform.rotate(self.image, random.randint(0,360))