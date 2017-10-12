'''
Created on Dec 19, 2015

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


class MultiLaser():
    
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
        self.LASER_RADIUS = 15
                
    def createMultiLaser(self, dot_location_x, dot_location_y):
        
        pi = 2 * math.pi
        
        angle = random.uniform(0.000000001, pi)
                
        x = math.cos(angle);
        y = math.sin(angle);
        
        x = x * self.LASER_SPEED
        y = y * self.LASER_SPEED
                                                        
        self.LASER_X_MOVE = x
        self.LASER_Y_MOVE = y
        
        start_x = self.MIDDLE_X
        start_y = self.MIDDLE_Y
        
        self.LASER_X_ON_SCREEN_LOCATION = start_x
        self.LASER_Y_ON_SCREEN_LOCATION = start_y
        
        self.LASER_X_COORDINATES = dot_location_x
        self.LASER_Y_COORDINATES = dot_location_y
        
    def updateAndDrawMultiLaser(self, screen, list_num, dot_movement_x, dot_movement_y, manageObjectsObject):
                   
        laser_x = self.LASER_X_ON_SCREEN_LOCATION
        laser_y = self.LASER_Y_ON_SCREEN_LOCATION
            
        laser_x = laser_x + self.LASER_X_MOVE - dot_movement_x
        laser_y = laser_y + self.LASER_Y_MOVE - dot_movement_y
                    
        laser_x = int(laser_x)
        laser_y = int(laser_y)
            
        pygame.draw.circle(screen, [255,255,0], [laser_x, laser_y], self.LASER_RADIUS, 0)

        self.LASER_X_ON_SCREEN_LOCATION = laser_x
        self.LASER_Y_ON_SCREEN_LOCATION = laser_y
                
        self.checkMultiLaserLocation(list_num, manageObjectsObject)
            
    def checkMultiLaserLocation(self, list_num, ManageObjects_Object):
        
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
           
            ManageObjects_Object.removeMultiLaserFromList(list_num) #Gives the go ahead for laser to be remove from the list
            
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
            
            