import pygame
import sys
import numpy as np

if __name__ == "__main__":
    pygame.init()
    displayInfo = pygame.display.Info()
    displayWidth = displayInfo.current_w + 2   # Adding 2 to the values and foregoing fullscreen
    displayHeight = displayInfo.current_h + 2  # in order to avoid black bars or the top bar

    screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.HWACCEL)

    active = True
    clock = pygame.time.Clock()

    colors = [(255, 0, 0),  # Red       |     Declare tuples for RGB Values
              (0, 255, 0),  # Blue
              (0, 0, 255),  # Green
              (0, 0, 0,),  # Black
              (255, 255, 255),  # White
              (0, 255, 255),  # Cyan
              (255, 0, 255),  # Magenta
              (255, 255, 0)]  # Yellow

    colors_2d = np.array(colors)  # |     Turn list of lists into a numpy array

    # Calculate the positions of each zone based on the size of the display
    zonePositions = [(0 * (displayWidth // 8), 0),
                     (1 * (displayWidth // 8), 0),
                     (2 * (displayWidth // 8), 0),
                     (3 * (displayWidth // 8), 0),
                     (4 * (displayWidth // 8), 0),
                     (5 * (displayWidth // 8), 0),
                     (6 * (displayWidth // 8), 0),
                     (7 * (displayWidth // 8), 0)]

    while active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active = False

        # Creates an Array containing the indices for their corresponding tuples from colors
        # Here we only calculate for 1/8th of the screen, as we are essentially splitting the
        # display into 8 zones
        pIndices = np.random.choice(len(colors_2d), size=(displayWidth // 8, displayHeight))

        # Create a new array by indexing colors_2d with pIndices
        pixel_array = colors_2d[pIndices]

        # Create surface using new 3D array of randomly selected color tuples
        pixel_surface = pygame.surfarray.make_surface(pixel_array)

        # Blit onto each strip of the 8 zones on the screen
        screen.blit(pixel_surface, (zonePositions[0]))
        screen.blit(pixel_surface, (zonePositions[1]))
        screen.blit(pixel_surface, (zonePositions[2]))
        screen.blit(pixel_surface, (zonePositions[3]))
        screen.blit(pixel_surface, (zonePositions[4]))
        screen.blit(pixel_surface, (zonePositions[5]))
        screen.blit(pixel_surface, (zonePositions[6]))
        screen.blit(pixel_surface, (zonePositions[7]))

        pygame.display.flip()
        clock.tick(60)  # Limit FPS
        pygame.time.delay(1)


pygame.quit()
sys.exit()
