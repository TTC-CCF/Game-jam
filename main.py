import pygame
import config as cf
import blocks
import scene
import draw
pygame.init()
pygame.display.set_caption("First Game")

def main():
    running = True
    phase = draw.draw_scene(scene.Scene)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            changeScene = phase.handle_event(event)
            if changeScene:
                phase = draw.draw_scene(scene.Scene)
        draw.update(phase)
                
        
if __name__=="__main__":
    main()