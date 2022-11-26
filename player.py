import blocks
import pygame
class P:
    
    def __init__(self, ch, i, lives):
        if ch == 1:
            self.character = blocks.red_block()
        elif ch == 2:
            self.character = blocks.green_block()
        elif ch == 3:
            self.character = blocks.blue_block()
        self.animate = [self.character.idle,
                        self.character.idler,
                        self.character.walk,
                        self.character.walkr,
                        self.character.attacks,
                        self.character.attacksr]
        self.cur_animate = 0
        self.cur_frame = 0
        self.direction = pygame.math.Vector2(0,0)
        self.respon_pos = pygame.math.Vector2(0,0)
        self.jump_time = 0
        self.max_jump = self.character.jump_time
        self.image = self.animate[self.cur_animate][self.cur_frame]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*2,self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.percentage = 0
        self.lives = lives
        self.attacking = 0
        self.bullets = []
        self.identify = i
        self.dir = 1 if i == 1 else -1
    def _animate(self):
        self.get_status()
        self.cur_frame+=0.1

        if self.cur_frame >= len(self.animate[self.cur_animate]):
            if self.attacking:
                self.attacking = 0
            self.cur_frame = 0
        self.image = self.animate[self.cur_animate][int(self.cur_frame)]  
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*2,self.image.get_height()*2))
    def set_pos(self, pos):
        self.rect.center = pos
        
    def change_pos(self):
        self.rect.center += self.direction*self.character.agility
    
    def reset(self):
        self.rect.center = self.respon_pos
        self.percentage = 0

    def get_status(self):
        if self.attacking:
            self.cur_animate = 4 if self.dir == 1 else 5
        elif self.direction.x != 0:
            self.cur_animate = 2 if self.dir == 1 else 3
        else:
            self.cur_animate = 0 if self.dir == 1 else 1
        
    def hurt_by(self, other, dir):
        self.percentage += other.character.attack
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
        self.speed = 20
        self.id = id
    def change_pos(self):
        self.rect.x += self.direction*self.speed
