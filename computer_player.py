import pygame
from paddle import Paddle
from user import User
pygame.init()

class Computer(User):

	def __init__(self, name, usernum):
		super().__init__(name,usernum)
		self.name="Computer"
		self.usernum=2
		self.paddle = Paddle(480,250)

	def paddle_algo(self, paddle):
		#need to implement
		pass
