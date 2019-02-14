import pygame
from ball import Ball
from controller import Controller
pygame.init()

win=pygame.display.set_mode((500,500))

pygame.display.set_caption("Slaap it!")

run = True

def redraw_game():
	pygame.draw.circle(win, (0,0,255), (ball.x, ball.y), ball.radius,0)
	controller.update_info(win, key, ball, mode)
	pygame.draw.line(win, (255,255,255),(250,0),(250,500),2)
	pygame.display.update()  

#players=input("Number of players?")

ball = Ball()
controller = Controller(2)
mode='2'

while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			 run=False
	
#	ball.ball_movement()
	key=pygame.key.get_pressed()

	win.fill((0,0,0))	
	redraw_game()

pygame.quit()

#all the data input needs to be done here in view. 

