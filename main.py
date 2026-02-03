import pygame   
import sys

from logger import log_event, log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)

    #Time
    clock = pygame.time.Clock()
    dt = 0

    #Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #asteroid field
    asteroid_field = AsteroidField()

    #player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)


        clock.tick(60)
        dt = clock.get_time() / 1000.0 

        pygame.display.flip()


if __name__ == "__main__":
    main()
