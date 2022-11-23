import draw
import config
import pygame
import player
Scene = "menu"
Player1 = 2
Player2 = 3
win = None
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
    elif Scene == "Battle":
        Scene = "finish"
    elif Scene == "finish":
        Scene = "ChooseCharacters"
class Scene_base:
    def __init__(self):
        self.buttons = []
    def generate(self):
        pass
    def update(self):
        self.generate()
    def get_buttons(self):
        return self.buttons
    def handle_event(self):
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
        self.hover_but = 0
        self.buttons = [draw.button("Start",(self.Sblock_x, self.Sblock_y), self.len),
                        draw.button("Quit", (self.Qblock_x, self.Qblock_y), self.len)]

    def generate(self):
        draw.generateText("Just brawl", self.Title_size, (config.win_width/2, 200),config.textFont1)
        
    def draw_button(self):
        for button in self.buttons:
            button.draw()

    def update(self):
        self.generate()
        self.draw_button()
    
    def get_buttons(self):
        return self.buttons
    
    def handle_event(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_UP]:
            self.buttons[self.hover_but].hover = False
            if self.hover_but == 0:
                self.hover_but = len(self.buttons)-1
            else:
                self.hover_but -= 1
        if keypress[pygame.K_DOWN]:
            self.buttons[self.hover_but].hover = False
            if self.hover_but == len(self.buttons)-1:
                self.hover_but = 0
            else:
                self.hover_but += 1
        self.buttons[self.hover_but].hover = True
        if keypress[pygame.K_RETURN] or keypress[pygame.K_KP_ENTER]:
            next_phase(self.buttons[self.hover_but])
            return True
        

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
    def handle_event(self):
        changeScene = False
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_a]:
            self.change_character(-1, 1)
        if keypress[pygame.K_d]:
            self.change_character(1, 1)
        if keypress[pygame.K_LEFT]:
            self.change_character(-1, 2)
        if keypress[pygame.K_RIGHT]:
            self.change_character(1, 2)
        if keypress[pygame.K_e]:
            self.buttons[0].clicked = not self.buttons[0].clicked
        if keypress[pygame.K_1] or keypress[pygame.K_KP_1]:
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
    def handle_event(self):
        changeScene = False
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_RETURN] or keypress[pygame.K_KP_ENTER]:
            changeScene = True
            next_phase(self.buttons)
        return changeScene
class Battle(Scene_base):
        
    def __init__(self):
        super().__init__()
        self.stageRect = pygame.Rect(config.win_width/2-config.stage_width/2,config.win_length/4*3-config.stage_thickness/2,config.stage_width,config.stage_thickness)
        self.p1 = player.P(Player1, 1)
        self.p2 = player.P(Player2, 2)
        self.players = player.Players(self.p1, self.p2)
        self.setBattle()
        self.clicked = [1,1]
    def generate(self):
        draw.draw_block((config.win_width/2, config.win_length/4*3),config.stage_width,config.stage_thickness,(159,159,150))
        for pl in self.players.players:
            draw.draw_sprite(pl.image, pl.rect)
            for b in pl.bullets:
                draw.draw_sprite(b.image,b.rect)
                
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
        self.handle_bullet()
        self.gravity()
        self.generate()
        self.display_lives()
    def handle_bullet(self):
        for pl in self.players.players:
            for b in pl.bullets:
                b.change_pos()
                if b.direction == 1 and b.rect.centerx > config.win_width:
                    pl.bullets.remove(b)
                elif b.direction == -1 and b.rect.centerx < 0:
                    pl.bullets.remove(b)
                for p in self.players.players:
                    if p.rect.colliderect(b.rect):
                        if p.rect.left < b.id.rect.left:
                            p.hurt_by(b.id, -1)
                        else:
                            p.hurt_by(b.id, 1)
                        pl.bullets.remove(b)

    def gravity(self):
        for pl in self.players.players:
            if not self.collideStage(pl):
                if pl.direction.y <= config.max_vel:
                    pl.direction.y += pl.character.weight
            else:
                pl.direction.y = 0
                pl.rect.centery = self.stageRect.top-pl.character.size/2+1

            if pl.rect.top>config.win_length:
                pl.lives -= 1
                pl.reset()

        # print("p1: "+str(self.p1.direction)+" p2: "+str(self.p2.direction))

    def collideStage(self, player):
        return player.rect.colliderect(self.stageRect)
    def get_buttons(self):
        pass
    def display_lives(self):
        draw.generateText("lives: "+str(self.p1.lives), 30, (self.p1.respon_pos.x-50, config.win_length/8*7), config.textFont1)
        draw.generateText("lives: "+str(self.p2.lives), 30, (self.p2.respon_pos.x+50, config.win_length/8*7), config.textFont1)
        draw.generateText(str(self.p1.percentage)+"%", self.p1.character.size-10, self.p1.rect.center, config.textFont2)
        draw.generateText(str(self.p2.percentage)+"%", self.p2.character.size-10, self.p2.rect.center, config.textFont2)
    def handle_event(self):
            global win
            if self.p1.lives == 0:
                win = self.p2
                next_phase(self.buttons)
                return True
            if self.p2.lives == 0:
                win = self.p1
                next_phase(self.buttons)
                return True
            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_a] and not keypressed[pygame.K_d]:
                self.p1.direction.x = -1
                self.p1.dir = -1
            elif keypressed[pygame.K_d] and not keypressed[pygame.K_a]:
                self.p1.direction.x = 1
                self.p1.dir = 1
            else:
                self.p1.direction.x = 0
            if keypressed[pygame.K_w]:
                if self.collideStage(self.p1):
                    self.p1.direction.y = -5
                    self.p1.jump_time = 0
                elif not self.collideStage(self.p1) and self.p1.jump_time < self.p1.max_jump:
                    self.p1.direction.y = -3
                    self.p1.jump_time+=1
            if keypressed[pygame.K_r] and not self.clicked[0]:
                self.clicked[0] = 1
                if (len(self.p1.bullets) < config.max_bullet):
                    self.p1.bullets.append(player.bullet(self.p1.rect.center, self.p1.dir, self.p1))
            elif not keypressed[pygame.K_r]:
                self.clicked[0] = 0
            if keypressed[pygame.K_LEFT] and not keypressed[pygame.K_RIGHT]:
                self.p2.direction.x = -1
                self.p2.dir = -1
            elif keypressed[pygame.K_RIGHT] and not keypressed[pygame.K_LEFT]:
                self.p2.direction.x = 1
                self.p2.dir = 1
            else:
                self.p2.direction.x = 0
            if keypressed[pygame.K_UP]:
                if self.collideStage(self.p2):
                    self.p2.direction.y = -5
                    self.p2.jump_time = 0
                elif not self.collideStage(self.p2) and self.p2.jump_time < self.p2.max_jump:
                    self.p2.direction.y = -3
                    self.p2.jump_time+=1
            if keypressed[pygame.K_RETURN] and not self.clicked[1]:
                self.clicked[1] = 1
                if len(self.p2.bullets)<config.max_bullet:
                    self.p2.bullets.append(player.bullet(self.p2.rect.center, self.p2.dir, self.p2))            
            elif not keypressed[pygame.K_RETURN]:
                self.clicked[1] = 0
            
            
class Finish(Scene_base):
    def __init__(self):
        self.winner_color = win.character.color
        self.rect = win.rect
        self.text = "Player "+str(win.identify)+" Won!"
        self.rect.center = (config.win_width/2,config.win_length/3)
        self.text_pos = pygame.math.Vector2(config.win_width/2, config.win_length/4*3)
    def generate(self):
        draw.generateText(self.text,50,self.text_pos,config.textFont1)
        
    def update(self):
        self.generate()
    def get_buttons(self):
        return self.buttons
    def handle_event(self):
        pass
