import blocks
import pygame
class P:
    
    def __init__(self, ch):
        if ch == 1:
            self.character = blocks.red_block()
        elif ch == 2:
            self.character = blocks.green_block()
        elif ch == 3:
            self.character = blocks.blue_block()
        self.direction = pygame.math.Vector2(0,0)
        # self.top_left = pygame.math.Vector2(0,0)
        self.respon_pos = pygame.math.Vector2(0,0)
        self.jump_time = 0
        self.max_jump = self.character.jump_time
        self.image = pygame.Surface([self.character.size, self.character.size])
        self.image.fill(self.character.color)
        self.rect = self.image.get_rect()
        self.percentage = 0
        self.touch_by = -1
        self.lives = 3
    
    def set_pos(self, pos):
        self.rect.center = pos
        
    def change_pos(self):
        self.rect.center += self.direction*self.character.agility
    
    def reset(self):
        self.rect.center = self.respon_pos
        self.touch_by = -1
        self.percentage = 0

    def hurt_by(self, other, id, dir):
        self.percentage += other.character.attack
        self.touch_by = id
        self.rect.centerx += dir*(self.percentage+1)

        
class Players:
    def __init__(self, p1, p2):
        self.players = [p1,p2]

