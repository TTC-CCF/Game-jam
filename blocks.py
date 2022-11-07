import draw
import pygame
import config
class base:
    def __init__(self, size, attack, weight, position):
        self.size = size
        self.attack = attack
        self.weight = weight
        self.position = position
    

class green_block(base):
    def __init__(self, size, attack, weight, position):
        super().__init__(size, attack, weight, position)
    

class blue_block(base):
    def __init__(self, size, attack, weight, position):
        super().__init__(size, attack, weight, position)  

        
class red_block(base):
    def __init__(self, size, attack, weight, position):
        super().__init__(size, attack, weight, position)

    