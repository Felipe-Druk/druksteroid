import pygame   
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game
from menu_druksteroid import MenuDruksteroid

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game = Game()
    menu = MenuDruksteroid(game.screen)


    menu.display()
    game.change_sprite_color(menu.get_selected_color())
    game.start()
    
    pygame.quit() 
    


if __name__ == "__main__":
    main()
