import pygame
import pygame_menu as pm

from constants import MENU_WIDTH, MENU_HEIGHT, MENU_TITLE, SELECTOR_TITLE, DEFAULT_SPRITE_COLOR, DEFAULT_BACKGROUND_COLOR
from color import WHITE, RED, BLUE, GREEN, YELLOW, NEON_PURPLE




class MenuDruksteroid(pm.Menu):

    def __init__(self, screen):
        super().__init__(
            height=MENU_HEIGHT,
            width=MENU_WIDTH,
            title=MENU_TITLE,
            theme=pm.themes.THEME_DARK,
        )
        self.screen = screen
        self.add.button("Start Game", self.start_game)
        self.color_selector = self.add.selector(
            SELECTOR_TITLE,
            [("White", 1), ("Red", 2), ("Blue", 3), ("Green", 4), ("Yellow", 5), ("Neon Purple", 6)],
        )
        self.add.button("Quit", pm.events.EXIT)

    def get_selected_color(self):
        selected_tuple = self.color_selector.get_value()
        color_name = selected_tuple[0][0] if selected_tuple else DEFAULT_SPRITE_COLOR
        color_dict = {
            "White": WHITE,
            "Red": RED,
            "Blue": BLUE,
            "Green": GREEN,
            "Yellow": YELLOW,
            "Neon Purple": NEON_PURPLE
        }
        return color_dict.get(color_name, DEFAULT_SPRITE_COLOR)
    
    def start_game(self):
        self.disable()  

    def display(self):
        self.mainloop(self.screen)
