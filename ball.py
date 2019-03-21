
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
                        if(self.yvel>0):
                                self.y+=self.yvel
                                if(self.y==490):
                                        self.yvel=-self.yvel

                        elif(self.yvel<0):
                                self.y+=self.yvel
                                if(self.y==10):
                                        self.yvel=-self.yvel

                elif(self.xvel<0):
                        self.x+=self.xvel
                        if(self.yvel>0):
                                self.y+=self.yvel
                                if self.y==490:
                                        self.yvel=-self.yvel

                        elif(self.yvel<0):
                                self.y+=self.yvel
                                if self.y==10:
                                        self.yvel=-self.yvel

        def reset(self):
                self.x = 250
                self.y = 450
                self.xvel = -self.xvel
                self.yvel = self.yvel
                
        def collision(self, paddle):            
                if(paddle.x>250):
                        if(self.y in range(paddle.y,paddle.y+30)) and (self.x+self.radius==paddle.x):
                                self.xvel=-self.xvel

                        elif(self.y in range(paddle.y+30,paddle.y+60)) and (self.x+self.radius==paddle.x):
                                self.xvel=-self.xvel

                        elif(self.y in range(paddle.y+60,paddle.y+paddle.height)) and (self.x+self.radius==paddle.x):
                                self.xvel=-self.xvel

                        elif(self.x in range(paddle.x, paddle.x+paddle.width)) and (self.y+self.radius == paddle.y):
                                self.yvel=-self.yvel

                        elif(self.x in range(paddle.x, paddle.x+paddle.width)) and (self.y-self.radius == paddle.y+paddle.height):
                                self.yvel=-self.yvel

                        elif(paddle.x in range(self.x+(int)(self.radius/1.41), self.x+(int)(self.radius/1.42))):
                                if(paddle.y in range(self.y+(int)(self.radius/1.41), self.y+(int)(self.radius/1.42))):
                                        self.xvel=-self.xvel
                                        self.yvel=-self.yvel

                        elif(paddle.x in range(self.x+(int)(self.radius/1.41), self.x+(int)(self.radius/1.42))):
                                if(paddle.y+paddle.height in range(self.y-(int)(self.radius/1.41), self.y-(int)(self.radius/1.42))):
                                        self.xvel=-self.xvel
                                        self.yvel=-self.yvel

                else:           
                        if(self.y in range(paddle.y,paddle.y+30)) and (self.x-self.radius==paddle.x+paddle.width):
                                self.xvel=-self.xvel

                        elif(self.y in range(paddle.y+30,paddle.y+60)) and (self.x-self.radius==paddle.x+paddle.width):
                                self.xvel=-self.xvel

                        elif(self.y in range(paddle.y+60,paddle.y+paddle.height)) and (self.x-self.radius==paddle.x+paddle.width):
                                self.xvel=-self.xvel

                        elif(self.x in range(paddle.x, paddle.x+paddle.width)) and (self.y+self.radius == paddle.y):
                                self.yvel=-self.yvel

                        elif(self.x in range(paddle.x, paddle.x+paddle.width)) and (self.y-self.radius == paddle.y+paddle.height):
                                self.yvel=-self.yvel

                        elif(paddle.x+paddle.width in range(self.x+(int)(self.radius/1.41), self.x+(int)(self.radius/1.42))):
                                if(paddle.y in range(self.y+(int)(self.radius/1.41), self.y+(int)(self.radius/1.42))):
                                        self.xvel=-self.xvel
                                        self.yvel=-self.yvel

                        elif(paddle.x+paddle.width in range(self.x+(int)(self.radius/1.41), self.x+(int)(self.radius/1.42))):
                                if(paddle.y+paddle.height in range(self.y-(int)(self.radius/1.41), self.y-(int)(self.radius/1.42))):
                                        self.xvel=-self.xvel
                                        self.yvel=-self.yvel



