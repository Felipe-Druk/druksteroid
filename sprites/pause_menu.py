import pygame

import constants

from sprites.shape import Shape



class PauseMenu(Shape):
    def __init__(self, x, y, options=[""]):
        super().__init__(x, y)
        self.font = pygame.font.SysFont(None, constants.FONT_SIZE)
        self.options = options
        self._selected_option = 0
        self.character_selected = "> "
        self.image = self.font.render("GAME PAUSED", True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._delay_options = 0.05
        self._time_since_last_input = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self._time_since_last_input += dt
        if self._time_since_last_input >= self._delay_options:
            if keys[pygame.K_UP]:
                self._selected_option = (self._selected_option - 1) % len(self.options)
            if keys[pygame.K_DOWN]:
                self._selected_option = (self._selected_option + 1) % len(self.options)
            if keys[pygame.K_RETURN]:
                return self.options[self._selected_option]
            self._time_since_last_input = 0
            if keys[pygame.K_KP_ENTER]:
                return self.options[self._selected_option]
        return None

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for i, option in enumerate(self.options):
            if i == self._selected_option:
                option_image = self.font.render(self.character_selected + option, True, self.color)
            else:
                option_image = self.font.render("  " + option, True, self.color)
            screen.blit(option_image, (self.rect.x, self.rect.y + (i+1) * 30))
