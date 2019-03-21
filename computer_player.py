import pygame
from paddle import Paddle
from user import User
pygame.init()

class Computer(User):

        def __init__(self, name, usernum):
                '''Initializes a Computer player'''

                super().__init__(name,usernum)
                self.name="Computer"
                self.usernum=2
                self.paddle = Paddle(480,250)

        
        def paddle_algo(self, paddle, ball_y):
                ''' Move the Paddle up or down based on the y-value of the ball.
                The location is given by ball_y. This function returns void.'''
                
                if ball_y<self.paddle.y and self.paddle.y>self.paddle.vel:
                        self.paddle.y-=self.paddle.vel
                elif ball_y>self.paddle.y and self.paddle.y<500-self.paddle.height-self.paddle.vel:
                        self.paddle.y+=self.paddle.vel
