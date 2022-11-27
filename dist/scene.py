import draw
import config
import pygame
import player
Scene = "menu"
Player1 = 1
Player2 = 2
nump1win = 0
nump2win = 0
_round = 0
pressESC = 0
win = None
def next_phase(button):
    global Scene
    if Scene == "menu":
        if button.text == "Quit":
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        elif button.text == "Start":
            Scene = "ChooseCharacters"
        elif button.text == "Option":
            Scene = "Option"
            
    elif Scene == "ChooseCharacters":
        pygame.mixer.music.fadeout(2000)
        Scene = "Ready"
    elif Scene == "Ready":
        pygame.mixer.music.unload()
        pygame.mixer.music.load(config.battle)
        pygame.mixer.music.play(-1)
        Scene = "Battle"
    elif Scene == "Battle":
        if nump2win == config.numwin or nump1win == config.numwin:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.unload()
            pygame.mixer.music.load(config.finish)
            pygame.mixer.music.play()
            Scene = "finish"
        else:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.unload()
            pygame.mixer.music.load(config.nextround)
            pygame.mixer.music.play(-1)
            Scene = "nextround"
    elif Scene == "nextround":
        pygame.mixer.music.pause()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(config.battle)
        pygame.mixer.music.play(-1)
        Scene = "Battle"
    elif Scene == "finish":
        pygame.mixer.music.unload()
        pygame.mixer.music.load(config.menu)
        pygame.mixer.music.play(-1)
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
        self.Oblock_x = config.win_width/2
        self.Oblock_y = self.Sblock_y+self.len+10
        self.Qblock_x = config.win_width/2
        self.Qblock_y = self.Oblock_y+self.len+10
        self.hover_but = 0
        self.buttons = [draw.button("Start",(self.Sblock_x, self.Sblock_y), self.len),
                        draw.button("Option", (self.Oblock_x, self.Oblock_y), self.len),
                        draw.button("Quit", (self.Qblock_x, self.Qblock_y), self.len)]

    def generate(self):
        draw.generateText("Just brawl", self.Title_size, (config.win_width/2, 200),config.textFont1)
        for button in self.buttons:
            button.draw()

    def update(self):
        self.generate()
    
    def get_buttons(self):
        return self.buttons
    
    def handle_event(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_UP]:
            pygame.mixer.Sound.play(config.move_button)
            self.buttons[self.hover_but].hover = False
            if self.hover_but == 0:
                self.hover_but = len(self.buttons)-1
            else:
                self.hover_but -= 1
        if keypress[pygame.K_DOWN]:
            pygame.mixer.Sound.play(config.move_button)
            self.buttons[self.hover_but].hover = False
            if self.hover_but == len(self.buttons)-1:
                self.hover_but = 0
            else:
                self.hover_but += 1
        self.buttons[self.hover_but].hover = True
        if keypress[pygame.K_RETURN] or keypress[pygame.K_KP_ENTER]:
            pygame.mixer.Sound.play(config.click_button)
            next_phase(self.buttons[self.hover_but])
            return True

class Option(Scene_base):
    def __init__(self):
        self.text = ["Option","Round", "Lives", "Back Ground"]
        self.pos = [(config.win_width/2,config.win_length/6),(config.win_width/4,config.win_length/5*2),(config.win_width/4,config.win_length/5*3),(config.win_width/4,config.win_length/5*4)]
        self.buttons = [draw.button(self.text[1],self.pos[1],50),
                        draw.button(self.text[2],self.pos[2],50),
                        draw.button(self.text[3],self.pos[3],50)]
        self.bg_frame_pos = (config.win_width/4*3,config.win_length/5*4)
        self.bg_frame_w = 250
        self.bg_frame_l = 140
        self.hover_but = 0
    def generate(self):
        draw.generateText(self.text[0],60,self.pos[0],config.textFont1)
        draw.generateText(str(config.Round),50,(config.win_width/4*3,config.win_length/5*2),config.textFont1)
        draw.generateText(str(config.lives),50,(config.win_width/4*3,config.win_length/5*3),config.textFont1)
        draw.draw_block_wline(self.bg_frame_pos,self.bg_frame_w,self.bg_frame_l,(255,255,255),5)
        self.bg = pygame.image.load(config.bgs[config.curbg])
        self.bg = pygame.transform.scale(self.bg,(self.bg_frame_w-10,self.bg_frame_l-10))
        draw.showPicture(self.bg, (config.win_width/4*3-self.bg_frame_w/2+5,config.win_length/5*4-self.bg_frame_l/2+5))
        for button in self.buttons:
            button.draw()
    def update(self):
        self.generate()
    def handle_event(self):
        keypress = pygame.key.get_pressed()
        global Scene
        if keypress[pygame.K_ESCAPE]:
            pygame.mixer.Sound.play(config.esc)
            Scene = "menu"
            return True
        if keypress[pygame.K_UP]:
            pygame.mixer.Sound.play(config.move_button)
            self.buttons[self.hover_but].hover = False
            if self.hover_but == 0:
                self.hover_but = len(self.buttons)-1
            else:
                self.hover_but -= 1
        if keypress[pygame.K_DOWN]:
            pygame.mixer.Sound.play(config.move_button)
            self.buttons[self.hover_but].hover = False
            if self.hover_but == len(self.buttons)-1:
                self.hover_but = 0
            else:
                self.hover_but += 1
        self.buttons[self.hover_but].hover = True
        if self.buttons[0].hover == True:
            if keypress[pygame.K_LEFT] and config.Round > 3:
                pygame.mixer.Sound.play(config.click_button)
                config.Round -= 2
                config.numwin = config.Round//2+1
            elif keypress[pygame.K_RIGHT] and config.Round < 7:
                pygame.mixer.Sound.play(config.click_button)
                config.Round += 2
                config.numwin = config.Round//2+1
        elif self.buttons[1].hover == True:
            if keypress[pygame.K_LEFT] and config.lives > 1:
                pygame.mixer.Sound.play(config.click_button)
                config.lives -= 1
            elif keypress[pygame.K_RIGHT] and config.lives < 10:
                pygame.mixer.Sound.play(config.click_button)
                config.lives += 1
        elif self.buttons[2].hover == True:
            if keypress[pygame.K_LEFT] and config.curbg > 0:
                pygame.mixer.Sound.play(config.click_button)
                config.curbg -= 1
                draw.changeBG(config.bgs[config.curbg])
            elif keypress[pygame.K_RIGHT] and config.curbg < len(config.bgs)-1:
                pygame.mixer.Sound.play(config.click_button)
                config.curbg += 1
                draw.changeBG(config.bgs[config.curbg])

                

class Choose(Scene_base):
    def __init__(self):
        self.text_size = 70
        self.buttons = []
        self.p1_character = 1
        self.p2_character = 2
        self.buttons = [draw.button("Press E to Ready", (config.win_width/4, config.win_length/5+self.text_size+330), 30),
                        draw.button("Press ENTER to Ready", (config.win_width/4*3, config.win_length/5+self.text_size+330), 30)]
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
            image1 = pygame.image.load("./character3/idle1.png")
        elif self.p1_character == 2:
            image1 = pygame.image.load("./character2/idle1.png")
        elif self.p1_character == 3:
            image1 = pygame.image.load("./character1/idle1.png")
        if self.p2_character == 1:
            image2 = pygame.image.load("./character3/idle1.png")
        elif self.p2_character == 2:
            image2 = pygame.image.load("./character2/idle1.png")
        elif self.p2_character == 3:
            image2 = pygame.image.load("./character1/idle1.png")
        image1 = pygame.transform.scale(image1,(image1.get_width()*3,image1.get_height()*3))
        image2 = pygame.transform.scale(image2,(image2.get_width()*3,image2.get_height()*3))

        rect1 = image1.get_rect()
        rect2 = image2.get_rect()
        rect1.center = (config.win_width/4,config.win_length/5+self.text_size+140)
        rect2.center = (config.win_width/4*3,config.win_length/5+self.text_size+140)
        draw.draw_sprite(image1,rect1)
        draw.draw_sprite(image2,rect2)

    def hover_buttons(self):
        pass
    
    def get_buttons(self):
        return self.buttons
    def handle_event(self):
        changeScene = False
        global pressESC
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_a]:
            pygame.mixer.Sound.play(config.move_button)
            self.change_character(-1, 1)
        if keypress[pygame.K_d]:
            pygame.mixer.Sound.play(config.move_button)
            self.change_character(1, 1)
        if keypress[pygame.K_LEFT]:
            pygame.mixer.Sound.play(config.move_button)
            self.change_character(-1, 2)
        if keypress[pygame.K_RIGHT]:
            pygame.mixer.Sound.play(config.move_button)
            self.change_character(1, 2)
        if keypress[pygame.K_e]:
            pygame.mixer.Sound.play(config.click_button)
            self.buttons[0].clicked = not self.buttons[0].clicked
        if keypress[pygame.K_RETURN] or keypress[pygame.K_KP_ENTER]:
            pygame.mixer.Sound.play(config.click_button)
            self.buttons[1].clicked = not self.buttons[1].clicked
        if keypress[pygame.K_ESCAPE] and pressESC == 0:
            pygame.mixer.Sound.play(config.esc)
            pressESC = 1
            global Scene
            Scene = "menu"
            changeScene = True
        elif not keypress[pygame.K_ESCAPE]:
            pressESC = 0
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
        global nump1win,nump2win,win
        super().__init__()
        self.pos = (config.win_width/2, config.win_length/2)
        self.wid = config.win_width-200
        self.len = config.win_length//3
        self.text = "Press Enter to Brawl!"
        self.text_size = self.len-150
        nump1win = 0
        nump2win = 0
        win = None
        
    def generate(self):
        draw.draw_block_wline(self.pos, self.wid, self.len, (255,255,255), 3)
        draw.draw_block(self.pos, self.wid-200, self.len-100, (255,255,150))
        draw.generateText(self.text, self.text_size, self.pos, config.textFont1, color=(0,0,0))
    def update(self):
        super().update()
    def get_buttons(self):
        super().get_buttons
    def handle_event(self):
        changeScene = False
        global pressESC
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_RETURN] or keypress[pygame.K_KP_ENTER]:
            changeScene = True
            next_phase(self.buttons)
        if keypress[pygame.K_ESCAPE]:
            pressESC = 1
            global Scene
            Scene = "ChooseCharacters"
            changeScene = True
        return changeScene
class Battle(Scene_base):
        
    def __init__(self):
        super().__init__()
        self.stageRect = pygame.Rect(config.win_width/2-config.stage_width/2,config.win_length/4*3-config.stage_thickness/2,config.stage_width,config.stage_thickness)
        self.p1 = player.P(Player1, 1, config.lives)
        self.p2 = player.P(Player2, 2, config.lives)
        self.players = player.Players(self.p1, self.p2)
        self.setBattle()
        self.clicked = [1,1]
        self.jump = [1,1]
    def generate(self):
        draw.draw_block((config.win_width/2, config.win_length/4*3),config.stage_width+100,config.stage_thickness+16,(159,159,150))
        for pl in self.players.players:
            draw.draw_sprite(pl.image, pl.rect)
            for b in pl.bullets:
                draw.draw_sprite(b.image,b.rect)
                
    def setBattle(self):
        space  =  (config.stage_width-2*config.stage_edge_space)/(config.NUMOFPLAYERS-1)
        i = 0
        for pl in self.players.players:
            pl.set_pos(pygame.math.Vector2(config.win_width/2-config.stage_width/2+config.stage_edge_space+space*i, config.win_length/4*3-config.stage_thickness/2-pl.rect.height/2))
            pl.respon_pos = pygame.math.Vector2(pl.rect.centerx,0)
            i+=1
    def update(self):
        for pl in self.players.players:
            pl.change_pos()
            pl._animate()
        self.handle_bullet()
        self.gravity()
        self.generate()
        self.display_lives()
    def handle_bullet(self):
        for pl in self.players.players:
            if pl.character.job == 1:
                for b in pl.bullets:
                    b.change_pos()
                    if b.direction == 1 and b.rect.centerx > config.win_width:
                        pl.bullets.remove(b)
                    elif b.direction == -1 and b.rect.centerx < 0:
                        pl.bullets.remove(b)
                    for p in self.players.players:
                        if p.rect.colliderect(b.rect) and b.id != p:
                            if not(p.defend and p.dir == -b.direction):
                                if p.rect.left < b.id.rect.left:
                                    p.hurt_by(b.id, -1)
                                else:
                                    p.hurt_by(b.id, 1)
                            if b in pl.bullets:
                                pl.bullets.remove(b)
            elif pl.character.job == 2 and pl.attacking == 1:
                for p in self.players.players:
                    if p != pl and not (p.defend and p.dir == -pl.dir):
                        dis = p.rect.centerx-pl.rect.centerx
                        if abs(dis) < 80 and not (p.rect.top+10 >= pl.rect.bottom - 10 or p.rect.bottom-10<= pl.rect.top+10):
                            if dis>0 and pl.dir > 0:
                                p.hurt_by(pl,1)
                            elif dis < 0 and pl.dir < 0:
                                p.hurt_by(pl,-1)
    def gravity(self):
        for pl in self.players.players:
            if not self.collideStage(pl):
                if pl.direction.y <= config.max_vel:
                    pl.direction.y += pl.character.weight
            else:
                pl.direction.y = 0
                pl.rect.centery = self.stageRect.top-pl.rect.height/2+1

            if pl.rect.top > 2 * config.win_length and not pl.die:
                pygame.mixer.Sound.play(config.loselives)
                pl.lives -= 1
                pl.die = 1
            if pl.rect.top >3 * config.win_length:
                pl.reset()


    def collideStage(self, player):
        return player.rect.colliderect(self.stageRect)
    def get_buttons(self):
        pass
    def display_lives(self):
        draw.generateText("lives: "+str(self.p1.lives), 30, (self.p1.respon_pos.x-50, config.win_length/8*7), config.textFont1)
        draw.generateText("lives: "+str(self.p2.lives), 30, (self.p2.respon_pos.x+50, config.win_length/8*7), config.textFont1)
        draw.generateText(str(self.p1.percentage)+"%", 30, (self.p1.respon_pos.x-50, config.win_length/8*6), config.textFont2)
        draw.generateText(str(self.p2.percentage)+"%", 30, (self.p2.respon_pos.x+50, config.win_length/8*6), config.textFont2)
    def handle_event(self):
            global win,nump1win,nump2win,_round
    # handle lives
            if self.p1.lives == 0:
                nump2win += 1
                _round += 1
                if _round == config.Round or nump2win == config.numwin:
                    win = self.p2
                next_phase(self.buttons)
                return True
            if self.p2.lives == 0:
                nump1win += 1
                _round += 1
                if _round == config.Round or nump1win == config.numwin:
                    win = self.p1
                next_phase(self.buttons)
                return True
            keypressed = pygame.key.get_pressed()

    # p1 attack
            if keypressed[pygame.K_r] and not self.clicked[0] and not self.p1.attacking and not self.p1.defend:
                self.p1.attacking = 1
                pygame.mixer.Sound.play(self.p1.character.attack_se)
                self.p1.cur_frame = 0
                self.clicked[0] = 1
                if (len(self.p1.bullets) < config.max_bullet) and self.p1.character.job != 2:
                    self.p1.bullets.append(player.bullet(self.p1.rect.center, self.p1.dir, self.p1))
            elif not keypressed[pygame.K_r]:
                self.clicked[0] = 0
    # p1 defend
            if not keypressed[pygame.K_e]:
                self.p1.defend = 0
                self.p1.defend_time = 0
                self.p1.da = 0
            if self.p1.defend_time >= config.max_defend:
                self.p1.defend = 0
                self.p1.da = 0
            elif keypressed[pygame.K_e]:
                self.p1.defend = 1
                self.p1.defend_time += 1
            
    # p1 walk
            if keypressed[pygame.K_a] and not keypressed[pygame.K_d] and not self.p1.defend:
                self.p1.direction.x = -1
                self.p1.dir = -1
            elif keypressed[pygame.K_d] and not keypressed[pygame.K_a] and not self.p1.defend:
                self.p1.direction.x = 1
                self.p1.dir = 1
            else:
                self.p1.direction.x = 0
    # p1 jump
            if keypressed[pygame.K_w] and not self.jump[0] and not self.p1.defend:
                self.jump[0] = 1
                self.p1.jumping = 1
                if not self.p1.attacking:
                    self.p1.cur_frame = 0
                if self.collideStage(self.p1):
                    pygame.mixer.Sound.play(self.p1.character.jump_se)
                    self.p1.direction.y = -5
                    self.p1.jump_time = 0
                elif not self.collideStage(self.p1) and self.p1.jump_time < self.p1.max_jump:
                    pygame.mixer.Sound.play(self.p1.character.jump_se)
                    self.p1.direction.y = -3
                    self.p1.jump_time+=1
            elif not keypressed[pygame.K_w]:
                self.jump[0] = 0

    # p2 attack
            if keypressed[pygame.K_RETURN] and not self.clicked[1] and not self.p2.attacking and not self.p2.defend:
                pygame.mixer.Sound.play(self.p2.character.attack_se)
                self.p2.attacking = 1
                self.p2.cur_frame = 0
                self.clicked[1] = 1
                if len(self.p2.bullets)<config.max_bullet and self.p2.character.job != 2:
                    self.p2.bullets.append(player.bullet(self.p2.rect.center, self.p2.dir, self.p2))            
            elif not keypressed[pygame.K_RETURN]:
                self.clicked[1] = 0

    # p2 defend
            if not keypressed[pygame.K_RSHIFT]:
                self.p2.defend = 0
                self.p2.defend_time = 0
                self.p2.da = 0
            if self.p2.defend_time >= config.max_defend:
                self.p2.defend = 0
                self.p2.da = 0
            elif keypressed[pygame.K_RSHIFT]:
                self.p2.defend = 1
                self.p2.defend_time += 1
            
    # p2 walk
            if keypressed[pygame.K_LEFT] and not keypressed[pygame.K_RIGHT] and not self.p2.defend:
                self.p2.direction.x = -1
                self.p2.dir = -1
            elif keypressed[pygame.K_RIGHT] and not keypressed[pygame.K_LEFT] and not self.p2.defend:
                self.p2.direction.x = 1
                self.p2.dir = 1
            else:
                self.p2.direction.x = 0
    # p2 jump
            if keypressed[pygame.K_UP] and not self.jump[1] and not self.p2.defend:
                self.jump[1] = 1
                self.p2.jumping = 1
                if not self.p2.attacking:
                    self.p2.cur_frame = 0
                if self.collideStage(self.p2):
                    pygame.mixer.Sound.play(self.p2.character.jump_se)
                    self.p2.direction.y = -5
                    self.p2.jump_time = 0
                elif not self.collideStage(self.p2) and self.p2.jump_time < self.p2.max_jump:
                    pygame.mixer.Sound.play(self.p2.character.jump_se)
                    self.p2.direction.y = -3
                    self.p2.jump_time+=1
            elif not keypressed[pygame.K_UP]:
                self.jump[1] = 0
    
class NextRound(Scene_base):
    def __init__(self):
        self.buttons = []
    def generate(self):
        draw.generateText("P1",100,(config.win_width/5*1.7,config.win_length/4),config.textFont1)
        draw.generateText("P2",100,(config.win_width/5*3.3,config.win_length/4),config.textFont1)
        draw.generateText(str(nump1win),80,(config.win_width/5*1.7,config.win_length/2),config.textFont1)
        draw.generateText(str(nump2win),80,(config.win_width/5*3.3,config.win_length/2),config.textFont1)
        draw.generateText("Press c to continue",40,(config.win_width/2,config.win_length/4*3),config.textFont1)
        
    def update(self):
        self.generate()
    def get_buttons(self):
        return self.buttons
    def handle_event(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_c]:
            next_phase(self.buttons)
            return True

            
class Finish(Scene_base):
    def __init__(self):
        self.image = win.character.special[0]
        self.rect = self.image.get_rect()
        self.text = "Player "+str(win.identify)+" Won!"
        self.text_pos = (config.win_width/2, config.win_length/4*3)
        self.buttons = []
        self.cur_frame = 0

    def generate(self):
        draw.generateText(self.text,50,self.text_pos,config.textFont1)
        draw.generateText("Press c to continue",30,(config.win_width/2,config.win_length/4*3.5),config.textFont1,(230,230,230))
        draw.draw_sprite(self.image, self.rect)
    def update(self):
        self.animate()
        self.generate()
    
    def animate(self):
        self.cur_frame += 0.1
        if self.cur_frame >= 6:
            self.cur_frame = 0
        self.image = win.character.special[int(self.cur_frame)]
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*4,self.image.get_height()*4))
        self.rect = self.image.get_rect()
        self.rect.center = (config.win_width/2,config.win_length/2)

    def get_buttons(self):
        return self.buttons
    def handle_event(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_c]:
            next_phase(self.buttons)
            return True
