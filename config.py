import pygame
pygame.mixer.init()
# window config
win_width = 1080
win_length = 640
# fonts``
textFont1 = "gunmetl.ttf"
textFont2 = "VCR_OSD_MONO_1.001.ttf"
# background
bgs = ["parallax-space-backgound.png",
        "underwater-fantasy.png",
        "parallax-mountain.png"]
curbg = 0
# characters
CHARACTERS = 3
# players
NUMOFPLAYERS = 2
# battle stage size
stage_width = win_width*2.4//4
stage_thickness = win_length/15
stage_edge_space = 100
# acceleration
a = 0.4
max_vel = 2
delay = 60
# bullet
max_bullet = 4
# rounds
Round = 3
numwin = 2
# lives
lives = 1
# max defend time
max_defend = 60
# bgm
menu = "./bgm/Battle-on-the-Plains_loop.ogg"    #"./bgm/agilis.ogg"
battle = "./bgm/8bitMusic1_loop.ogg"
nextround = "./bgm/Solitary-Dance.ogg"
finish = "./bgm/win2.ogg"
# se
click_button = pygame.mixer.Sound("./se/click_button.ogg")
move_button = pygame.mixer.Sound("./se/move_button.ogg")
damage = pygame.mixer.Sound("./se/damaged.ogg")
esc = pygame.mixer.Sound("./se/esc.ogg")