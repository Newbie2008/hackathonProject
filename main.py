import pygame
import sys, random
from pygame import mouse

from settings import *
from player import *
from Mobs import *
from battle import *
from tilemap import *
from tiles import *
from guis import *
from particles import *
from sprites import *
from os import path

class Game:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.enemies = []
        self.bullets = []
        self.playing = False
        self.maps= ['mapexample.txt','maps/area-1-map.txt', 'maps/area-2-map.txt', 'maps/area-3-map.txt', 'maps/area-4-map.txt', 'maps/area-5-map.txt', 'maps/area-6-map.txt', ]
        self.gui = pygame.sprite.Group()
        self.mouse = Mouse(pygame.mouse.get_pos(), self, pygame.image.load('assets/cursor.png'))
        self.saveMenu = saveMenu(self)
        self.saveMenu.load_save()
        self.levelNumber = 1
        self.load_data(self.maps[self.levelNumber-1])
        self.saveMenu = saveMenu(self)
        
        self.bulletsound = pygame.mixer.Sound("assets/bullet.wav")
        self.MobHitsound = pygame.mixer.Sound("assets/mob-hit.wav")
        self.mainthemestart = pygame.mixer.Sound("assets/soundtrack(start).wav")
        self.mainTheme = pygame.mixer.Sound("assets/soundtrack-Main.wav")

    def load_data(self, filename):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, filename))

    def new(self):
        self.mainTheme.stop()
        self.mainthemestart.stop()
        self.keyboards = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.battles = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.Bullets = pygame.sprite.Group()
        self.gui = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.saveMenu = saveMenu(self)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row, 'assets/WallTile.png')
                if tile == "P":
                    if self.saveMenu.loadSaveData == True:
                        self.player = Player(
                            self,
                            self.savex,
                            self.savey,
                            self.save_data[2],
                        )
                    else:
                        self.player = Player(self, col, row)
                if tile == 'L':
                    LevelEnd(self,col,row)
                if tile == 'E':
                   mob(self,col,row)
                   #self.enemies.append(mob)
                if tile == "C":
                    self.chest = Chest(self, col, row, pygame.image.load('assets/Chest.png'))
                if tile == ".":
                    pass
        self.camera = Camera(self.map.width, self.map.height)
        self.battle = BattleSystem(self)
        self.mainthemestart.play()
        self.mainTheme.play(-1)
        pygame.mixer.music.set_volume(0.2)
    
    def run(self):
        self.playing = True
        while self.playing:
            pygame.mixer.music.stop()
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()
            self.events()

    def update(self):
        self.mouse.update()
        if not self.saveMenu.savemenu:
            if not self.saveMenu.menu:
                if not self.player.Battling:
                    self.all_sprites.update()
                    self.camera.update(self.player)

    def quit(self):
        pygame.quit()
        sys.exit()
    


    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        if self.saveMenu.savemenu == False:
            if self.saveMenu.menu == False:
                if self.battle.Battling == False:
                    for sprite in self.all_sprites:
                        self.screen.blit(sprite.image, self.camera.apply(sprite))
                    
                    self.screen.blit(self.mouse.image, self.mouse.rect)
                    #for mob in self.mobs:
                    #    self.screen.blit(mob.healthbar, mob.healthbarrect)
                    pygame.display.flip()
                else:
                    self.screen.fill(BACKGROUND_COLOR)
                    self.screen.blit(self.battle.playerimg, (0, HEIGHT -TILESIZE * 20))
                    self.screen.blit(self.battle.mobimg, (WIDTH -TILESIZE * 20, 0))
                    self.screen.blit(self.battle.playerHealthBar, (0 + self.battle.width/2, HEIGHT -TILESIZE * 24))
                    self.screen.blit(self.battle.mobHealthBar, (WIDTH - TILESIZE * 37, 0 + self.battle.height/2))
                    self.screen.blit(self.battle.keyboard.image, self.battle.keyboard.rect)
                    self.screen.blit(self.battle.keyboard.cursor, self.battle.keyboard.cursorrect)
                    self.screen.blit(self.battle.keyboard.renderedText, self.battle.keyboard.rect)
                    self.screen.blit(self.battle.questionBoard.image, self.battle.questionBoard.rect)
                    self.screen.blit(self.battle.questionBoard.renderedText, self.battle.questionBoard.rect)
                    self.screen.blit(self.mouse.image, self.mouse.rect)
                    pygame.display.flip()
            else:
                for gui in self.gui:
                    gui.update()
                    self.screen.blit(gui.image, gui.rect)
                    self.screen.blit(gui.renderedText, gui.rect)
                #self.screen.blit(self.saveMenu.Savebutton.renderedText, (self.saveMenu.Savebutton.rect.x + self.saveMenu.Savebutton.width/10, self.saveMenu.Savebutton.rect.y))
                self.screen.blit(self.saveMenu.keyboard.cursor, self.saveMenu.keyboard.cursorrect)
                self.screen.blit(self.mouse.image, self.mouse.rect)
                pygame.display.flip()

        else:
            for gui in self.gui:
                gui.update()
                self.screen.blit(gui.image, gui.rect)
                self.screen.blit(gui.renderedText, gui.rect)
            self.screen.blit(self.mouse.image, self.mouse.rect)
            pygame.display.flip()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.saveMenu.show_save_screen()
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.playing:
                        self.saveMenu.show_save_screen()
                    self.quit()
            
                if event.key == pygame.K_SPACE and self.player.weapon != "none":
                    self.bulletsound.play()
                    if self.player.weapon == "bullet":                        
                        if self.player.up is True:
                            Bullet(self,self.player.rect.centerx,self.player.rect.centery,0,-10,)

                        if self.player.down is True:
                            Bullet(self,self.player.rect.centerx,self.player.rect.centery,0,10,)

                        if self.player.right is True:
                            Bullet(self,self.player.rect.centerx,self.player.rect.centery,10,0,)

                        if self.player.left is True:
                            Bullet(self,self.player.rect.centerx,self.player.rect.centery,-10,0,)
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse.mousedown = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse.mousedown = False


g = Game()
while True:
    g.new()
    g.run()
#easter egg OWO UWU