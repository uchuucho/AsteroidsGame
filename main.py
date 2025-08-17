import pygame
from constants import *

def main():
    # Initliazing pygame
    pygame.init()
    # Getting new GUI 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Game loop
    while(True):
        # Checking if user has closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Filling the screen with black
        screen.fill((0,0,0))
        # Refreshing the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
