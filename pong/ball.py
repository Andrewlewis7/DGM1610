import pygame
from settings import WIDTH, HEIGHT, screen, GRAVITY, STOP_BOUNCE
class Ball:
    
    def __init__(self, posx, posy, radius, color, y_speed, x_speed,  mass, retention, friction):
        
        self.posx = posx
        self.posy = posy
        self.radius = radius
        #self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.friction = friction
 
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
        if (self.posx < self.radius and self.x_speed < 0) or \
                (self.posx > WIDTH - self.radius - self.x_speed > 0):
            self.x_speed *= -1 * self.retention
            if abs(self.x_speed) < STOP_BOUNCE:
                self.x_speed = 0
        if self.y_speed == 0 and self.x_speed != 0:
            if self.x_speed > 0:
                self.x_speed -= self.friction
            elif self.x_speed < 0:
                self.x_speed += self.friction
        else:
            self.x_speed = x_push
            self.y_speed = y_push
        return self.y_speed
    
 
    def update(self):
        self.posx += self.x_speed*self.xFac
        self.posy += self.y_speed*self.yFac
 
        # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and
        # it results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
 
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
 
    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.xFac *= -1
        self.firstTime = 1
 
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
 
    def getRect(self):
        return self.ball


#-----------------------------------
