import pygame

import constants

from sprites.sahpe import Shpe

class Score(Shpe):
    def __init__(self, score, x, y):
        super().__init__(x, y)
        self.score = score
        self.font = pygame.font.SysFont(None, constants.FONT_SIZE)
        self.image = self.font.render(f'Score: {self.score}', True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def __new_image(self):
        self.image = self.font.render(f'Score: {self.score}', True, self.color)
        old_topleft = self.rect.topleft
        self.rect = self.image.get_rect()
        self.rect.topleft = old_topleft

    def change_color(self, color):
        self.color = color
        self.__new_image()

    def increase(self, amount):
        self.score += amount
        self.__new_image()
    
    def reset(self):
        super().reset()
        self.score = 0
        self.__new_image()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect) 