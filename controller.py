import pygame
from ball import Ball
from person_player import Person
from computer_player import Computer
class Controller:

        def __init__(self, players):
                '''Initialize the players based on the players
                number given'''
                
                if players == 1 : 
                        
                        self.p1 = Person(1,1)
                        self.c1 = Computer("",0)
                else:
        
                        self.p1 = Person(1, 1)
                        self.p2 = Person(2, 2)

        def update_info(self, win, key, ball, mode):
                '''Update the game's state based on the key pressed,
                the Ball, and game mode'''
                
                ball.ball_movement()
                ball.collision(self.p1.paddle)
                if mode == '1': #mode is player vs computer
                        ball.collision(self.c1.paddle)
                        if (self.p1):
                                ball.collision(self.p1.paddle)
                                ball.collision(self.c1.paddle)
                                self.p1.paddle_algo(self.p1.paddle , key, self.p1.usernum)    
                        if (self.c1):
                                ball.collision(self.p1.paddle)
                                ball.collision(self.c1.paddle)
                                self.c1.paddle_algo(self.c1.paddle, ball.x, ball.y)

                elif mode == '2': #mode is player vs player
                        ball.collision(self.p2.paddle)
                        if(self.p1): 
                                ball.collision(self.p1.paddle)
                                ball.collision(self.p2.paddle)
                                self.p1.paddle_algo(self.p1.paddle , key, self.p1.usernum)
                        if (self.p2):
                                ball.collision(self.p1.paddle)
                                ball.collision(self.p2.paddle)
                                self.p2.paddle_algo(self.p2.paddle , key, self.p2.usernum)
                                
                pygame.draw.rect(win, (255, 255, 0) , (self.p1.paddle.x, self.p1.paddle.y, self.p1.paddle.width, self.p1.paddle.height))                
                if(mode == '2'):
                        pygame.draw.rect(win, (255, 0, 0) , (self.p2.paddle.x, self.p2.paddle.y, self.p2.paddle.width, self.p2.paddle.height))
                elif(mode == '1'):
                        pygame.draw.rect(win, (255, 0, 0) , (self.c1.paddle.x, self.c1.paddle.y, self.c1.paddle.width, self.c1.paddle.height))

                if ball.x < self.p1.paddle.x + self.p1.paddle.width and mode == '2':
                    self.p2.update_score()
                    ball.reset()
                elif ball.x < self.p1.paddle.x + self.p1.paddle.width and mode == '1':
                    self.c1.update_score()
                    ball.reset()
                elif ball.x > 490:
                    self.p1.update_score()
                    ball.reset()


#Use multiple constructors to remove the inputs from controller. 
#controller is only getters and setters, no i/o ops
