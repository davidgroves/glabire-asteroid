import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # random generator
            rand_angle = random.uniform(20, 50)

            # settings the velocity of the new asteroids
            new_velocity1 = self.velocity.rotate(rand_angle)
            new_velocity2 = self.velocity.rotate(-rand_angle)

            # new radius to determine the size of the new asteroids
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            # First new asteroid
            new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid1.velocity = new_velocity1 * 1.2

            # Second new asteroid
            new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid2.velocity = new_velocity2 * 1.2

            return [new_asteroid1, new_asteroid2]
