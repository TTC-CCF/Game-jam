import pygame
import config as cf
import scene
import draw 
pygame.init()
pygame.display.set_caption("First Game")

def main():
    running = True
    clock = pygame.time.Clock()
    phase = draw.draw_scene(scene.Scene)
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