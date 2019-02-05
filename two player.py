import pygame
from paddle import Paddle
from ball import Ball
pygame.init()

win=pygame.display.set_mode((500,500))

pygame.display.set_caption("Ping pong")

run = True

p1=Paddle(480,250)
p2=Paddle(20,250)
ball = Ball()

def redraw_game():
	pygame.draw.line(win, (255,255,255),(250,0),(250,500),2)
	pygame.draw.rect(win, (255, 255, 0) , (p1.x, p1.y, p1.width, p1.height))
	pygame.draw.rect(win, (255, 0, 0) , (p2.x, p2.y, p2.width, p2.height))
	pygame.draw.circle(win, (0,0,255), (ball.x, ball.y), ball.radius,0)	
	pygame.display.update()  

def score(p1, p2, ball):
	if(ball.x>495):
		p1.points+=1
#		print(p1.points)
		return True
	elif(ball.x<5):
		p2.points+=1
#		print(p2.points)
		return True
	return False

while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			 run=False

	key1 = pygame.key.get_pressed()
	key2 = pygame.key.get_pressed()
	if key1[pygame.K_UP] or key1[pygame.K_DOWN]:
		p1.key_pressed(key1)
	
	if key2[pygame.K_w] or key2[pygame.K_s]:	
		p2.key_pressed(key2)

	ball.ball_movement()
	ball.collision(p1)
	ball.collision(p2)
	if(score(p1,p2,ball)):
		ball.x=250
		ball.y=450

	if(p1.points==5):
		print("Player 2 won!")
		pygame.quit()
	elif(p2.points==5):
		print("Player 1 won!")
		pygame.quit()		
	win.fill((0,0,0))	
	redraw_game()

pygame.quit()

