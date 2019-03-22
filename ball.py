
import pygame
from paddle import Paddle

class Ball:
        
        def __init__(self, x, y, r=10, xvel=10, yvel=10):
                '''Initialize a Ball with center (x,y),
                radius r, x-velocity xvel, and y-velocity yvel'''
        
                self.x = x
                self.y = y
                self.radius = r
                self.xvel = xvel
                self.yvel = yvel

        def ball_movement(self):
                '''Implements ball movement

                The Ball's moveset can be extended by perhaps adding a timer and
                increasing the Ball's x and y velocities after a certain amount of
                time has passed'''
                
                if self.xvel != 0:
                        self.x += self.xvel
                        
                if self.yvel != 0:
                        self.y += self.yvel
                        if(self.y == pygame.display.get_surface().get_height() - self.radius
                           or self.y == self.radius):
                                self.yvel = -self.yvel

        def reset(self):
                '''Centers the ball in the middle of the screen and
                negates its x-velocity, keeping y-velocity the same'''
                
                self.x = pygame.display.get_surface().get_width()//2
                self.y = pygame.display.get_surface().get_height()//2
                self.xvel = -self.xvel
                self.yvel = self.yvel
                
        def collision(self, paddle):
                '''Sets the Ball's reaction to colliding with the Paddle paddle'''
                
                if paddle.x > pygame.display.get_surface().get_width() // 2: #right paddle
                        if ((self.x + self.radius == paddle.x) and
                            (self.y in range(paddle.y - self.radius, paddle.y + paddle.height + self.radius))):

                            self.xvel = -self.xvel

                else: #left paddle
                        if ((self.x - self.radius == paddle.x + paddle.width) and
                            (self.y in range(paddle.y - self.radius, paddle.y + paddle.height + self.radius))):

                            self.xvel = -self.xvel
                            

                            
                        

                



