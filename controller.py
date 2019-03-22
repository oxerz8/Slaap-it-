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
                        self.p2 = Computer("",0)
                else:
        
                        self.p1 = Person(1, 1)
                        self.p2 = Person(2, 2)

        def update_info(self, win, key, ball, mode):
                '''Update the game's state based on the key pressed,
                the Ball, and game mode'''
                
                ball.ball_movement()
                ball.collision(self.p1.paddle)
                ball.collision(self.p2.paddle)
                self.p1.paddle_algo(self.p1.paddle , key, self.p1.usernum)   
                if mode == '1': #mode is player vs computer
                        self.p2.paddle_algo(self.p2.paddle, ball.x, ball.y)

                elif mode == '2': #mode is player vs player
                        self.p2.paddle_algo(self.p2.paddle , key, self.p2.usernum)
                                
                pygame.draw.rect(win, (255, 255, 0) , (self.p1.paddle.x, self.p1.paddle.y, self.p1.paddle.width, self.p1.paddle.height))                
                pygame.draw.rect(win, (255, 0, 0) , (self.p2.paddle.x, self.p2.paddle.y, self.p2.paddle.width, self.p2.paddle.height))

                if ball.x < self.p1.paddle.x:
                    self.p2.update_score()
                    ball.reset()
                elif ball.x > self.p2.paddle.x + self.p2.paddle.width:
                    self.p1.update_score()
                    ball.reset()


#Use multiple constructors to remove the inputs from controller. 
#controller is only getters and setters, no i/o ops
