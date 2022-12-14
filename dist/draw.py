import pygame
import config as cf
import scene
screen = pygame.display.set_mode((cf.win_width, cf.win_length))
background = pygame.image.load(cf.bgs[cf.curbg])
background = pygame.transform.scale(background,(cf.win_width,cf.win_length))

class button:

    def __init__(self, text, pos, size):
        self.clicked = False
        self.hover = False
        self.pos = pos
        self.text = text
        self.size = size
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
    def draw_clicked(self, change_text):
        self.set_text(change_text)
        screen.blit(self.rend, self.rect)
    def set_rend(self):
        self.rend = pygame.font.Font(cf.textFont1, self.size).render(self.text, True, self.get_color())
    def set_text(self, change_text):
        self.rend = pygame.font.Font(cf.textFont1, self.size).render(change_text, True, (255,255,255))
    def get_color(self):
        if self.hover:
            return (255,255,255)
        else:
            return (150,150,150)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.center = self.pos

def changeBG(bg):
    global background
    background = pygame.image.load(bg)
    background = pygame.transform.scale(background,(cf.win_width,cf.win_length))

def showPicture(pic,topleft):
    screen.blit(pic,topleft)
    
def update(phase):
    screen.blit(background,(0,0))
    phase.update()
    pygame.display.flip()

def draw_block(pos, wid, len, color):
    _rect = pygame.Rect(0,0,wid, len)
    _rect.center = pos
    pygame.draw.rect(screen, color, _rect)
    return _rect

def draw_block_wline(pos, wid, len, color, l):
    _rect = pygame.Rect(0,0,wid, len)
    _rect.center = pos     
    pygame.draw.rect(screen, color, _rect, l)
    return _rect

def generateText(str, size, pos, _font,color = (255,255,255)):
    fonts = pygame.font.Font(_font, size)
    text = fonts.render(str, True, color)
    textRect = text.get_rect()
    textRect.center = pos
    screen.blit(text, textRect)
    return textRect
def draw_tri(color, vertices):
    pygame.draw.polygon(screen, color, vertices)

def draw_tri_wline(color, vertices, l):
    pygame.draw.polygon(screen, color, vertices, l)

def draw_sprite(sur, topleft):
    screen.blit(sur,topleft)

def draw_scene(Scene):
    s = scene.Scene_base()
    if Scene == "menu":
        s = scene.Menu()
    elif Scene == "Option":
        s = scene.Option()
    elif Scene == "ChooseCharacters":
        s = scene.Choose()
    elif Scene == "Ready":
        s = scene.Ready()
    elif Scene == "Battle":
        s = scene.Battle()
    elif Scene == "nextround":
        s = scene.NextRound()
    elif Scene == "finish":
        s = scene.Finish()
    s.generate()
    return s