'''
Created on Dec 1, 2015

@author: ryan3971
'''

import pygame
#import random
#import sys
import math

#from Dot import Dot
from InitiateClass import InitiateClass
#from ManageObjects import ManageObjects
#from ObstaclesAndPowerUps import ObstaclesAndPowerUps
from PowerUpVariables import PowerUpVariables
#from shootLaser import shootLaser

class Boundaries():

    LEFT = 0
    RIGHT = 0
    TOP = 0
    BOTTOM = 0
    OBSTACLE_AND_POWERUPS_MOVEMENT_X = 0
    OBSTACLE_AND_POWERUPS_MOVEMENT_Y = 0
    
    WIDTH = 0
    HEIGHT = 0
    MIDDLE_X = 0
    MIDDLE_Y = 0
    DOT_RADIUS = 0
    
    IS_MAX_TOP = False
    IS_MAX_BOTTOM = False
    IS_MAX_LEFT = False
    IS_MAX_RIGHT = False
    
    PowerUpVariables = None

    DOT_X = 0
    DOT_Y = 0
    
    OBSTACLE_AND_POWERUPS_DIAMETER = 0
    
    INSTANTANEOUS_MOVEMENT_X = 0
    INSTANTANEOUS_MOVEMENT_y = 0
    
    def __init__(self, PowerUpVariables):
                
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        self.DOT_RADIUS = self.initiateClass.DOT_RADIUS
        self.MIDDLE_Y = self.initiateClass.MIDDLE_Y
        self.MIDDLE_X = self.initiateClass.MIDDLE_X
        
        self.PowerUpVariables = PowerUpVariables
        
        self.TOP = self.initiateClass.TOP
        self.BOTTOM = self.initiateClass.BOTTOM
        self.RIGHT = self.initiateClass.RIGHT
        self.LEFT = self.initiateClass.LEFT
        
        self.DIAMETER = self.initiateClass.OBSTACLE_AND_POWERUPS_DIAMETER
        
        self.setDotY(self.BOTTOM / 2)
        self.setDotX(self.RIGHT / 2)
        
        self.OBSTACLE_AND_POWERUPS_MOVEMENT_Y = (-self.BOTTOM / 2) + self.MIDDLE_Y  
        self.OBSTACLE_AND_POWERUPS_MOVEMENT_X = (-self.RIGHT / 2) + self.MIDDLE_X
             
    def updateBoundaries(self, screen):
             
        mousex, mousey = pygame.mouse.get_pos()     # get the mouses x and y position
     #   angle = self.getAngle(self.MIDDLE_X, self.MIDDLE_Y, mousex, mousey)
                
        angle = math.atan2(mousey - self.MIDDLE_Y, mousex - self.MIDDLE_X)
                      
        x = math.cos(angle);
        y = math.sin(angle);
        
        if self.PowerUpVariables.isSpeedBoost() == True:    #Check if speed boost
            self.PowerUpVariables.speedBoost()
        
        y = (y * self.PowerUpVariables.getDotSpeed()) * self.PowerUpVariables.SPEED_BOOST      #increases speed, multiplies here for simplicity
        x = (x * self.PowerUpVariables.getDotSpeed()) * self.PowerUpVariables.SPEED_BOOST      # Multiplying may cause issues with boundaries
                                                                                               #add speed boost if any
        
        if self.PowerUpVariables.getDotOppositeDirecton() == False:
            y = y
            x = x
        elif self.PowerUpVariables.getDotOppositeDirecton() == True:
            y = -y
            x = -x
        
        newX = self.getDotX() + x                    
        newY = self.getDotY() + y
        
    #    print self.getDotY()
    #    print self.TOP
        
        self.checkX(newX, x)
        self.checkY(newY, y)

    #    self.drawBoundaries(screen)

    #    print "RIGHT2:   ",self.RIGHT
    #    print "DOTX:     ",self.DOT_X + self.DOT_RADIUS
    #    print ""
        
    def drawBoundaries(self, screen): #adjust_obstacle_placement variable used to prevents obstacles from moving when the dot hits the boundaries
        
        boundary_top = self.TOP + self.MIDDLE_Y
        boundary_bottom = self.BOTTOM - self.MIDDLE_Y
        boundary_right = self.RIGHT - self.MIDDLE_X
        boundary_left = self.LEFT + self.MIDDLE_X
        
        if self.getDotY() < boundary_top:
            rectHeight = boundary_top - self.getDotY()
            rect = pygame.Rect(0, 0, self.WIDTH, rectHeight)
            pygame.draw.rect(screen, (0, 255, 255), rect)
            
        if self.getDotY() > boundary_bottom:
            rectHeight = (self.HEIGHT) - (self.getDotY() - boundary_bottom)
            rect = pygame.Rect(0, rectHeight, self.WIDTH, self.HEIGHT)
            pygame.draw.rect(screen, (0, 255, 255), rect)
            
        if self.getDotX() > boundary_right:
            rectWidth = self.WIDTH - (self.getDotX() - boundary_right)
            rect = pygame.Rect(rectWidth, 0, self.WIDTH, self.HEIGHT)
            pygame.draw.rect(screen, (0, 255, 255), rect)
            
        if self.getDotX() < boundary_left:
            rectWidth = boundary_left - self.getDotX()
            rect = pygame.Rect(0, 0, rectWidth, self.HEIGHT)
            pygame.draw.rect(screen, (0, 255, 255), rect)
        

    def checkX(self, newDotX, x):
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
        
        if self.PowerUpVariables.getDotSheild() == True:
            dot_radius = int(dot_radius * 1.5)

        
        if newDotX + dot_radius > self.RIGHT or newDotX - dot_radius < self.LEFT:
            if newDotX + dot_radius > self.RIGHT:
                
                adjust_obstacle_placement = self.RIGHT - (self.getDotX() + dot_radius) 
                self.updateObstaclesAndPowerUpsMovement_X(adjust_obstacle_placement)
                self.setInstantaneousMovementX(adjust_obstacle_placement)
                self.setDotX(self.getDotX() + adjust_obstacle_placement)
                
                
            elif newDotX - dot_radius < self.LEFT:
                
                adjust_obstacle_placement = self.LEFT + (self.getDotX() - dot_radius) 
                self.updateObstaclesAndPowerUpsMovement_X(-adjust_obstacle_placement)
                self.setInstantaneousMovementX(adjust_obstacle_placement)
                self.setDotX(self.getDotX() - adjust_obstacle_placement)
        else:
            self.setDotX(newDotX)
            self.updateObstaclesAndPowerUpsMovement_X(x)
            self.setInstantaneousMovementX(x)
            
            
    def checkY(self, newDotY, y):
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
                
        if self.PowerUpVariables.getDotSheild() == True:
            dot_radius = int(dot_radius * 1.5)

                
        if newDotY - dot_radius < self.TOP or newDotY + dot_radius > self.BOTTOM:
            if newDotY - dot_radius < self.TOP:
                
                adjust_obstacle_placement = self.TOP + (self.getDotY() - dot_radius) 
                self.updateObstaclesAndPowerUpsMovement_Y(-adjust_obstacle_placement)
                self.setInstantaneousMovementY(adjust_obstacle_placement)
                self.setDotY(self.getDotY() - adjust_obstacle_placement)
                
            elif newDotY + dot_radius > self.BOTTOM:
                
                adjust_obstacle_placement = self.BOTTOM - (self.getDotY() + dot_radius) 
                self.updateObstaclesAndPowerUpsMovement_Y(adjust_obstacle_placement)
                self.setInstantaneousMovementY(adjust_obstacle_placement)
                self.setDotY(self.getDotY() + adjust_obstacle_placement)
        else:
            self.setDotY(newDotY)
            self.updateObstaclesAndPowerUpsMovement_Y(y)
            self.setInstantaneousMovementY(y)

    
    def setDotX(self, newX):
        self.DOT_X = newX
   #     print "DOT_X:          ",self.DOT_X
        
    def setDotY(self, newY):
        self.DOT_Y = newY
    #    print "DOT_Y:          ",self.DOT_Y
        
    def getDotX(self):
        return self.DOT_X
        
    def getDotY(self):
        return self.DOT_Y
    
    
    def updateObstaclesAndPowerUpsMovement_X(self, addX):
        self.OBSTACLE_AND_POWERUPS_MOVEMENT_X = self.OBSTACLE_AND_POWERUPS_MOVEMENT_X - addX  # subtracting to make them move in the right direction
        
    def updateObstaclesAndPowerUpsMovement_Y(self, addY):
        self.OBSTACLE_AND_POWERUPS_MOVEMENT_Y = self.OBSTACLE_AND_POWERUPS_MOVEMENT_Y - addY  # adding to make them move in the right direction
        
    def getObstaclesAndPowerUpsMovement_X(self):
        return self.OBSTACLE_AND_POWERUPS_MOVEMENT_X
        
    def getObstaclesAndPowerUpsMovement_Y(self):
        return self.OBSTACLE_AND_POWERUPS_MOVEMENT_Y
    
    def setInstantaneousMovementX(self, x):
        self.INSTANTANEOUS_MOVEMENT_X = x
        
    def setInstantaneousMovementY(self, y):
        self.INSTANTANEOUS_MOVEMENT_Y = y

    def getInstantaneousMovementX(self):
        return self.INSTANTANEOUS_MOVEMENT_X

    def getInstantaneousMovementY(self):
        return self.INSTANTANEOUS_MOVEMENT_Y


        
        
