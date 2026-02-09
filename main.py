import pygame   
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_SPRITE_COLOR, DEFAULT_BACKGROUND_COLOR
from game import Game
from menu_druksteroid import MenuDruksteroid

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

    game = Game(sprite_color=DEFAULT_SPRITE_COLOR, background_color=DEFAULT_BACKGROUND_COLOR)
    menu = MenuDruksteroid(game.screen)

    menu.display()
    game.change_sprite_color(menu.get_selected_color())
    game.start()

    pygame.quit() 
    


if __name__ == "__main__":
    main()
