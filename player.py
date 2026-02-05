
import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    color = "white"

    def __init__(self, x, y):
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.__shot_cooldown = 0
        super().__init__(x, y, self.radius)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            self.color,
            self.triangle(),
            LINE_WIDTH,
        )
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.__shot_cooldown <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot = Shot(
                self.position.x + forward.x * self.radius,
                self.position.y + forward.y * self.radius,
            )
            shot.velocity = forward * PLAYER_SHOOT_SPEED
            self.__shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            return shot

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.__shot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            return self.shoot()