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
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable, drawable)
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
        for a in asteroids:
            # Exiting the game when player collides with asteroids
            if a.is_colliding(player):
                print("Game over!")
                pygame.quit()
                return
            # Removing asteroids hit by shots
            for s in shots:
                if s.is_colliding(a):
                    s.kill()
                    a.split()
        
        # Refreshing the screen
        pygame.display.flip()
        # Restricting fps to 60
        dt = (clock.tick(60)/1000)
        



if __name__ == "__main__":
    main()
