import blocks
import pygame
class P:
    
    def __init__(self, ch, i):
        if ch == 1:
            self.character = blocks.red_block()
        elif ch == 2:
            self.character = blocks.green_block()
        elif ch == 3:
            self.character = blocks.blue_block()
        self.direction = pygame.math.Vector2(0,0)
        self.respon_pos = pygame.math.Vector2(0,0)
        self.jump_time = 0
        self.max_jump = self.character.jump_time
        self.image = pygame.Surface([self.character.size, self.character.size])
        self.image.fill(self.character.color)
        self.rect = self.image.get_rect()
        self.percentage = 0
        self.touch_by = -1
        self.lives = 3
        self.bullets = []
        self.identify = i
        self.dir = 1
    
    def set_pos(self, pos):
        self.rect.center = pos
        
    def change_pos(self):
        self.rect.center += self.direction*self.character.agility
    
    def reset(self):
        self.rect.center = self.respon_pos
        self.touch_by = -1
        self.percentage = 0

    def hurt_by(self, other, dir):
        self.percentage += other.character.attack
        self.touch_by = other
        self.rect.centerx += dir*(self.percentage+1)        
        

class Players:
    def __init__(self, p1, p2):
        self.players = [p1,p2]

class bullet(pygame.sprite.Sprite):
    def __init__(self, pos, dir, id):
        self.size = 10
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(id.character.color)
        self.rect = self.image.get_rect()
        if dir == 1:
            self.rect.midleft = (pos[0]+id.character.size/2,pos[1])
        else:
            self.rect.midright = (pos[0]-id.character.size/2,pos[1])
        self.direction = dir
        self.speed = 5
        self.id = id
    def change_pos(self):
        self.rect.x += self.direction*self.speed
