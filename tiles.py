import pygame
from settings import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y, sprite=None):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if sprite:
            self.image = sprite
        else:
            self.image = pygame.Surface((TILESIZE, TILESIZE))


class Chest(pygame.sprite.Sprite):
    def __init__(self, game, x, y, sprite='none'):
        self.groups = game.all_sprites, game.chests
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if sprite == 'none':
            self.image = pygame.Surface((TILESIZE, TILESIZE))
        else:
            pass
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.opened = False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.check_if_opened()

    def check_if_opened(self):
        if self.opened == False:
            if self.game.player.rect.colliderect(self.rect):
                self.opened = True
                self.game.player.weapon = 'bullet'