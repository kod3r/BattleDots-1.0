'''
Created on Dec 23, 2015

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
from ClientVariables import ClientVariables

class Dot_2(ClientVariables):#, pygame.sprite.Sprite):
    
    WIDTH = 0
    HEIGHT = 0
    MIDDLE_X = 0
    MIDDLE_Y = 0
    DOT_RADIUS = 0
    
    PowerUpVariables = None
    
    def __init__(self, PowerUpVariables):#, client):
        
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        self.DOT_RADIUS = self.initiateClass.DOT_RADIUS
        
        self.MIDDLE_Y = self.initiateClass.MIDDLE_Y
        self.MIDDLE_X = self.initiateClass.MIDDLE_X
        
        self.PowerUpVariables = PowerUpVariables
        
     #   self.CLIENT = client
        self.CV = ClientVariables
    
    def drawDot2(self, screen, dot_1_x, dot_1_y):
        
        dot_radius = int(self.DOT_RADIUS * self.CV.DOT_2_SIZE)
        
        dot_2_on_screen_location_x = (self.CV.DOT_2_X - dot_1_x) + self.MIDDLE_X
        dot_2_on_screen_location_y = (self.CV.DOT_2_Y - dot_1_y) + self.MIDDLE_Y
        
        
        dot_2_on_screen_location_x = int(dot_2_on_screen_location_x)
        dot_2_on_screen_location_y = int(dot_2_on_screen_location_y)
        
        if self.CV.DOT_2_INVISIBLE == True:
            dot_color = [255, 255, 255]
        elif self.CV.DOT_2_INVISIBLE == False:
            dot_color = [255, 0, 0]
                        
        if self.CV.DOT_2_SHEILD == True and self.CV.DOT_2_INVISIBLE == False:
            sheild_radius = int(dot_radius * 1.5)
            pygame.draw.circle(screen, [0, 0, 255], [dot_2_on_screen_location_x, dot_2_on_screen_location_y], sheild_radius, 0)
        
        
        pygame.draw.circle(screen, dot_color, [dot_2_on_screen_location_x, dot_2_on_screen_location_y], dot_radius, 0)
        