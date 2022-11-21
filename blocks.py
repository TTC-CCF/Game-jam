# import draw
import pygame
import config
class green_block(pygame.sprite.Sprite):
    def __init__(self):
        self.size = 40
        self.attack = 10
        self.weight = 0.4
        self.agility = config.win_width*0.01
        self.color = (150,255,150)
        self.jump_time = 3
        
class blue_block(pygame.sprite.Sprite):
    def __init__(self):
        self.size = 80
        self.attack = 60
        self.weight = 0.6
        self.agility = config.win_width*0.005
        self.color = (150,150,255)
        self.jump_time = 2
class red_block(pygame.sprite.Sprite):
    def __init__(self):
        self.size = 50
        self.attack = 25
        self.weight = 0.5
        self.agility = config.win_width*0.01
        self.color = (255,100,100)
        self.jump_time = 2
    