'''
Created on Dec 1, 2015

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


class shootLaser():
    
    LEFT = 0
    RIGHT = 0
    TOP = 0
    BOTTOM = 0
    
    WIDTH = 0
    HEIGHT = 0
    
    DOT_RADIUS = 0
    
    MIDDLE_X = 0
    MIDDLE_Y = 0
    
    LASER_X_MOVE = 0
    LASER_Y_MOVE = 0
    LASER_X_ON_SCREEN_LOCATION = 0
    LASER_Y_ON_SCREEN_LOCATION = 0
    
    LASER_X_COORDINATES = 0
    LASER_Y_COORDINATES = 0
    
    LASER_SPEED = 0
    LASER_RADIUS = 0
    
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
        
        self.LASER_SPEED = 10       #change latter
        self.LASER_RADIUS = 30
                
    def createLaser(self, dot_location_x, dot_location_y):
        
        two_pi = 2 * math.pi
        
        angle = random.uniform(0, two_pi)
                
        x = math.cos(angle);
        y = math.sin(angle);
               
        x = x * self.LASER_SPEED
        y = y * self.LASER_SPEED
        
        self.LASER_X_MOVE = x
        self.LASER_Y_MOVE = y
        
        self.LASER_X_COORDINATES = dot_location_x
        self.LASER_Y_COORDINATES = dot_location_y
        
        self.START_X = dot_location_x
        self.START_Y = dot_location_y
        
        self.ADJUSTED_X = 0
        self.ADJUSTED_Y = 0
        
    def updateAndDrawLaser(self, screen, list_num, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object):
                   
        self.ADJUSTED_X -= instantaneous_movement_x
        self.ADJUSTED_Y -= instantaneous_movement_y
        
        x = self.LASER_X_COORDINATES - self.START_X
        y = self.LASER_Y_COORDINATES - self.START_Y
        
        x = x + self.MIDDLE_X
        y = y + self.MIDDLE_Y
        
        x = x + self.ADJUSTED_X
        y = y + self.ADJUSTED_Y
        
        ball_x_int = int(x)
        ball_y_int = int(y)
            
        pygame.draw.circle(screen, [0,0,0], [ball_x_int, ball_y_int], self.LASER_RADIUS, 0)

        self.checkLaserLocation(list_num, ManageObjects_Object)
            
    def checkLaserLocation(self, list_num, ManageObjects_Object):
        
        laser_x_coordinates = self.LASER_X_COORDINATES
        laser_y_coordinates = self.LASER_Y_COORDINATES
                    
        next_laser_x_coordinates = self.LASER_X_COORDINATES + self.LASER_X_MOVE
        next_laser_y_coordinates = self.LASER_Y_COORDINATES + self.LASER_Y_MOVE
            
        TOP = (self.TOP + self.LASER_RADIUS)
        BOTTOM = (self.BOTTOM - self.LASER_RADIUS)
        RIGHT = (self.RIGHT - self.LASER_RADIUS)
        LEFT = (self.LEFT + self.LASER_RADIUS)
            
        if (laser_y_coordinates == TOP or laser_y_coordinates == BOTTOM
            or laser_x_coordinates == RIGHT or laser_x_coordinates == LEFT):
           
            ManageObjects_Object.removeLaserFromList(list_num) #Gives the go ahead for laser to be remove from the list
            
        elif (next_laser_y_coordinates <= TOP or next_laser_y_coordinates >= BOTTOM
            or next_laser_x_coordinates >= RIGHT or next_laser_x_coordinates <= LEFT):
            
            if next_laser_x_coordinates >= RIGHT:
                laser_x_coordinates = RIGHT
                
            if next_laser_x_coordinates <= LEFT:
                laser_x_coordinates = LEFT
                
            if next_laser_y_coordinates <= TOP:
                laser_y_coordinates = TOP
                
            if next_laser_y_coordinates >= BOTTOM:
                laser_y_coordinates = BOTTOM
                

            self.LASER_X_COORDINATES = laser_x_coordinates
            self.LASER_Y_COORDINATES = laser_y_coordinates
        
        else:
            self.LASER_X_COORDINATES = next_laser_x_coordinates
            self.LASER_Y_COORDINATES = next_laser_y_coordinates
            
            
            
            
'''  when doing adjustment, nothing is done or variable not being adjusted'''