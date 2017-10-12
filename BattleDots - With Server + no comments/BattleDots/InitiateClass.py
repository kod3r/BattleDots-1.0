'''
Created on Dec 1, 2015

@author: ryan3971
'''

import pygame

class InitiateClass():
    
    WIDTH = 0
    HEIGHT = 0
    DOT_RADIUS = 0
    
    OBSTACLE_AND_POWERUPS_RADIUS = 0
    OBSTACLE_AND_POWERUPS_DIAMETER = 0
    
    MIDDLE_X = 0
    MIDDLE_Y = 0
    
    TOP = 0
    BOTTOM = 0
    LEFT = 0
    RIGHT = 0
        
    def __init__(self):
        
        self.setHeight()
        self.setWidth()
        self.DOT_RADIUS = self.WIDTH / 50
        
        self.OBSTACLE_AND_POWERUPS_RADIUS = self.WIDTH / 50
        self.OBSTACLE_AND_POWERUPS_DIAMETER = self.OBSTACLE_AND_POWERUPS_RADIUS * 2
        
        self.MIDDLE_X = self.WIDTH / 2
        self.MIDDLE_Y = self.HEIGHT / 2
        
        self.TOP = 0
        self.BOTTOM = self.getHeight() * 3
        self.RIGHT = self.getWidth() * 3
        self.LEFT = 0
    
    def setHeight(self):
        
        infoObject = pygame.display.Info()
        self.HEIGHT = infoObject.current_h
        
    def setWidth(self):
        infoObject = pygame.display.Info()
        self.WIDTH = infoObject.current_w
        
    def getHeight(self):
        return self.HEIGHT
        
    def getWidth(self):
        return self.WIDTH
        
    
    