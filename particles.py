import pygame
from settings import *
import random

class Particle(pygame.sprite.Sprite):

    def __init__(self, game, x, y, img=None):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.timeOnscreen = random.randint(5, 7)
        if img:
            self.image = pygame.image.load(img)
        else:
            self.image = pygame.Surface((TILESIZE/2, TILESIZE/2))
            self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = self.x, self.y
        self.timeOnscreen -= 1
        print(self.timeOnscreen)
        if self.timeOnscreen <= 0:
            self.kill()
            self.timeOnscreen = 0
        self.animate()
    
    def animate(self):
        self.x += random.randint(-2, 2)
        self.y += random.randint(-2, 2)
        pygame.transform.rotate(self.image, 25)