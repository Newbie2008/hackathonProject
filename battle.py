from settings import *
import pygame
from guis import *

class BattleSystem(pygame.sprite.Sprite):

    def __init__(self, game):
        self.groups = game.gui
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.playerimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        self.playerimg.fill(YELLOW)

        self.mobimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        self.mobimg.fill(RED)
        
        self.playerHealthBar = pygame.Surface((TILESIZE * PLAYER_HEALTH, TILESIZE * 2))
        self.playerHealthBar.fill(RED)
        self.mobHealthBar = pygame.Surface((TILESIZE, TILESIZE * 2))
        self.mobHealthBar.fill(RED)
        
        self.Battling = False
        self.width = 64
        self.height = 64

    def battle(self, mob):
        self.Battling = True
        for attacks in self.game.player.attacks:
            Button()
        while self.Battling:
            self.playerHealthBar = pygame.Surface((TILESIZE * PLAYER_HEALTH * 1.5, TILESIZE))
            self.playerHealthBar.fill(RED)
            self.mobHealthBar = pygame.Surface((TILESIZE * mob.health * 1.5, TILESIZE))
            self.mobHealthBar.fill(RED)
            self.game.update()
            self.game.events()
            self.game.draw()