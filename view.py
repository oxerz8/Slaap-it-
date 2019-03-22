import pygame
from ball import Ball
from controller import Controller

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("background_music.mp3") 
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Slaap It!")
run = False

ball = Ball((pygame.display.get_surface().get_width()//2),
            (pygame.display.get_surface().get_height()//2))

#Title
title = pygame.font.SysFont("Verdana", 60)
window.blit(title.render("Slaap It!", True, (255, 255, 255)), (120, 20))

#Button Look
button_text = pygame.font.SysFont("Arial", 30)
menu_options = ["Single  Player", "  Two Player", "  Quit Game"]

button1 = pygame.draw.rect(window, (255, 0, 0), (150, 130, 200, 50))
button2 = pygame.draw.rect(window, (0, 69, 255), (150, 190, 200, 50))
button3 = pygame.draw.rect(window, (50, 255, 50), (150, 250, 200, 50))

text_ypos = 135
for option in menu_options:
        window.blit(button_text.render(option, True, (255, 255, 255)), (170, text_ypos))
        text_ypos += 60

pygame.display.update()

#Scores
score_text = pygame.font.SysFont("Verdana", 40)
win_message = ""


#Main Menu
while not run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if clicked[0] and button1.collidepoint(mouse_pos):
                mode = '1'
                controller = Controller(1);
                run = True
        elif clicked[0] and button2.collidepoint(mouse_pos):
                mode = '2'
                controller = Controller(2);
                run = True
        elif clicked[0] and button3.collidepoint(mouse_pos):
                pygame.quit()



#Running Game
def redraw_game():
        '''Update the window to show the game's current state'''
        
        window.fill((0, 0, 0))
        key = pygame.key.get_pressed()
        pygame.draw.circle(window, (0, 0, 255), (ball.x, ball.y), ball.radius, 0)
        
        controller.update_info(window, key, ball, mode)

        window.blit(score_text.render(str(controller.p1.score), True, (255, 255, 255)), (125, 20))
        window.blit(score_text.render(str(controller.p2.score), True, (255, 255, 255)), (375, 20))
        
        line_y_pos = 0
        while line_y_pos < 500: #draw a dotted line
                pygame.draw.line(window, (255, 255, 255),(250, line_y_pos),(250, line_y_pos + 50) , 2)
                line_y_pos += 75
        pygame.display.update()

while run:
        pygame.time.delay(50)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        
        redraw_game()

        if (controller.p1.score >= 5):
                win_message = "Player 1 won!"
                run = False
        elif (mode == '2' and controller.p2.score >= 5):
                win_message = "Player 2 won!"
                run = False
        elif (mode == '1' and controller.p2.score >= 5):
                win_message = "You  lost  :("
                run = False

winner_text = pygame.font.SysFont("Verdana", 30)
window.blit(winner_text.render(win_message, True, (0, 0, 255)), (150, 220))
quit_button = pygame.draw.rect(window, (255, 0, 0), (150, 350, 190, 50))
window.blit(button_text.render("Quit Game", True, (255, 255, 255)), (187, 357))
pygame.display.update()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if clicked[0] and quit_button.collidepoint(mouse_pos):
                pygame.quit()

#all the data input needs to be done here in view. 
