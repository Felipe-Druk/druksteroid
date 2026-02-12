import pygame

import constants
from sprites.sahpe import Shpe


class CircleShape(Shpe):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)