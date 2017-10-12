'''
Created on Dec 1, 2015

@author: ryan3971
'''

import pygame
#import random
#import sys
#import math

#from Boundaries import Boundaries
from InitiateClass import InitiateClass
#from ManageObjects import ManageObjects
#from ObstaclesAndPowerUps import ObstaclesAndPowerUps
from PowerUpVariables import PowerUpVariables
#from shootLaser import shootLaser

class Dot():#, pygame.sprite.Sprite):
    
    WIDTH = 0
    HEIGHT = 0
    MIDDLE_X = 0
    MIDDLE_Y = 0
    DOT_RADIUS = 0
    
    PowerUpVariables = None
    
    def __init__(self, PowerUpVariables):
        
        '''
        Initiates variables
        
        @param PowerUpVariables: passes the PowerUpVariables object
        '''
        
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        self.DOT_RADIUS = self.initiateClass.DOT_RADIUS
        
        self.MIDDLE_Y = self.initiateClass.MIDDLE_Y
        self.MIDDLE_X = self.initiateClass.MIDDLE_X
        
        self.PowerUpVariables = PowerUpVariables
        
    
    def drawDot(self, screen):
        
        '''
        Draw's the dot with updated size and power ups, if any.
        @param screen: The display variable. Used to allow the dot to be drawn to the screen
        '''
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
        
        if self.PowerUpVariables.getDotInvisible() == True:
            dot_color = [255, 125, 125]
        elif self.PowerUpVariables.getDotInvisible() == False:
            dot_color = [255, 0, 0]
                        
        if self.PowerUpVariables.getDotSheild() == True:
            sheild_radius = int(dot_radius * 1.5)
            pygame.draw.circle(screen, [0, 0, 255], [self.MIDDLE_X, self.MIDDLE_Y], sheild_radius, 0)
        
        
        pygame.draw.circle(screen, dot_color, [self.MIDDLE_X, self.MIDDLE_Y], dot_radius, 0)
        