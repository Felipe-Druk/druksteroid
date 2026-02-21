from color import WHITE, BLACK
from enum import Enum

#Sceen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#Color definitions
DEFAULT_SPRITE_COLOR = WHITE
DEFAULT_BACKGROUND_COLOR = BLACK  

#Menu dimensions
MENU_WIDTH = SCREEN_WIDTH
MENU_HEIGHT = SCREEN_HEIGHT

#Menu titles
MENU_TITLE = "Druksteroids Menu"
SELECTOR_TITLE = "Color game: "

#General properties
LINE_WIDTH = 2

#Pasue menu properties
class PauseMenuOption(Enum):
    RESUME = 0
    RESTART = 1
    QUIT = 2

MENU_OPTIONS = ["Resume", "Restart", "Quit"]

#Player properties
PLAYER_RADIUS = 20 
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

#Score properties
SCORE_INCREASE_AMOUNT = 10
FONT_SIZE = 40

#Asteroids propierties
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3

#shooting properties
SHOT_RADIUS = 5
