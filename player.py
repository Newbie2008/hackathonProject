import random
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

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.weapon = 'bullet'
        self.moveDelay = 0
        self.Battling = False

    def update(self):
        self.collide_etc()
        self.get_keys()
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE

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