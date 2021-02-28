import pygame
from settings import *

class Spritesheet:

    def __init__(self, filename, columns, rows):
        self.sheet = pygame.image.load(filename)
        
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
        pass
