import pygame

import constants
from sprites.shape import Shape


class CircleShape(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)