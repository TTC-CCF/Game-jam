import blocks
import config
import pygame
class P:
    
    def __init__(self, ch, i, lives):
        if ch == 1:
            self.character = blocks.wizard()
        elif ch == 2:
            self.character = blocks.warrior()
        elif ch == 3:
            self.character = blocks.littleboy()
        self.animate = [self.character.idle,
                        self.character.idler,
                        self.character.walk,
                        self.character.walkr,
                        self.character.attacks,
                        self.character.attacksr,
                        self.character.jump,
                        self.character.jumpr,
                        self.character.defend,
                        self.character.defendr]
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
        self.jumping = 0
        self.bullets = []
        self.identify = i
        self.dir = 1 if i == 1 else -1
        self.defend = 0
        self.defend_time = 0
        self.die = 0
        self.da = 0

    def _animate(self):
        self.get_status()
        self.cur_frame+=0.15

        if self.cur_frame >= len(self.animate[self.cur_animate]):
            if self.attacking:
                self.attacking = 0
            if self.jumping:
                self.jumping = 0
            self.cur_frame = 0
            if self.defend:
                self.cur_frame = len(self.animate[self.cur_animate])-1

        self.image = self.animate[self.cur_animate][int(self.cur_frame)]  
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*2,self.image.get_height()*2))
    def set_pos(self, pos):
        self.rect.center = pos
        
    def change_pos(self):
        self.rect.center += self.direction*self.character.agility
    
    def reset(self):
        self.rect.center = self.respon_pos
        self.percentage = 0
        self.die = 0

    def get_status(self):
        if self.defend:
            if not self.da:
                self.cur_frame = 0
                self.da = 1
            self.cur_animate = 8 if self.dir == 1 else 9
        elif self.attacking:
            self.cur_animate = 4 if self.dir == 1 else 5
        elif self.jumping:
            self.cur_animate = 6 if self.dir == 1 else 7
        elif self.direction.x != 0:
            self.cur_animate = 2 if self.dir == 1 else 3
        else:
            self.cur_animate = 0 if self.dir == 1 else 1
        
    def hurt_by(self, other, dir):
        pygame.mixer.Sound.play(config.damage)
        self.percentage += other.character.attack
        self.rect.centerx += dir*(self.percentage+1)        
        

class Players:
    def __init__(self, p1, p2):
        self.players = [p1,p2]

class bullet(pygame.sprite.Sprite):
    def __init__(self, pos, dir, id):
        self.w = id.character.bullet_w
        self.l = id.character.bullet_l
        self.image = pygame.Surface([self.w, self.l])
        self.image.fill(id.character.color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = dir
        self.speed = id.character.bullet_speed
        self.id = id
    def change_pos(self):
        self.rect.x += self.direction*self.speed
