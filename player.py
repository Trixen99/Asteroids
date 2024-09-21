import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.reload_time = PLAYER_RELOAD_TIME
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "WHITE",self.triangle(),width=2)

    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            if self.reload_time <= 0:
                self.shoot(self.position.x, self.position.y)
                self.reload_time = 0.3
        self.reload_time -= dt
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, x, y):
        shot = Shot(x,y)
        shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)




        
class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, width=2)    

    def update(self,dt):
        self.position += (self.velocity * dt) 