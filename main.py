import pygame
import random
import sys
import numpy as np

if __name__ == "__main__":
    pygame.init()
    displayInfo = pygame.display.Info()
    displayWidth = displayInfo.current_w+2  # Adding 2 to the values and foregoing fullscreen
    displayHeight = displayInfo.current_h+2 # in order to avoid black bars or the top bar

    screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.HWACCEL)

    active = True
    clock = pygame.time.Clock()

    while active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active = False

        colors = [(255, 0, 0),      #red
                  (0, 255, 0),      #blue
                  (0, 0, 255),      #green
                  (0, 0, 0,),       #black
                  (255, 255, 255),  #white
                  (0, 255, 255),    #cyan
                  (255, 0, 255),    #magenta
                  (255, 255, 0)]    #yeLlow

        colors_2d = np.array(colors)
        pIndices = np.random.choice(len(colors_2d), size=(displayWidth, displayHeight))
        pixel_array = colors_2d[pIndices]
        pixel_surface = pygame.surfarray.make_surface(pixel_array)
        screen.blit(pixel_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)  # Limit FPS
        pygame.time.delay(1)


pygame.quit()
sys.exit()