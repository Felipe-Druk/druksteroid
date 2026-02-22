import pygame   
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game
from menu_druksteroid import MenuDruksteroid
from persistence.high_score_savior import HighScoreSavior, HighScore

def main():
    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game = Game()
    score = 0
    high_score = HighScoreSavior("tall_score.pickle", HighScore(score, "DRUK") )
    high_old = high_score.deserialize()
    print(high_old.score)
    menu = MenuDruksteroid(game.screen)

    while True:
        menu.display()
        game.change_sprite_color(menu.get_selected_color())
        game.start()

        if score < game.get_score():
            score = game.get_score()
            high_score = HighScoreSavior("tall_score.pickle", HighScore(score, "DRUK") )
            high_score.serialize()
            print(f"New high score: {score}")
        
        game.reset()
        menu.reset()
        
    pygame.quit() 
    


if __name__ == "__main__":
    main()
