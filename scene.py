import draw
import config
import pygame
import player
Scene = "menu"

def next_phase(button):
    global Scene
    if Scene == "menu":
        if button.text == "Start":
            Scene = "ChooseCharacters"
        elif button.text == "Quit":
            pygame.event.post(pygame.event.Event(pygame.QUIT))
    elif Scene == "ChooseCharacters":
        Scene = "Ready"
    elif Scene == "Ready":
        Scene = "Battle"
class Scene_base:
    def __init__(self):
        self.buttons = []
    def generate(self):
        pass
    def update(self):
        self.generate()
    def get_buttons(self):
        return self.buttons
    def handle_event(self, event):
        pass

class Menu(Scene_base):
    def __init__(self):
        self.wid = 200
        self.len = 50
        self.Title_size = 180
        self.Sblock_x = config.win_width/2
        self.Sblock_y = config.win_length/2+100
        self.Qblock_x = config.win_width/2
        self.Qblock_y = self.Sblock_y+self.len+10

    def generate(self):
        draw.generateText("Just brawl", self.Title_size, (config.win_width/2, 200), (255,255,255))
        self.buttons = [draw.button("Start",(self.Sblock_x, self.Sblock_y), self.len),
                        draw.button("Quit", (self.Qblock_x, self.Qblock_y), self.len)]
    def hover_button(self):
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.hover = True
            else:
                button.hover = False
            button.draw()

    def update(self):
        self.generate()
        self.hover_button()
    
    def get_buttons(self):
        return self.buttons
    def handle_event(self, event):
        changeScene = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.hover:
                    next_phase(button)
                    changeScene = True
        return changeScene
        

class Choose(Scene_base):
    def __init__(self):
        self.text_size = 70
        self.buttons = []
        self.p1_character = 1
        self.p2_character = 2
        self.buttons = [draw.button("Press E to Ready", (config.win_width/4, config.win_length/5+self.text_size+330), 30),
                        draw.button("Press 1 to Ready", (config.win_width/4*3, config.win_length/5+self.text_size+330), 30)]
    def generate(self):
        draw.generateText("Player 1:", self.text_size, (config.win_width/4, config.win_length/5), (255,255,255))
        draw.generateText("Player 2:", self.text_size, (config.win_width/4*3, config.win_length/5), (255,255,255))
        draw.draw_block_wline((config.win_width/4, config.win_length/5+self.text_size+140), 250, 300, (255,255,255), 3)
        draw.draw_tri_wline((200,200,200), [(config.win_width/4-155, config.win_length/5+self.text_size+140), (config.win_width/4-130,config.win_length/5+self.text_size+130), (config.win_width/4-130,config.win_length/5+self.text_size+150)],2)
        draw.draw_tri_wline((200,200,200), [(config.win_width/4+155, config.win_length/5+self.text_size+140), (config.win_width/4+130,config.win_length/5+self.text_size+130), (config.win_width/4+130,config.win_length/5+self.text_size+150)],2)
        draw.draw_block_wline((config.win_width/4*3, config.win_length/5+self.text_size+140), 250, 300, (255,255,255), 3)
        draw.draw_tri_wline((200,200,200), [(config.win_width/4*3-155, config.win_length/5+self.text_size+140), (config.win_width/4*3-130,config.win_length/5+self.text_size+130), (config.win_width/4*3-130,config.win_length/5+self.text_size+150)],2)
        draw.draw_tri_wline((200,200,200), [(config.win_width/4*3+155, config.win_length/5+self.text_size+140), (config.win_width/4*3+130,config.win_length/5+self.text_size+130), (config.win_width/4*3+130,config.win_length/5+self.text_size+150)],2)
        self.display_character()
        
    def clicked_button(self):
        return self.buttons[0].clicked and self.buttons[1].clicked
            
    def update(self):
        self.generate()
        for button in self.buttons:
            if button.clicked:
                button.draw_clicked("Ready")
            else:
                button.draw()
        # print(self.buttons[0].clicked, self.buttons[1].clicked)

    def display_character(self):
        if self.p1_character == 1:
            color1 = (255,0,0)
        elif self.p1_character == 2:
            color1 = (0,255,0)
        elif self.p1_character == 3:
            color1 = (0,0,255)
        if self.p2_character == 1:
            color2 = (255,0,0)
        elif self.p2_character == 2:
            color2 = (0,255,0)
        elif self.p2_character == 3:
            color2 = (0,0,255)
        draw.draw_block((config.win_width/4,config.win_length/5+self.text_size+140), 180, 180, color1)
        draw.draw_block((config.win_width/4*3,config.win_length/5+self.text_size+140), 180, 180, color2)

    def hover_buttons(self):
        pass
    
    def get_buttons(self):
        return self.buttons
    def handle_event(self, event):
        changeScene = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.change_character(-1, 1)
            if event.key == pygame.K_d:
                self.change_character(1, 1)
            if event.key == pygame.K_LEFT:
                self.change_character(-1, 2)
            if event.key == pygame.K_RIGHT:
                self.change_character(1, 2)
            if event.key == pygame.K_e:
                self.buttons[0].clicked = not self.buttons[0].clicked
            if event.key == pygame.K_KP_1 or event.key == pygame.K_1:
                self.buttons[1].clicked = not self.buttons[1].clicked
        if self.clicked_button():
            changeScene = True
            next_phase(self.buttons[1])
        return changeScene
            
    def change_character(self, lor, p1op2):
        if p1op2 == 1:
            if self.p1_character == 3 and lor == 1:
                self.p1_character = 1
            elif self.p1_character == 1 and lor == -1:
                self.p1_character = 3
            else:
                self.p1_character += lor
        else:
            if self.p2_character == 3 and lor == 1:
                self.p2_character = 1
            elif self.p2_character == 1 and lor == -1:
                self.p2_character = 3
            else:
                self.p2_character += lor
class Ready(Scene_base):
    def __init__(self):
        super().__init__()
        self.pos = (config.win_width/2, config.win_length/2)
        self.wid = config.win_width-200
        self.len = config.win_length//3
        self.text = "Press Enter to Brawl!"
        self.text_size = self.len-150
    def generate(self):
        draw.draw_block_wline(self.pos, self.wid, self.len, (255,255,255), 3)
        draw.draw_block(self.pos, self.wid-200, self.len-100, (255,255,0))
        draw.generateText(self.text, self.text_size, self.pos, (0,0,0))
    def update(self):
        super().update()
    def get_buttons(self):
        super().get_buttons
    def handle_event(self, event):
        changeScene = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                changeScene = True
                next_phase(self.buttons)
        return changeScene