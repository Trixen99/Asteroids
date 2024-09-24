import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, width=2)    

    def update(self,dt):
        self.position += (self.velocity * dt) 

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_asteroid_velocity_1 = self.velocity.rotate(random_angle)
        new_asteroid_velocity_2 = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_1.velocity = new_asteroid_velocity_1 * 1.2
        new_asteroid_2.velocity = new_asteroid_velocity_2 * 1.2
        

        
