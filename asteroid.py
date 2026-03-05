import pygame
import random

from circleshape import CircleShape
from logger import log_event

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        child_angle = random.uniform(20,50)
        child1_v = self.velocity.rotate(child_angle)
        child2_v = self.velocity.rotate(-child_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = child1_v
        child2.velocity = child2_v