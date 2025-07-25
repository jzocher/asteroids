import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(rand)
        new_vel2 = self.velocity.rotate(-rand)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)

        new_asteroid1.velocity = new_vel1 * 1.2
        new_asteroid2.velocity = new_vel2 * 1.2

        