import pygame
import random
import sys

if __name__ == "__main__":
    pygame.init()
    displayInfo = pygame.display.Info()
    # print(screenInfo)
    displayWidth = displayInfo.current_w
    displayHeight = displayInfo.current_h

    screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

    active = True
    clock = pygame.time.Clock()

    while active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active = False
