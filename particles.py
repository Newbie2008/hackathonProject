import pygame
from settings import *
import random

class Particle(pygame.sprite.Sprite):

    def __init__(self, game, x, y, color=[WHITE], img=None):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.color = color
        self.timeOnscreen = random.randint(0, PARTICLETIME)
        if img:
            self.image = pygame.image.load(img)
        else:
            self.image = pygame.Surface((TILESIZE/4, TILESIZE/4))
            self.image.fill(self.color[random.randint(0,len(self.color)-1)])
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = self.x, self.y
        self.timeOnscreen -= 1
        if self.timeOnscreen <= 0:
            self.kill()
            self.timeOnscreen = 0
        self.animate()
    
    def animate(self):
        self.x += random.randint(PARTICLEOFFSET * -1, PARTICLEOFFSET)
        self.y += random.randint(PARTICLEOFFSET * -1, PARTICLEOFFSET)
        pygame.transform.rotate(self.image, 25)