# import draw
import pygame
import config
class littleboy(pygame.sprite.Sprite):
    def __init__(self):
        self.attack_se = pygame.mixer.Sound("./se/littleboy_attack.ogg")
        self.jump_se = pygame.mixer.Sound("./se/littleboy_jump.ogg")
        
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
        self.jumpr = [pygame.image.load("./character1/jumpr1.png"),
                    pygame.image.load("./character1/jumpr2.png"),
                    pygame.image.load("./character1/jumpr3.png")]
        
        self.attacks = [pygame.image.load("./character1/attack1.png"),
                    pygame.image.load("./character1/attack2.png"),
                    pygame.image.load("./character1/attack3.png"),
                    pygame.image.load("./character1/attack4.png")]
        self.attacksr = [pygame.image.load("./character1/attackr1.png"),
                    pygame.image.load("./character1/attackr2.png"),
                    pygame.image.load("./character1/attackr3.png"),
                    pygame.image.load("./character1/attackr4.png")]
        
        self.defend = [pygame.image.load("./character1/defend1.png"),
                    pygame.image.load("./character1/defend2.png"),
                    pygame.image.load("./character1/defend3.png"),
                    pygame.image.load("./character1/defend4.png"),]
        self.defendr = [pygame.image.load("./character1/defendr1.png"),
                    pygame.image.load("./character1/defendr2.png"),
                    pygame.image.load("./character1/defendr3.png"),
                    pygame.image.load("./character1/defendr4.png"),]
        self.special = [pygame.image.load("./character1/special1.png"),
                    pygame.image.load("./character1/special2.png"),
                    pygame.image.load("./character1/special3.png"),
                    pygame.image.load("./character1/special4.png"),
                    pygame.image.load("./character1/special5.png"),
                    pygame.image.load("./character1/special6.png"),]
        self.job = 1
        self.attack = 10
        self.weight = 0.4
        self.agility = config.win_width*0.005
        self.color = (150,150,150)
        self.jump_time = 8
        self.bullet_speed = 15
        self.bullet_w = 10
        self.jump_height = 6
        self.bullet_l = 10
class warrior(pygame.sprite.Sprite):
    def __init__(self):
        self.attack_se = pygame.mixer.Sound("./se/warrior_attack.ogg")
        self.jump_se = pygame.mixer.Sound("./se/warrior_jump.ogg")
        
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
        self.jumpr = [pygame.image.load("./character2/jumpr1.png"),
                    pygame.image.load("./character2/jumpr2.png"),
                    pygame.image.load("./character2/jumpr3.png")]
        
        self.attacks = [pygame.image.load("./character2/attack1.png"),
                    pygame.image.load("./character2/attack2.png"),
                    pygame.image.load("./character2/attack3.png"),
                    pygame.image.load("./character2/attack4.png")]
        self.attacksr = [pygame.image.load("./character2/attackr1.png"),
                    pygame.image.load("./character2/attackr2.png"),
                    pygame.image.load("./character2/attackr3.png"),
                    pygame.image.load("./character2/attackr4.png")]
        
        self.defend = [pygame.image.load("./character2/defend1.png"),
                    pygame.image.load("./character2/defend2.png"),
                    pygame.image.load("./character2/defend3.png"),
                    pygame.image.load("./character2/defend4.png"),]
        self.defendr = [pygame.image.load("./character2/defendr1.png"),
                    pygame.image.load("./character2/defendr2.png"),
                    pygame.image.load("./character2/defendr3.png"),
                    pygame.image.load("./character2/defendr4.png"),]
        
        self.special = [pygame.image.load("./character2/special1.png"),
                    pygame.image.load("./character2/special2.png"),
                    pygame.image.load("./character2/special3.png"),
                    pygame.image.load("./character2/special4.png"),
                    pygame.image.load("./character2/special5.png"),
                    pygame.image.load("./character2/special6.png"),]
        
        self.job = 2
        self.attack = 5
        self.weight = 0.6
        self.agility = config.win_width*0.003
        self.color = (255,255,255,0)
        self.jump_time = 2
        self.jump_height = 4

class wizard(pygame.sprite.Sprite):
    def __init__(self):
        self.attack_se = pygame.mixer.Sound("./se/wizard_attack.ogg")
        self.jump_se = pygame.mixer.Sound("./se/wizard_jump.ogg")
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
        self.jumpr = [pygame.image.load("./character3/jumpr1.png"),
                    pygame.image.load("./character3/jumpr2.png"),
                    pygame.image.load("./character3/jumpr3.png")]
        
        self.attacks = [pygame.image.load("./character3/attack1.png"),
                    pygame.image.load("./character3/attack2.png"),
                    pygame.image.load("./character3/attack3.png"),
                    pygame.image.load("./character3/attack4.png")]
        self.attacksr = [pygame.image.load("./character3/attackr1.png"),
                    pygame.image.load("./character3/attackr2.png"),
                    pygame.image.load("./character3/attackr3.png"),
                    pygame.image.load("./character3/attackr4.png")]
        
        self.defend = [pygame.image.load("./character3/defend1.png"),
                    pygame.image.load("./character3/defend2.png"),
                    pygame.image.load("./character3/defend3.png"),
                    pygame.image.load("./character3/defend4.png"),]
        self.defendr = [pygame.image.load("./character3/defendr1.png"),
                    pygame.image.load("./character3/defendr2.png"),
                    pygame.image.load("./character3/defendr3.png"),
                    pygame.image.load("./character3/defendr4.png"),]
        
        self.special = [pygame.image.load("./character3/special1.png"),
                    pygame.image.load("./character3/special2.png"),
                    pygame.image.load("./character3/special3.png"),
                    pygame.image.load("./character3/special4.png"),
                    pygame.image.load("./character3/special5.png"),
                    pygame.image.load("./character3/special6.png"),]
        self.job = 1
        self.attack = 16
        self.weight = 0.4
        self.agility = config.win_width*0.003
        self.color = (252, 102, 3)
        self.jump_time = 2
        self.bullet_speed = 20
        self.bullet_w = 13
        self.bullet_l = 13
        self.jump_height = 5

