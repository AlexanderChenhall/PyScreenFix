import pygame
import random
import sys
import numpy as np

if __name__ == "__main__":
    pygame.init()
    displayInfo = pygame.display.Info()
    # print(screenInfo)
    displayWidth = displayInfo.current_w
    displayHeight = displayInfo.current_h

    # screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN | pygame.HWACCEL)

    screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.HWACCEL)

    active = True
    clock = pygame.time.Clock()

    while active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active = False

        pixel_array = np.random.randint(0, 256, (displayWidth, displayHeight, 3), dtype=np.uint8) #Generate random pixels
        pixel_surface = pygame.surfarray.make_surface(pixel_array)
        screen.blit(pixel_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)  # Limit FPS
        pygame.time.delay(1)


pygame.quit()
sys.exit()