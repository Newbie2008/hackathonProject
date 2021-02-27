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

    def menu(self, Text, color):
        self.button =  Button(WIDTH/2, HEIGHT/2, 12, 5, Text, color, self.game, 32)
        menu = True
        while menu:
            self.game.screen.fill(BACKGROUND_COLOR)
            self.button.update()
            self.game.mouse.update()
            self.game.events()
            pygame.display.flip()
    