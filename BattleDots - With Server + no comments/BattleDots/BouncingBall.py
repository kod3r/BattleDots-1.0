'''
Created on Dec 9, 2015

@author: ryan3971
'''

import pygame
import random
#import sys
#import math

#from Boundaries import Boundaries
#from Dot import Dot
from InitiateClass import InitiateClass
import math
#from ObstaclesAndPowerUps import ObstaclesAndPowerUps
#from PowerUpVariables import PowerUpVariables


class BouncingBall():

    LEFT = 0
    RIGHT = 0
    TOP = 0
    BOTTOM = 0
    
    WIDTH = 0
    HEIGHT = 0
    
    DOT_RADIUS = 0
    
    MIDDLE_X = 0
    MIDDLE_Y = 0
    
    BALL_X_MOVE = 0
    BALL_Y_MOVE = 0
    BALL_X_ON_SCREEN_LOCATION = 0
    BALL_Y_ON_SCREEN_LOCATION = 0
    
    BALL_X_COORDINATES = 0
    BALL_Y_COORDINATES = 0
    
    BALL_SPEED = 0
    BALL_RADIUS = 0
    
    ADJUSTED_X = 0
    ADJUSTED_Y = 0

    
    def __init__(self):
                
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        self.MIDDLE_Y = self.initiateClass.MIDDLE_Y
        self.MIDDLE_X = self.initiateClass.MIDDLE_X
        self.DOT_RADIUS = self.initiateClass.DOT_RADIUS
        
        self.TOP = self.initiateClass.TOP
        self.BOTTOM = self.initiateClass.BOTTOM
        self.RIGHT = self.initiateClass.RIGHT
        self.LEFT = self.initiateClass.LEFT
        
        self.BALL_SPEED = 10       #change latter
        self.BALL_RADIUS = self.WIDTH / 50
                
    def createBall(self, dot_location_x, dot_location_y):
        
        two_pi = 2 * math.pi
        
        angle = random.uniform(0, two_pi)
                
        x = math.cos(angle);
        y = math.sin(angle);
               
        x = x * self.BALL_SPEED
        y = y * self.BALL_SPEED
        
        self.BALL_X_MOVE = x
        self.BALL_Y_MOVE = y
        
        self.BALL_X_COORDINATES = dot_location_x
        self.BALL_Y_COORDINATES = dot_location_y
        
        self.START_X = dot_location_x
        self.START_Y = dot_location_y
        
        self.ADJUSTED_X = 0
        self.ADJUSTED_Y = 0
        
    def updateAndDrawBall(self, screen, instantaneous_movement_x, instantaneous_movement_y):
        
        
        self.ADJUSTED_X -= instantaneous_movement_x
        self.ADJUSTED_Y -= instantaneous_movement_y
        
        x = self.BALL_X_COORDINATES - self.START_X
        y = self.BALL_Y_COORDINATES - self.START_Y
        
        x = x + self.MIDDLE_X
        y = y + self.MIDDLE_Y
        
        x = x + self.ADJUSTED_X
        y = y + self.ADJUSTED_Y
        
        ball_x_int = int(x)
        ball_y_int = int(y)
            
        pygame.draw.circle(screen, [255,0,255], [ball_x_int, ball_y_int], self.BALL_RADIUS, 0)

        self.checkBallLocation()
            
    def checkBallLocation(self):
        
        next_ball_x_coordinates = self.BALL_X_COORDINATES + self.BALL_X_MOVE
        next_ball_y_coordinates = self.BALL_Y_COORDINATES + self.BALL_Y_MOVE

        
        TOP = (self.TOP + self.BALL_RADIUS)
        BOTTOM = (self.BOTTOM - self.BALL_RADIUS)
        RIGHT = (self.RIGHT - self.BALL_RADIUS)
        LEFT = (self.LEFT + self.BALL_RADIUS)
                
        
        if (next_ball_y_coordinates > BOTTOM):
            next_ball_y_coordinates = 2*(BOTTOM) - next_ball_y_coordinates;
            self.BALL_Y_MOVE = -abs(self.BALL_Y_MOVE);
      
        elif (next_ball_y_coordinates < TOP):
            next_ball_y_coordinates = 2*(TOP) - next_ball_y_coordinates;
            self.BALL_Y_MOVE = abs(self.BALL_Y_MOVE);
      
        if (next_ball_x_coordinates < LEFT):
            next_ball_x_coordinates = 2*(LEFT) - next_ball_x_coordinates;
            self.BALL_X_MOVE = abs(self.BALL_X_MOVE);
      
        elif (next_ball_x_coordinates > RIGHT):
            next_ball_x_coordinates = 2*(RIGHT) - next_ball_x_coordinates;
            self.BALL_X_MOVE = -abs(self.BALL_X_MOVE);
            
        self.BALL_Y_COORDINATES = next_ball_y_coordinates
        self.BALL_X_COORDINATES = next_ball_x_coordinates
 
            
