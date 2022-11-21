import draw
import config
import pygame
import player
Scene = "Battle"
Player1 = 2
Player2 = 3
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
        draw.generateText("Just brawl", self.Title_size, (config.win_width/2, 200),config.textFont1)
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
        draw.generateText("Player 1:", self.text_size, (config.win_width/4, config.win_length/5), config.textFont1)
        draw.generateText("Player 2:", self.text_size, (config.win_width/4*3, config.win_length/5), config.textFont1)
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
        global Player1, Player2
        Player1 = self.p1_character
        Player2 = self.p2_character
        for button in self.buttons:
            if button.clicked:
                button.draw_clicked("Ready")
            else:
                button.draw()

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
        draw.generateText(self.text, self.text_size, self.pos, config.textFont1, color=(0,0,0))
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
class Battle(Scene_base):
        
    def __init__(self):
        super().__init__()
        self.stageRect = pygame.Rect(config.win_width/2-config.stage_width/2,config.win_length/4*3-config.stage_thickness/2,config.stage_width,config.stage_thickness)
        self.p1 = player.P(Player1)
        self.p2 = player.P(Player2)
        self.players = player.Players(self.p1, self.p2)
        self.setBattle()
    def generate(self):
        draw.draw_block((config.win_width/2, config.win_length/4*3),config.stage_width,config.stage_thickness,(159,159,150))
        for pl in self.players.players:
            draw.draw_sprite(pl.image, pl.rect)
            if pl.rect.top>config.win_length:
                pl.lives -= 1
                pl.reset()
    def setBattle(self):
        space  =  (config.stage_width-2*config.stage_edge_space)/(config.NUMOFPLAYERS-1)
        i = 0
        for pl in self.players.players:
            pl.set_pos(pygame.math.Vector2(config.win_width/6+space*i, config.win_length/4*3-config.stage_thickness/2-pl.character.size/2+1))
            pl.respon_pos = pygame.math.Vector2(pl.rect.centerx,0)
            i+=1
    def update(self):
        for pl in self.players.players:
            pl.change_pos()
        self.handle_hurt()
        self.gravity()
        self.generate()
        self.display_lives()
    def handle_hurt(self):
        if self.p1.rect.colliderect(self.p2.rect):
            if self.p1.rect.left < self.p2.rect.left:
                self.p1.hurt_by(self.p2, 1, -1)
                self.p2.hurt_by(self.p1, 0, 1)
            else:
                self.p1.hurt_by(self.p2, 1, 1)
                self.p2.hurt_by(self.p1, 0, -1)

    def gravity(self):
        for pl in self.players.players:
            if not self.collideStage(pl):
                if pl.direction.y <= config.max_vel:
                    pl.direction.y += pl.character.weight
            else:
                pl.direction.y = 0
                pl.rect.centery = self.stageRect.top-pl.character.size/2+1
        print("p1: "+str(self.p1.direction)+" p2: "+str(self.p2.direction))

    def collideStage(self, player):
        return player.rect.colliderect(self.stageRect)
    def get_buttons(self):
        pass
    def display_lives(self):
        draw.generateText("lives: "+str(self.p1.lives), 30, (self.p1.respon_pos.x-50, config.win_length/8*7), config.textFont1)
        draw.generateText("lives: "+str(self.p2.lives), 30, (self.p2.respon_pos.x+50, config.win_length/8*7), config.textFont1)
        draw.generateText(str(self.p1.percentage)+"%", self.p1.character.size-10, self.p1.rect.center, config.textFont2)
        draw.generateText(str(self.p2.percentage)+"%", self.p2.character.size-10, self.p2.rect.center, config.textFont2)
    def handle_event(self, event):
            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_a] and not keypressed[pygame.K_d]:
                self.p1.direction.x = -1
            elif keypressed[pygame.K_d] and not keypressed[pygame.K_a]:
                self.p1.direction.x = 1
            else:
                self.p1.direction.x = 0
            if keypressed[pygame.K_w]:
                print(self.p1.jump_time)
                if self.collideStage(self.p1):
                    self.p1.direction.y = -5
                    self.p1.jump_time = 0
                elif not self.collideStage(self.p1) and self.p1.jump_time < self.p1.max_jump:
                    self.p1.direction.y = -3
                    self.p1.jump_time+=1
            if keypressed[pygame.K_LEFT] and not keypressed[pygame.K_RIGHT]:
                self.p2.direction.x = -1
            elif keypressed[pygame.K_RIGHT] and not keypressed[pygame.K_LEFT]:
                self.p2.direction.x = 1
            else:
                self.p2.direction.x = 0
            if keypressed[pygame.K_UP]:
                print(self.p2.jump_time)
                if self.collideStage(self.p2):
                    self.p2.direction.y = -5
                    self.p2.jump_time = 0
                elif not self.collideStage(self.p2) and self.p2.jump_time < self.p2.max_jump:
                    self.p2.direction.y = -3
                    self.p2.jump_time+=1
            
            
