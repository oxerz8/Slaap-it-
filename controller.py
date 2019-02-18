import pygame
from ball import Ball
from person_player import Person
from computer_player import Computer
class Controller:

	def __init__(self, players):
		
		if(players==1): #Not done yet
			#name1=input("Enter p1 name:")
			self.p1=Person(1,1)
			self.c1=Computer("",0)
		else:
			#name1=input("Enter p1 name:")
			#name2=input("Enter p2 name:")
			self.p1=Person(1, 1)
			self.p2=Person(2, 2)

	def update_info(self, win, key, ball, mode):
		
		ball.ball_movement()
		ball.collision(self.p1.paddle)

		if mode == '1': #mode is player vs computer
			if(self.p1!=None): 
				ball.collision(self.p2.paddle)
				self.p1.paddle_algo(self.p1.paddle , key, self.p1.usernum)
			if(self.p2!=None):
				self.p2.paddle_algo(self.p2.paddle, ball.y)	
		if mode == '2': #mode is player vs player
			if(self.p2!=None): 
				ball.collision(self.p2.paddle)
				self.p1.paddle_algo(self.p1.paddle , key, self.p1.usernum)
			if (self.p2!=None):
				self.p2.paddle_algo(self.p2.paddle , key, self.p2.usernum)
			pygame.draw.rect(win, (255, 255, 0) , (self.p1.paddle.x, self.p1.paddle.y, self.p1.paddle.width, self.p1.paddle.height))		
			if(self.p2): pygame.draw.rect(win, (255, 0, 0) , (self.p2.paddle.x, self.p2.paddle.y, self.p2.paddle.width, self.p2.paddle.height))		
		#pygame.draw.circle(win, (0,0,255), (ball.x, ball.y), ball.radius,0)	


#Use multiple constructors to remove the inputs from controller. 
#controller is only getters and setters, no i/o ops
#init the ball here?
