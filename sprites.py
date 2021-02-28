import pygame
from settings import *

class Spritesheet:

    def __init__(self, filename, columns, game, rows):
        self.sheet = pygame.image.load(filename)
        self.game = game
        
        self.columns = columns
        self.rows = rows
        self.totalCells = self.columns * self.rows

        self.rect = self.sheet.get_rect()
        w = self.cellwidth = self.rect.width/columns
        h = self.cellheight = self.rect.height/rows
        hw, hh = self.cellCenter = (w/2, h/2)

        self.cells = list([(index % columns * w, index/columns * h,w,h)for index in range(self.totalCells)])
        self.handle = list()
    
    def draw(self, surface, cellIndex, x, y, handle=0):
        self.game.screen.fill(LIGHTGREY)
        self.game.screen.blit(self.sheet(x + self.handle[handle][0], y + self.handle[handle][1], self.cells[cellIndex]))
        self.game.displayUpdate()
