import pygame

class Paddle:

	def __init__(self, x, y, width=20,height=100,vel=10):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.vel=vel
		self.points=0
#	keys = pygame.key.get_pressed()

	def key_pressed(self, key):

		if (key[pygame.K_UP] or key[pygame.K_w]) and self.y>self.vel:
			self.y-=self.vel

		if (key[pygame.K_DOWN] or key[pygame.K_s]) and self.y<500-self.height-self.vel:
			self.y+=self.vel

