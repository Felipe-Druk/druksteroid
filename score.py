import pygame

from constants import FONT_SIZE, FONT_COLOR



class Score(pygame.sprite.Sprite):
    def __init__(self, score, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = score
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.image = self.font.render(f'Score: {self.score}', True, FONT_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def __new_image(self):
        self.image = self.font.render(f'Score: {self.score}', True, FONT_COLOR)
        old_topleft = self.rect.topleft
        self.rect = self.image.get_rect()
        self.rect.topleft = old_topleft

    def increase(self, amount):
        self.score += amount
        self.__new_image()
    
    def reset(self):
        self.score = 0
        self.__new_image()
    
    def draw(self, screen):
    
        screen.blit(self.image, self.rect) 