# import draw
import pygame
import config
class green_block(pygame.sprite.Sprite):
    def __init__(self):
        self.walk = [pygame.image.load("./character1/walk1.png"),
                    pygame.image.load("./character1/walk2.png"),
                    pygame.image.load("./character1/walk3.png"),
                    pygame.image.load("./character1/walk4.png"),
                    pygame.image.load("./character1/walk5.png"),
                    pygame.image.load("./character1/walk6.png")]
        self.walkr = [pygame.image.load("./character1/walkr1.png"),
                    pygame.image.load("./character1/walkr2.png"),
                    pygame.image.load("./character1/walkr3.png"),
                    pygame.image.load("./character1/walkr4.png"),
                    pygame.image.load("./character1/walkr5.png"),
                    pygame.image.load("./character1/walkr6.png")]
        
        self.idle = [pygame.image.load("./character1/idle1.png"),
                    pygame.image.load("./character1/idle2.png"),
                    pygame.image.load("./character1/idle3.png"),
                    pygame.image.load("./character1/idle4.png")]
        self.idler = [pygame.image.load("./character1/idler1.png"),
                    pygame.image.load("./character1/idler2.png"),
                    pygame.image.load("./character1/idler3.png"),
                    pygame.image.load("./character1/idler4.png")]
        
        self.jump = [pygame.image.load("./character1/jump1.png"),
                    pygame.image.load("./character1/jump2.png"),
                    pygame.image.load("./character1/jump3.png")]
        self.attacks = [pygame.image.load("./character1/attack1.png"),
                    pygame.image.load("./character1/attack2.png"),
                    pygame.image.load("./character1/attack3.png"),
                    pygame.image.load("./character1/attack4.png")]
        self.attacksr = [pygame.image.load("./character1/attackr1.png"),
                    pygame.image.load("./character1/attackr2.png"),
                    pygame.image.load("./character1/attackr3.png"),
                    pygame.image.load("./character1/attackr4.png")]
        
        self.size = 50
        self.attack = 10
        self.weight = 0.4
        self.agility = config.win_width*0.003
        self.color = (150,255,150)
        self.jump_time = 3
        
class blue_block(pygame.sprite.Sprite):
    def __init__(self):
        self.walk = [pygame.image.load("./character2/walk1.png"),
                    pygame.image.load("./character2/walk2.png"),
                    pygame.image.load("./character2/walk3.png"),
                    pygame.image.load("./character2/walk4.png"),
                    pygame.image.load("./character2/walk5.png"),
                    pygame.image.load("./character2/walk6.png")]
        self.walkr = [pygame.image.load("./character2/walkr1.png"),
                    pygame.image.load("./character2/walkr2.png"),
                    pygame.image.load("./character2/walkr3.png"),
                    pygame.image.load("./character2/walkr4.png"),
                    pygame.image.load("./character2/walkr5.png"),
                    pygame.image.load("./character2/walkr6.png")]
        
        self.idle = [pygame.image.load("./character2/idle1.png"),
                    pygame.image.load("./character2/idle2.png"),
                    pygame.image.load("./character2/idle3.png"),
                    pygame.image.load("./character2/idle4.png")]
        self.idler = [pygame.image.load("./character2/idler1.png"),
                    pygame.image.load("./character2/idler2.png"),
                    pygame.image.load("./character2/idler3.png"),
                    pygame.image.load("./character2/idler4.png")]
        
        self.jump = [pygame.image.load("./character2/jump1.png"),
                    pygame.image.load("./character2/jump2.png"),
                    pygame.image.load("./character2/jump3.png")]
        self.attacks = [pygame.image.load("./character2/attack1.png"),
                    pygame.image.load("./character2/attack2.png"),
                    pygame.image.load("./character2/attack3.png"),
                    pygame.image.load("./character2/attack4.png")]
        self.attacksr = [pygame.image.load("./character2/attackr1.png"),
                    pygame.image.load("./character2/attackr2.png"),
                    pygame.image.load("./character2/attackr3.png"),
                    pygame.image.load("./character2/attackr4.png")]
        
        self.size = 80
        self.attack = 60
        self.weight = 0.4
        self.agility = config.win_width*0.003
        self.color = (150,150,255)
        self.jump_time = 2
class red_block(pygame.sprite.Sprite):
    def __init__(self):
        self.walk = [pygame.image.load("./character3/walk1.png"),
                    pygame.image.load("./character3/walk2.png"),
                    pygame.image.load("./character3/walk3.png"),
                    pygame.image.load("./character3/walk4.png"),
                    pygame.image.load("./character3/walk5.png"),
                    pygame.image.load("./character3/walk6.png")]
        self.walkr = [pygame.image.load("./character3/walkr1.png"),
                    pygame.image.load("./character3/walkr2.png"),
                    pygame.image.load("./character3/walkr3.png"),
                    pygame.image.load("./character3/walkr4.png"),
                    pygame.image.load("./character3/walkr5.png"),
                    pygame.image.load("./character3/walkr6.png")]
    
        self.idle = [pygame.image.load("./character3/idle1.png"),
                    pygame.image.load("./character3/idle2.png"),
                    pygame.image.load("./character3/idle3.png"),
                    pygame.image.load("./character3/idle4.png")]
        self.idler = [pygame.image.load("./character3/idler1.png"),
                    pygame.image.load("./character3/idler2.png"),
                    pygame.image.load("./character3/idler3.png"),
                    pygame.image.load("./character3/idler4.png")]
        
        self.jump = [pygame.image.load("./character3/jump1.png"),
                    pygame.image.load("./character3/jump2.png"),
                    pygame.image.load("./character3/jump3.png")]
        self.attacks = [pygame.image.load("./character3/attack1.png"),
                    pygame.image.load("./character3/attack2.png"),
                    pygame.image.load("./character3/attack3.png"),
                    pygame.image.load("./character3/attack4.png")]
        self.attacksr = [pygame.image.load("./character3/attackr1.png"),
                    pygame.image.load("./character3/attackr2.png"),
                    pygame.image.load("./character3/attackr3.png"),
                    pygame.image.load("./character3/attackr4.png")]
        
        self.size = 65
        self.attack = 25
        self.weight = 0.4
        self.agility = config.win_width*0.003
        self.color = (255,100,100)
        self.jump_time = 2

