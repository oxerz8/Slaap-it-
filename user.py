import pygame
from paddle import Paddle
pygame.init()

class User:
        
        def __init__(self, name, usernum):
                '''Initializes the User'''
                
                self.name = name
                self.score = 0
                self.usernum = usernum

        def paddle_algo(self, paddle):
                '''Defines how the User will
                control the Paddle'''
                
                pass

        def update_score(self):
                '''Increments the user's score'''
                
                self.score += 1
