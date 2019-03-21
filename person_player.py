import pygame
from paddle import Paddle
from user import User
pygame.init()

class Person(User):

        def __init__(self, name, usernum):
                '''Initialize a Person to control a Paddle'''
                super().__init__(name, usernum)
                if self.usernum == 1:
                        self.paddle = Paddle(10,250)
                else:
                        self.paddle = Paddle(480,250)

        def paddle_algo(self, paddle, key, usernum):
                '''Define the Paddle movement based on key pressed
                and usernum'''
                
                if usernum == 1:
                        if key[pygame.K_w] and self.paddle.y > 0:
                                self.paddle.y -= self.paddle.vel

                        elif key[pygame.K_s] and self.paddle.y < pygame.display.get_surface().get_height() - self.paddle.height:
                                self.paddle.y += self.paddle.vel

                elif usernum == 2:
                        if key[pygame.K_UP] and self.paddle.y > 0:
                                self.paddle.y -= self.paddle.vel

                        elif key[pygame.K_DOWN] and self.paddle.y < pygame.display.get_surface().get_height() - self.paddle.height:
                                self.paddle.y += self.paddle.vel

