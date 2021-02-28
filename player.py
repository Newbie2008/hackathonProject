from os import walk
import random

from pygame import sprite
from tiles import Wall
from sprites import Spritesheet
import pygame
from settings import *
from particles import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, weapon="none"):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.health = PLAYER_HEALTH
        self.walkDown = [pygame.image.load('assets/WalkDown1.png').convert_alpha(), pygame.image.load('assets/WalkDown2.png').convert_alpha(), pygame.image.load('assets/WalkDown3.png').convert_alpha(), pygame.image.load('assets/WalkDown4.png').convert_alpha()]
        self.walkUp = [pygame.image.load('assets/WalkUp1.png').convert_alpha(),pygame.image.load('assets/WalkUp2.png').convert_alpha(),pygame.image.load('assets/WalkUp3.png').convert_alpha(),pygame.image.load('assets/WalkUp4.png').convert_alpha()]
        self.walkLeft = [pygame.image.load('assets/WalkLeft1.png').convert_alpha(),pygame.image.load('assets/WalkLeft2.png').convert_alpha(),pygame.image.load('assets/WalkLeft3.png').convert_alpha(),pygame.image.load('assets/WalkLeft4.png').convert_alpha(),]
        self.walkRight =[pygame.image.load('assets/WalkRight1.png').convert_alpha(),pygame.image.load('assets/WalkRight2.png').convert_alpha(),pygame.image.load('assets/WalkRight3.png').convert_alpha(),pygame.image.load('assets/WalkRight4.png').convert_alpha(),]

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.standing = True
        self.weapon = 'bullet'
        self.moveDelay = 0
        self.Battling = False
        self.walkCount = 0
        self.spriteChangeDelay = 0

    def update(self):
        self.collide_etc()
        self.get_keys()
        self.draw()
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE
        #self.walkDown.draw(self.game.screen,  index %s, self.walkDown.totalCells, )
    
    def draw(self):
        if self.walkCount + 1 >= 4:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                self.image = self.walkLeft[self.walkCount]
                self.spriteChangeDelay += 1 
            if self.right:
                self.image = self.walkRight[self.walkCount]
                self.spriteChangeDelay += 1 
            if self.up:
                self.image = self.walkUp[self.walkCount]
                self.spriteChangeDelay += 1 
            if self.down:
                self.image = self.walkDown[self.walkCount]
                self.spriteChangeDelay += 1
            
        else:
            if self.left:
                self.image = self.walkLeft[0]
            if self.right:
                self.image = self.walkRight[0]
            if self.up:
                self.image = self.walkUp[0]
            if self.down:
                self.image = self.walkDown[0]


    def move(self, dx, dy):
        self.moveDelay += 1
        if self.moveDelay >= PLAYER_SPEED and not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
            self.moveDelay = 0

    def get_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(0, -1)
            self.up = True
            self.down = False
            self.left = False
            self.right = False
        if keys[pygame.K_s]:
            self.move(0, 1)
            self.up = False
            self.down = True
            self.left = False
            self.right = False
        if keys[pygame.K_a]:
            self.move(-1, 0)
            self.up = False
            self.down = False
            self.left = True
            self.right = False
        if keys[pygame.K_d]:
            self.move(1, 0)
            self.up = False
            self.down = False
            self.left = False
            self.right = True
        else:
            self.standing = True
            self.walkCount = 0

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if (
                wall.rect.x == self.rect.x + dx * TILESIZE
                and wall.rect.y == self.rect.y + dy * TILESIZE
            ):
                self.rect.centery -= PLAYER_WIDTH / 2
                return True
    
    def collide_etc(self):
        if pygame.sprite.spritecollideany(self, self.game.mobs):
           self.health -= 1
        if self.health <= 0:
            self.game.quit()
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, velx, vely):
        self.groups = game.all_sprites, game.Bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE / 2, TILESIZE / 2))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.kill_timer = 0

    def update(self):
        # self.collision()
        self.collision_else()
        if not self.collision_else():
            self.x += self.velx  # * self.game.dt
            self.y += self.vely  # * self.game.dt
        self.rect.center = self.x, self.y
        if pygame.sprite.spritecollideany(self, self.game.walls):
            for x in range(random.randint(PARTICLELIMIT/2, PARTICLELIMIT)):
                Particle(self.game, self.x + random.randint(-10, 10), self.y + random.randint(-10,10), [LIGHTBROWN, YELLOW])
            self.kill()
        
        
    def collision_else(self):
        if pygame.sprite.spritecollideany(self, self.game.mobs):
            for x in range(random.randint(PARTICLELIMIT/2, PARTICLELIMIT)):
                Particle(self.game, self.x + random.randint(-10, 10), self.y + random.randint(-10,10), [YELLOW,RED,WHITE])
            self.kill()
            return True
        else:
            return False