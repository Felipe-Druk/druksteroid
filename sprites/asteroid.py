
import pygame
import random

from sprites.circleshape import CircleShape
import constants
import logger

class Asteroid(CircleShape):
        
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
            constants.LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        logger.log_event("asteroid_split")
        angle = random.uniform(20,50)
        first_asteroid_velocity = self.velocity.rotate(angle)
        second_asteroid_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_asteroid_velocity
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = second_asteroid_velocity

