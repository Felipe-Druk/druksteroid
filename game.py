
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_SPRITE_COLOR, DEFAULT_BACKGROUND_COLOR

from logger import log_event, log_state


#sprites
from sprites.shot import Shot
from sprites.asteroid import Asteroid
from sprites.asteroidfield import AsteroidField
from sprites.player import Player
from sprites.score import Score


class Game():

    def __init__(self, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, sprite_color = DEFAULT_SPRITE_COLOR, background_color = DEFAULT_BACKGROUND_COLOR):

        self.__runing = True
        self.sprite_color = sprite_color
        self.background_color = background_color

        #groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.texts = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots,self.updatable, self.drawable)
        Score.containers = (self.drawable, self.texts)

     


        #Time
        self.clock = pygame.time.Clock()
        self.dt = 0

        #Screen
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        #asteroid field
        self.asteroid_field = AsteroidField()

        #score
        self.score = Score(0, 100 , screen_height - 100)

        #player
        self.player = Player(screen_width / 2, screen_height / 2)

        #colors
        Asteroid.color = self.sprite_color
        Shot.color = self.sprite_color
        Player.color = self.sprite_color
        self.background_color = background_color
        self.score.change_color(self.sprite_color)

    def change_sprite_color(self, color):
        self.sprite_color = color
        Asteroid.color = self.sprite_color
        Shot.color = self.sprite_color
        self.player.color = self.sprite_color
        self.score.change_color(self.sprite_color)
        
    
    def change_background_color(self, color):
        self.background_color = color

    def start(self):
        while self.__runing:
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__runing = False
                    break
            self.screen.fill(self.background_color)

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
                        self.score.increase(10)
                        shot.kill()

            for sprite in self.updatable:
                sprite.update(self.dt)

            for sprite in self.drawable:
                sprite.draw(self.screen)


            self.clock.tick(60)
            self.dt = self.clock.get_time() / 1000.0 

            pygame.display.flip()
        print(f"final score: {self.score.score}")
        print(f"Exiting game... Bye!")