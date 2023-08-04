# ball.py

import pygame
from settings import WIDTH, HEIGHT, screen, GRAVITY, STOP_BOUNCE


class Ball:

    def __init__(self, posx, posy, radius, color, y_speed, x_speed, mass, retention, friction):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.color = color
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.friction = friction
        self.direction = 1

    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    def check_gravity(self):
        if self.posy < HEIGHT - self.radius:
            self.y_speed += GRAVITY
        else:
            if self.y_speed > STOP_BOUNCE:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= STOP_BOUNCE:
                    self.y_speed = 0
        if self.y_speed == 0 and self.x_speed != 0:
            self.x_speed -= self.friction * self.direction

    def update(self):
        self.posx += self.x_speed * self.direction
        self.posy += self.y_speed

        if self.posy <= 0 or self.posy >= HEIGHT:
            self.y_speed *= -1

        # Remove the speed adjustment when hitting the walls
        if self.posx <= self.radius and self.direction == -1:
            self.x_speed *= -self.retention
        elif self.posx >= WIDTH - self.radius and self.direction == 1:
            self.x_speed *= -self.retention

        self.check_gravity()

        if self.posx <= 0 or self.posx >= WIDTH:
            self.firstTime = 1

    def resolve_collision(self, player_rect):
        if self.y_speed > 0:
            self.posy = player_rect.top - self.radius
        else:
            self.posy = player_rect.bottom + self.radius
        self.y_speed *= -1

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.direction *= -1
        self.firstTime = 1

    def hit(self, y_speed_paddle):
        self.direction *= -1
        self.y_speed = -y_speed_paddle * self.mass  # Reverse the y_speed based on the paddle's speed and ball's mass
    
    def getRect(self):
        return self.ball

