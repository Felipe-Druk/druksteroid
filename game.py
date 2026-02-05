
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from shot import Shot

from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event, log_state
from player import Player


class Game():

    def __init__(self):
        pygame.init()

        self.__runing = True

        #groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots,self.updatable, self.drawable)

        #Time
        self.clock = pygame.time.Clock()
        self.dt = 0

        #Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        #asteroid field
        self.asteroid_field = AsteroidField()

        #player
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def start(self):
        while self.__runing:
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__runing = False
                    break
            self.screen.fill("black")

            for asteroid in self.asteroids:
                if self.player.collides_with(asteroid):
                    log_event("player_hit")
                    print("Game over!")
                    self.__runing = False
                    break
            for shot in self.shots:
                for asteroid in self.asteroids:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()

            for sprite in self.updatable:
                sprite.update(self.dt)

            for sprite in self.drawable:
                sprite.draw(self.screen)


            self.clock.tick(60)
            self.dt = self.clock.get_time() / 1000.0 

            pygame.display.flip()
        pygame.quit()