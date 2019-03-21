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
	
	def paddle_algo(self, paddle, ball_x, ball_y):
		""" Move self.paddle up or down based on the y-value of the ball, if the ball is on the left side of the board.
		The location of the ball is given by (ball_x, ball_y) 
		This function returns void. 	
		"""
		
		if ball_x >= 250:
			if ball_y < self.paddle.y and self.paddle.y > self.paddle.vel:
				self.paddle.y -= self.paddle.vel
			elif ball_y > self.paddle.y and self.paddle.y < 500-self.paddle.height-self.paddle.vel:
				self.paddle.y += self.paddle.vel

	def update_score(self):
		self.score += 1
