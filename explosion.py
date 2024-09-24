import pygame
from constants import *
from circleshape import CircleShape

class Explosion(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, BOMB_EXPLOSION_RADIUS_START)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, width=0)


    def update(self, dt):
        if self.time_onscreen <= 0:
            self.kill()
        self.radius += dt * 50
        self.time_onscreen -= dt
                