import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # Initliazing pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    # Getting new GUI 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid = AsteroidField()
    # Game loop
    while(True):
        # Checking if user has closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Filling the screen with black
        screen.fill((0,0,0))
        # Drawing the player
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        # Refreshing the screen
        pygame.display.flip()
        #restricting fps to 60
        dt = (clock.tick(60)/1000)
        



if __name__ == "__main__":
    main()
