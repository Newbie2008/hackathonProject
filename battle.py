from settings import *
import pygame

class BattleSystem(pygame.sprite.Sprite):

    def __init__(self, game):
        self.groups = game.all_sprites
        self.playerimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        self.playerimg.fill(YELLOW)
        self.mobimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        self.playerHealthBar = pygame.Surface(TILESIZE * PLAYER_HEALTH, TILESIZE)
        self.Battling = False

    def battle(self, mob):
        self.Battling = True
        while self.Battling:
            self.game.update()
            self.game.events()
            self.game.draw(self.playerimg, self.mobimg)