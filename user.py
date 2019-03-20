import pygame
from paddle import Paddle
pygame.init()

class User:
	
	def __init__(self, name, usernum):
		self.name=name
		self.score=0
		self.usernum=usernum

	def paddle_algo(self, paddle):
		pass

	def update_score(self):
                self.score += 1
