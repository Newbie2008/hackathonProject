import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, weapon="none"):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.health = PLAYER_HEALTH

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.weapon = weapon
        self.moveDelay = 0