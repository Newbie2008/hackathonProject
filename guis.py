from sys import flags

from pygame import rect
from settings import *
import pygame

class saveMenu:

    def __init__(self, game):
        self.game = game
        self.loadSaveData = False
    
    def show_save_screen(self):
        self.filename = input("filename: ")
        self.f = open(f"{self.filename}", "w+")
        self.f.write(f"{self.player.rect.x//TILESIZE}\r\n")
        self.f.write(f"{self.player.rect.y//TILESIZE}\r\n")
        self.f.write(f"{self.player.weapon}\r\n")

    def LoadSaveMenu(self, Text, color):
        self.Savebutton =  Button(WIDTH/2, HEIGHT/2, 12, 5, Text, color, self.game, 32)
        menu = True
        while menu:
            self.game.events()
            if self.game.mouse.CollideButton(self.Savebutton):
                self.menu = False
                self.keyboardInput(Keyboard(self.Savebutton.x, self.Savebutton.y, self.Savebutton.width, self.Savebutton.height, self.game, None))
            self.game.screen.fill(BACKGROUND_COLOR)
            self.Savebutton.update()
            self.game.screen.blit(self.game.mouse.img, self.game.mouse.rect)
            self.game.mouse.update()
            pygame.display.flip()
    
    def keyboardInput(self, keyboard):
        keyboardInput = True
        while keyboardInput:
            pass


    def load_save(self):
        self.LoadSaveMenu('open save', ORANGE)
        self.save_data = []
        self.filename = input("filename: ")
        if self.filename == "none":
            self.loadSaveData = False
        if self.filename != "none":
            with open(self.filename, "rt") as f:
                for line in f:
                    self.save_data.append(line.strip())

            self.savex = self.save_data[0]
            self.savey = self.save_data[1]
            self.savex = int(self.savex)
            self.savey = int(self.savey)
            self.loadSaveData = True
        else:
            self.loadSaveData = False

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, text, color, game, font_size, img=None):
        self.groups = game.gui
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font_size = font_size
        self.width = width
        self.height = height
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        if img == None:
            self.img = pygame.Surface((width * TILESIZE, height * TILESIZE))
            self.img.fill(color)
        else:
            self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()

    def update(self):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.renderedText = self.font.render(self.text,True, (0, 0, 0))
        self.game.screen.blit(self.img, self.rect)
        self.game.screen.blit(self.renderedText, (self.rect.x + self.width/2, self.rect.y + self.font_size))

class Mouse():

    def __init__(self, pos, game, image=None):
        self.x, self.y = pos
        self.game = game 
        self.mousedown = False
        pygame.mouse.set_visible(False)
        if image != None:
            self.img = image
        else:
            self.img = pygame.Surface((TILESIZE/4, TILESIZE/4))
            self.img.fill(WHITE)
        
        self.rect = self.img.get_rect()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
    def CollideButton(self, button):
        if self.mousedown is True:
            if self.rect.colliderect(button.rect):
                return True

class Keyboard(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, game, img=None):
        self.groups = game.gui
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.width = width
        self.height = height
        self.text = ''
        self.font_size = KEYBOARDHEIGHT - 4
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        self.x = x
        self.y = y 
        self.screenText = self.font.render(str(self.text), True, (BLACK))
        
        self.cursor = pygame.Surface((CURSORWIDTH, CURSORHEIGHT))
        self.cursor.fill(BLACK)
        self.cursorrect = self.cursor.get_rect()
        
        if img:
            self.img = pygame.image.load(img)
        else:
            self.img = pygame.Surface((self.width,self.height))
            self.img.fill(LIGHTGREY)
        
        self.rect = self.img.get_rect()

        self.cursorx = self.x - self.width/2 + CURSORWIDTH
        self.cursory = self.y

    def update(self):
        self.rect.center = self.x, self.y
        self.cursorrect.center = self.cursorx, self.cursory
        self.renderText()
    
    def cursorinput(self, mob):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if len(self.text) < 7:
                    if event.key == pygame.K_0:
                        self.text = self.text + '0'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_1:
                        self.text = self.text + '1'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_2:
                        self.text = self.text + '2'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_3:
                        self.text = self.text + '3'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_4:
                        self.text = self.text + '4'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_5:
                        self.text = self.text + '5'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_6:
                        self.text = self.text + '6'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_7:
                        self.text = self.text + '7'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_8:
                        self.text = self.text + '8'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_9:
                        self.text = self.text + '9'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_9:
                        self.text = self.text + '9'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_PERIOD:
                        self.text = self.text + '.'
                        self.cursorx += self.font_size - TILESIZE * 2
                    if event.key == pygame.K_RETURN:
                        self.game.battle.check(mob)
                        self.text = ''
                        self.screenText = ''
                        self.cursorx = self.x - self.width/2 + CURSORWIDTH
    
    def renderText(self):
        self.screenText = self.font.render(str(self.text), True, (BLACK))
