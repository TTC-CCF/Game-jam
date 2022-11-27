import pygame
import config as cf
import scene
import draw 

pygame.init()
pygame.display.set_caption("Just Brawl")
icon = pygame.image.load("justbrawl.ico")
pygame.display.set_icon(icon)
def main():
    running = True
    clock = pygame.time.Clock()
    phase = draw.draw_scene(scene.Scene)
    pygame.mixer.music.load(cf.menu)
    pygame.mixer.music.play(-1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if scene.Scene != "Battle":
                changeScene = phase.handle_event()
                if changeScene:
                    phase = draw.draw_scene(scene.Scene)
        if scene.Scene == "Battle":
            changeScene = phase.handle_event()
            if changeScene:
                phase = draw.draw_scene(scene.Scene)
        draw.update(phase)
        clock.tick(cf.delay)
                
        
if __name__=="__main__":
    main()