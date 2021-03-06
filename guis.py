from settings import *
import pygame

class saveMenu:

    def __init__(self, game):
        self.game = game
        self.loadSaveData = False
        self.savemenu = False
        self.menu = False
        self.text = ''
        self.filename = 'save.txt'
        self.savex = 0
        self.savey = 0
        self.save_data = []
        self.levelNumber = 1
    
    def show_save_screen(self):
        self.yesButton =  Button(WIDTH/2, HEIGHT/2, KEYBOARDWIDTH, KEYBOARDHEIGHT, 'Save', LIGHTGREY, self.game, 64, self.game.gui)
        self.noButton =  Button(self.yesButton.x, self.yesButton.y + self.yesButton.height + TILESIZE, KEYBOARDWIDTH, KEYBOARDHEIGHT, "do not save", LIGHTGREY, self.game, 64, self.game.gui)
        self.savemenu = True
        while self.savemenu:
            self.game.update()
            self.game.draw()
            self.game.events()
            if self.game.mouse.CollideButton(self.yesButton):
                self.save()
            if self.game.mouse.CollideButton(self.noButton):
                self.game.quit()

    def save(self):
        self.f = open("{}".format(self.filename), "w+")
        self.f.write("{}\r\n".format(self.game.player.rect.x//TILESIZE))
        self.f.write("{}\r\n".format(self.game.player.rect.y//TILESIZE))
        self.f.write("{}\r\n".format(self.game.player.weapon))
        self.f.write("{}\r\n".format(self.game.levelNumber))
        self.savemenu = False 
        self.game.quit()

    def LoadSaveMenu(self):
        self.Savebutton =  Button(WIDTH/2, HEIGHT/2, KEYBOARDWIDTH, KEYBOARDHEIGHT, 'Open Save', LIGHTGREY, self.game, 64, self.game.gui)
        self.NewSavebutton =  Button(self.Savebutton.x, self.Savebutton.y + self.Savebutton.height + TILESIZE, KEYBOARDWIDTH, KEYBOARDHEIGHT, 'new save', LIGHTGREY, self.game, 64, self.game.gui)
        #self.keyboard  = Keyboard(self.Savebutton.x, self.NewSavebutton.y + KEYBOARDHEIGHT + TILESIZE, KEYBOARDWIDTH, KEYBOARDHEIGHT, self.game, self.game.gui, 'Enter filename here', 32)
        self.menu = True
        while self.menu:
            self.game.update()
            self.game.draw()
            self.game.events()
            if self.game.mouse.CollideButton(self.Savebutton):
                self.Savebutton.kill()
                self.NewSavebutton.kill()
                self.loadSaveData = True
                self.menu = False
            if self.game.mouse.CollideButton(self.NewSavebutton):
                self.Savebutton.kill()
                self.NewSavebutton.kill()
                self.menu = False
                self.loadSaveData = False
    
    def load_save(self):
        self.LoadSaveMenu()
        self.save_data = []
        if self.loadSaveData == True:
            with open(self.filename, "rt") as f:
                for line in f:
                    self.save_data.append(line.strip())
            
            self.savex = self.save_data[0]
            self.savey = self.save_data[1]
            self.savex = int(self.savex)
            self.savey = int(self.savey)
            self.levelNumber = self.save_data[3]

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, text, color, game, font_size, groups, img=None):
        self.groups = groups
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
            self.image = pygame.Surface((width, height))
            self.image.fill(color)
        else:
            self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = self.x, self.y
        self.renderedText = self.font.render(self.text,True, (0, 0, 0))
        #self.game.screen.blit(self.img, self.rect)
        #self.game.screen.blit(self.renderedText, (self.rect.x + self.width/2, self.rect.y + self.font_size))
        #self.game.displayUpdate()

class Mouse():

    def __init__(self, pos, game, image=None):
        self.x, self.y = pos
        self.game = game 
        self.mousedown = False
        pygame.mouse.set_visible(False)
        if image != None:
            self.image = image
        else:
            self.image = pygame.Surface((TILESIZE/4, TILESIZE/4))
            self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
    def CollideButton(self, button):
        if self.mousedown is True:
            if self.rect.colliderect(button.rect):
                return True

class Keyboard(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, game, groups, text, font_size, img=None):
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.width = width
        self.height = height
        self.text = text
        self.starttext = text
        self.font_size = font_size
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        self.x = x
        self.y = y 
        self.renderedText = self.font.render(str(self.text), True, (BLACK))
        
        #self.cursor = pygame.Surface((CURSORWIDTH, CURSORHEIGHT))
        #self.cursor.fill(BLACK)
        #self.cursorrect = self.cursor.get_rect()
        
        if img:
            self.image = pygame.image.load(img)
        else:
            self.image = pygame.Surface((self.width,self.height))
            self.image.fill(LIGHTGREY)
        
        self.rect = self.image.get_rect()

        #self.cursorx = self.x - self.width/2 + CURSORWIDTH
        #self.cursory = self.y

    def update(self):
        self.rect.center = self.x, self.y
        #self.cursorrect.center = self.cursorx, self.cursory
        self.renderText()

    def textinput(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.text == self.starttext:
                    self.text = ''
                if event.key == pygame.K_a:
                    self.text = self.text + 'a'
                    self.cursorx += self.font_size - TILESIZE * 2
                if event.key == pygame.K_b:
                    self.text = self.text + 'b'
                if event.key == pygame.K_c:
                    self.text = self.text + 'c'
                if event.key == pygame.K_d:
                    self.text = self.text + 'd'
                if event.key == pygame.K_e:
                    self.text = self.text + 'e'
                if event.key == pygame.K_f:
                    self.text = self.text + 'f'
                if event.key == pygame.K_g:
                    self.text = self.text + 'g'
                if event.key == pygame.K_h:
                    self.text = self.text + 'h'
                if event.key == pygame.K_i:
                    self.text = self.text + 'i'
                if event.key == pygame.K_j:
                    self.text = self.text + 'j'
                if event.key == pygame.K_k:
                    self.text = self.text + 'k'
                if event.key == pygame.K_l:
                    self.text = self.text + 'l'
                if event.key == pygame.K_m:
                    self.text = self.text + 'm'
                if event.key == pygame.K_n:
                    self.text = self.text + 'n'
                if event.key == pygame.K_o:
                    self.text = self.text + 'o'
                if event.key == pygame.K_p:
                    self.text = self.text + 'p'
                if event.key == pygame.K_q:
                    self.text = self.text + 'q'
                if event.key == pygame.K_r:
                    self.text = self.text + 'r'
                if event.key == pygame.K_s:
                    self.text = self.text + 's'
                if event.key == pygame.K_t:
                    self.text = self.text + 't'
                if event.key == pygame.K_u:
                    self.text = self.text + 'u'
                if event.key == pygame.K_v:
                    self.text = self.text + 'v'
                if event.key == pygame.K_w:
                    self.text = self.text + 'w'
                if event.key == pygame.K_x:
                    self.text = self.text + 'x'
                if event.key == pygame.K_y:
                    self.text = self.text + 'y'
                if event.key == pygame.K_z:
                    self.text = self.text + 'z'
                if event.key == pygame.K_0:
                    self.text = self.text + '0'
                if event.key == pygame.K_1:
                    self.text = self.text + 'z'
                if event.key == pygame.K_2:
                    self.text = self.text + 'z'
                if event.key == pygame.K_3:
                    self.text = self.text + 'z'
                if event.key == pygame.K_4:
                    self.text = self.text + 'z'
                if event.key == pygame.K_5:
                    self.text = self.text + 'z'
                if event.key == pygame.K_6:
                    self.text = self.text + 'z'
                if event.key == pygame.K_7:
                    self.text = self.text + 'z'
                if event.key == pygame.K_8:
                    self.text = self.text + 'z'
                if event.key == pygame.K_z:
                    self.text = self.text + 'z'
    
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
                    if event.key == pygame.K_MINUS:
                        self.text = self.text + '-'
                        self.cursorx += self.font_size - TILESIZE * 2
                if event.key == pygame.K_RETURN:
                    self.game.battle.check(mob)
                    self.text = ''
                    self.screenText = ''
                    self.cursorx = self.x - self.width/2 + CURSORWIDTH
                if event.key == pygame.K_BACKSPACE:
                    if len(self.text) > 0:
                        self.text = self.text[:-1]
                        self.cursorx += TILESIZE * 2 - self.font_size
    
    def renderText(self):
        self.renderedText = self.font.render(str(self.text), True, (BLACK))
