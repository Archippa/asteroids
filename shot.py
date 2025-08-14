import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, position, velocity, radius):
        super().__init__(position.x, position.y, radius)
        self.velocity = velocity
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 0)

    def update(self, dt):
        self.position += (self.velocity * dt)

