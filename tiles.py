import pygame
from settings import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y, sprite=None):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if sprite:
            self.image = pygame.image.load(sprite)
        else:
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Chest(pygame.sprite.Sprite):
    def __init__(self, game, x, y, sprite='none'):
        self.groups = game.all_sprites, game.chests
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if sprite == 'none':
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            self.image.fill(WHITE)
        else:
            pass
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

class LevelEnd(pygame.sprite.Sprite):

    def __init__(self, game, x, y, sprite=None):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x
        self.y = y
        if sprite:
            self.image = pygame.image.load(sprite)
        else:
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            self.image.fill(WHITE)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE
        self.check()
    
    def check(self):
        if self.game.player.rect.colliderect(self.rect):
            self.nextlevel()
    
    def nextlevel(self):
        for sprite in self.game.all_sprites:
            sprite.kill()
        
        for sprite in self.game.gui:
            sprite.kill()
        
        self.game.playing = False
        self.game.new()
        self.game.levelNumber +=1
        self.game.load_data(self.game.maps[self.game.levelNumber-1])