import pygame

import constants

# Base class for game objects
class Shpe(pygame.sprite.Sprite):
    
    color = constants.DEFAULT_SPRITE_COLOR

    def __init__(self, x, y):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def collides_with(self, other):
        # must override
        pass

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass