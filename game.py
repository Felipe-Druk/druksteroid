
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_SPRITE_COLOR, DEFAULT_BACKGROUND_COLOR
from color import darken_color, lighten_color
from logger import log_event, log_state


#sprites
from sprites.shot import Shot
from sprites.asteroid import Asteroid
from sprites.asteroidfield import AsteroidField
from sprites.player import Player
from sprites.score import Score
from sprites.pause_menu import PauseMenu


class Game():

    def __init__(self, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, sprite_color = DEFAULT_SPRITE_COLOR, background_color = DEFAULT_BACKGROUND_COLOR):

        self.__runing = True
        self.__is_paused = False
        self.sprite_color = sprite_color
        self.background_color = background_color

        #groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.texts = pygame.sprite.Group()
        self.resetables = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable, self.resetables)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable, self.resetables)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots,self.updatable, self.drawable)
        Score.containers = (self.drawable, self.texts, self.resetables)


        #Time
        self.clock = pygame.time.Clock()
        self.dt = 0

        #Screen
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.__screen_width = screen_width
        self.__screen_height = screen_height

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

    def __update(self):
        for sprite in self.updatable:
            sprite.update(self.dt)
    def __draw(self):
        self.screen.fill(self.background_color)
        for sprite in self.drawable:
            sprite.draw(self.screen)
            
    def change_sprite_color(self, color):
        self.sprite_color = color
        Asteroid.color = self.sprite_color
        Shot.color = self.sprite_color
        self.player.color = self.sprite_color
        self.score.change_color(self.sprite_color)
        
    
    def change_background_color(self, color):
        self.background_color = color

    def get_score(self):
        return self.score.score
    
    def reset(self):
        self.__runing = True
        self.__is_paused = False
        for sprite in self.resetables:
            sprite.reset()

        self.asteroid_field.spawn_timer = 0
        self.dt = 0
        self.player.reset()
        self.clock.tick(self.dt)

    def pause(self):
        self.__is_paused = True
        old_color = self.sprite_color
        new_color = darken_color(self.sprite_color, 0.5)
        self.change_sprite_color(new_color)
        self.clock.tick(60)
        pause_menu = PauseMenu(self.score.score, self.__screen_width / 2 - 100, self.__screen_height / 2 - 50)
        self.drawable.add(pause_menu)
        while self.__is_paused:
            self.__draw()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.resolve_keys_imput(pygame.key.get_pressed(), event.type)
            self.clock.tick(60)
            self.dt = self.clock.get_time() / 1000.0 
            pygame.display.flip()

        pause_menu.kill()
        self.change_sprite_color(old_color)

    def resolve_keys_imput(self, keys, event_type = None):
        if event_type is None:
            return
        
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            self.__runing = False
            self.__is_paused = False
            
        if keys[pygame.K_r]:
            self.reset()

        if keys[pygame.K_p] and event_type == pygame.KEYDOWN:
            log_event("PAUSE")
            if self.__is_paused:
                log_event("UNPAUSE")
                self.__is_paused = False
            else:
                self.pause()

    def start(self):
        while self.__runing:
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__runing = False
                    break
                if event.type == pygame.KEYDOWN:
                    self.resolve_keys_imput(pygame.key.get_pressed(), event.type)
                if event.type == pygame.KEYUP:
                    self.resolve_keys_imput(pygame.key.get_pressed(), event.type)

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
            self.__update()
            self.__draw()


            self.clock.tick(60)
            self.dt = self.clock.get_time() / 1000.0 

            pygame.display.flip()
        print(f"final score: {self.score.score}")
        print(f"Exiting game... Bye!")