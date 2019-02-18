import pygame
from paddle import Paddle

class Ball:
	
	def __init__(self, xvel=10,yvel=10):
		self.x=250
		self.y=450
		self.radius=10
		self.xvel=xvel
		self.yvel=xvel

	def ball_movement(self):
		
		if(self.xvel>0):
			self.x+=self.xvel

		if(self.xvel<0):
			self.x+=self.xvel
	
		if(self.yvel>0):
			self.y+=self.yvel
			if self.y==490:
				self.yvel=-self.yvel

		if(self.yvel<0):
			self.y+=self.yvel
			if self.y==20:
				self.yvel=-self.yvel


	def collision(self, paddle):		#incomplete

		if(paddle.x>250): 		
			if(self.y in range(paddle.y,paddle.y+30)) and (self.x+self.radius==paddle.x-paddle.width):
				self.xvel=-self.xvel

			if(self.y in range(paddle.y+30,paddle.y+60)) and (self.x+self.radius==paddle.x-paddle.width):
				self.xvel=-self.xvel
		
			if(self.y in range(paddle.y+60,paddle.y+90)) and (self.x+self.radius==paddle.x-paddle.width):
				self.xvel=-self.xvel

		else:		
			if(self.y in range(paddle.y,paddle.y+30)) and (self.x-self.radius==paddle.x+paddle.width):
				self.xvel=-self.xvel

			if(self.y in range(paddle.y+30,paddle.y+60)) and (self.x-self.radius==paddle.x+paddle.width):
				self.xvel=-self.xvel
		
			if(self.y in range(paddle.y+60,paddle.y+90)) and (self.x-self.radius==paddle.x+paddle.width):
				self.xvel=-self.xvel


