'''
Created on Dec 19, 2015

@author: ryan3971
'''

import pygame
from InitiateClass import InitiateClass

class PowerWave():
    
    def __init__(self, dot_location_x, dot_location_y, screen):
        
        '''
        Initiates variable
        
        
        @param dot_location_x: the x-coordinates of the main dot
        @param dot_location_y: the y-coordinates of the main dot
        @param PowerUpVariables: passes the PowerUpVariables object
        '''
        
        self.CENTER_WAVE_X = dot_location_x     #used or determineing collision with other player
        self.CENTER_WAVE_Y = dot_location_y
        
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        self.DOT_RADIUS = self.initiateClass.DOT_RADIUS
        self.MIDDLE_Y = self.initiateClass.MIDDLE_Y
        self.MIDDLE_X = self.initiateClass.MIDDLE_X
        
        self.SCREEN = screen
        self.WAVE_RADIUS = 0
        self.WAVE_BORDER = 10
        self.WAVE_COLOR = [0, 255, 150]
        
    def drawWave(self, dot_movement_x, dot_movement_y):
        
        '''
        Draw the PowerWave
        '''
        
        self.WAVE_RADIUS += 10
        
        self.MIDDLE_X -= dot_movement_x
        self.MIDDLE_Y -= dot_movement_y
        
        wave_x = int(self.MIDDLE_X)
        wave_y = int(self.MIDDLE_Y)
        
        pygame.draw.circle(self.SCREEN, self.WAVE_COLOR, [wave_x, wave_y], self.WAVE_RADIUS, self.WAVE_BORDER)

        if self.WAVE_RADIUS * 2 >= self.WIDTH:
            return True
        else:
            return False