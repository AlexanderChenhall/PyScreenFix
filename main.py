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

        colors = [(255, 0, 0),      # Red       |     Declare tuples for RGB Values
                  (0, 255, 0),      # Blue
                  (0, 0, 255),      # Green
                  (0, 0, 0,),       # Black
                  (255, 255, 255),  # White
                  (0, 255, 255),    # Cyan
                  (255, 0, 255),    # Magenta
                  (255, 255, 0)]    # Yellow

        colors_2d = np.array(colors)          # |     Turn list of lists into a numpy array

        # Creates an Array containing the indices for their corresponding tuples from colors
        pIndices = np.random.choice(len(colors_2d), size=(displayWidth, displayHeight))

        # Create a new array by indexing colors_2d with pIndices
        pixel_array = colors_2d[pIndices]

        # Create surface using new 3D array of randomly selected color tuples
        pixel_surface = pygame.surfarray.make_surface(pixel_array)

        screen.blit(pixel_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)  # Limit FPS
        pygame.time.delay(1)


pygame.quit()
sys.exit()