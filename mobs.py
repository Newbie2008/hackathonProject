import pygame 
from settings import *
import random

class mob(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.kill_radius = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE * 20, TILESIZE * 20)
        self.x = x
        self.y = y
        self.moveDelay = 0
        self.chance = 1
        self.speed = 40