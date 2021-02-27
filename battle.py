from settings import *
import pygame

class BattleSystem(pygame.sprite.Sprite):

    def __init__(self, game):
        self.groups = game.all_sprites
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.playerimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        self.playerimg.fill(YELLOW)
        self.mobimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        self.mobimg.fill(RED)
        self.playerHealthBar = pygame.Surface((TILESIZE * PLAYER_HEALTH, TILESIZE))
        self.mobHealthBar = pygame.Surface((TILESIZE, TILESIZE))
        self.Battling = False

    def battle(self, mob):
        self.mobHealthBar = pygame.Surface((TILESIZE * mob.health, TILESIZE))
        self.Battling = True
        while self.Battling:
            self.game.update()
            self.game.events()
            self.game.draw(self.playerimg, self.mobimg)