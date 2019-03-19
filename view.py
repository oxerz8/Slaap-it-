import pygame
from ball import Ball
from controller import Controller
pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Slaap It!")
run = False

ball = Ball()
controller = Controller(2)

#Title
title = pygame.font.SysFont("Verdana", 60)
window.blit(title.render("Slaap It!", True, (255, 255, 255)), (120, 20))


#Button Look
button_text = pygame.font.SysFont("Arial", 30)
menu_options = ["Single Player", "Two Player", "Quit Game"]

button1 = pygame.draw.rect(window, (255, 0, 0), (150, 130, 200, 50))
button2 = pygame.draw.rect(window, (0, 69, 255), (150, 190, 200, 50))
button3 = pygame.draw.rect(window, (50, 255, 50), (150, 250, 200, 50))

text_ypos = 135
for option in menu_options:
        window.blit(button_text.render(option, True, (255, 255, 255)), (170, text_ypos))
        text_ypos += 60

pygame.display.update()

#Main Menu
while not run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit
        
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if clicked[0] and button1.collidepoint(mouse_pos):
                mode = '1'
                #TODO: Implement button when Single Player game mode is complete
                pass
        elif clicked[0] and button2.collidepoint(mouse_pos):
                mode = '2'
                run = True
        elif clicked[0] and button3.collidepoint(mouse_pos):
                pygame.quit()


#Running Game
def redraw_game():
        window.fill((0, 0, 0))
        key = pygame.key.get_pressed()
        pygame.draw.circle(window, (0, 0, 255), (ball.x, ball.y), ball.radius,0)
        controller.update_info(window, key, ball, mode)
        i = 0
        while i < 500:
                pygame.draw.line(window, (255, 255, 255),(250, i),(250, i + 50),2)
                i = i + 75
        pygame.display.update()

while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run=False
        
        redraw_game()

pygame.quit()

#all the data input needs to be done here in view. 

