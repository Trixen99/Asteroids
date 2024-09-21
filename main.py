import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroids_Group = pygame.sprite.Group()
    Shots_Group = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, Asteroids_Group)
    Shot.containers = (updatable, drawable, Shots_Group)
    AsteroidField.containers = (updatable)
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroids = AsteroidField()


    

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        for updates in updatable:
            updates.update(dt)
        for asteroid in Asteroids_Group:
            if player1.collision_detection(asteroid) == True:
                print("Game over!")
                exit()
        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()