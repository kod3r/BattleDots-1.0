'''
Created on Dec 19, 2015

@author: ryan3971
'''

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


class TargetBall():
    
    LEFT = 0
    RIGHT = 0
    TOP = 0
    BOTTOM = 0
    
    WIDTH = 0
    HEIGHT = 0
    
    DOT_RADIUS = 0
    
    MIDDLE_X = 0
    MIDDLE_Y = 0
    
    TARGET_BALL_X_MOVE = 0
    TARGET_BALL_Y_MOVE = 0
    TARGET_BALL_X_ON_SCREEN_LOCATION = 0
    TARGET_BALL_Y_ON_SCREEN_LOCATION = 0
    
    TARGET_BALL_X_COORDINATES = 0
    TARGET_BALL_Y_COORDINATES = 0
    
    TARGET_BALL_SPEED = 0
    TARGET_BALL_RADIUS = 0
    
    def __init__(self):
        
        '''
        Initiates variables
        '''
                
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
        
        self.TARGET_BALL_SPEED = 7       #change latter
        self.TARGET_BALL_RADIUS = 30
                
    def createTargetBall(self, dot_location_x, dot_location_y):
        
        '''
            Initiates the TargetBall by assigning variables.
            
            @param dot_location_x: the x-coordinates of the main dot
            @param dot_location_y: the y-coordinates of the main dot
        '''
        
        start_x = self.MIDDLE_X
        start_y = self.MIDDLE_Y
        
        self.TARGET_BALL_X_ON_SCREEN_LOCATION = start_x
        self.TARGET_BALL_Y_ON_SCREEN_LOCATION = start_y
        
        self.TARGET_BALL_X_COORDINATES = dot_location_x
        self.TARGET_BALL_Y_COORDINATES = dot_location_y
        
    def updateAndDrawTargetBall(self, screen, list_num, dot_location_x, dot_location_y, dot_movement_x, dot_movement_y, manageObjectsObject):
        
        '''
            Updates and draws the TargetBalls location
            @param screen: The display variable. Used to allow a multi-laser to be drawn to the screen
            
            @param list_num: he location of the Multi-Laser in the Multi-Laser list
            
            @param dot_location_x: the x-coordinates of the main dot
            @param dot_location_y: the y-coordinates of the main dot
            
            @param dot_movement_x: the instantaneous movement of the dot in the x-axis
            @param dot_movement_y: the instantaneous movement of the dot in the y-axis
            
            @param manageObjectsObject: ManageObjects object, used to call the MangeObjects class

            
        '''
        
        target_ball_screen_x = self.TARGET_BALL_X_ON_SCREEN_LOCATION
        target_ball_screen_y = self.TARGET_BALL_Y_ON_SCREEN_LOCATION
        
        target_ball_coordinates_x = self.TARGET_BALL_X_COORDINATES
        target_ball_coordinates_y = self.TARGET_BALL_Y_COORDINATES

        angle = math.atan2(dot_location_y - target_ball_coordinates_y, dot_location_x - target_ball_coordinates_x)
                      
                      
        x = math.cos(angle) * self.TARGET_BALL_SPEED;
        y = math.sin(angle) * self.TARGET_BALL_SPEED;
        
        target_ball_screen_x = target_ball_screen_x + x - dot_movement_x
        target_ball_screen_y = target_ball_screen_y + y - dot_movement_y
        
        target_ball_coordinates_x = target_ball_coordinates_x + x  # plus sign makes it work
        target_ball_coordinates_y = target_ball_coordinates_y + y 
            
        # all of the adding and subtracting for the previous lines used to make it work. Don't change it!
        
        self.TARGET_BALL_X_ON_SCREEN_LOCATION = target_ball_screen_x
        self.TARGET_BALL_Y_ON_SCREEN_LOCATION = target_ball_screen_y            
        
        self.TARGET_BALL_X_COORDINATES = target_ball_coordinates_x
        self.TARGET_BALL_Y_COORDINATES = target_ball_coordinates_y
        
        
        target_ball_screen_x = int(target_ball_screen_x)
        target_ball_screen_y = int(target_ball_screen_y)
            
        pygame.draw.circle(screen, [100,0,100], [target_ball_screen_x, target_ball_screen_y], self.TARGET_BALL_RADIUS, 0)
