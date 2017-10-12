'''
Created on Dec 23, 2015

@author: ryan3971
'''

import pygame
import random
#import sys
import math

#from Boundaries import Boundaries
#from Dot import Dot
from InitiateClass import InitiateClass
#from ManageObjects import ManageObjects
from PowerUpVariables import PowerUpVariables
#from shootLaser import shootLaser
from PowerUps_Lives_EndGame import Lives
from PowerUps_Lives_EndGame import PowerUpsInUse
from ServerVariables import ServerVariables
from ClientVariables import ClientVariables

class ObstaclesAndPowerUps_2(ClientVariables):
    
    LEFT = 0
    RIGHT = 0
    TOP = 0
    BOTTOM = 0
    
    WIDTH = 0
    HEIGHT = 0
    
    RADIUS = 0
    DIAMETER = 0
    
    MIDDLE_X = 0
    MIDDLE_Y = 0
    
    DOT_RADIUS = 0

    OBSTACLE_LIST_X = []
    OBSTACLE_LIST_Y = []
    
    POWERUPS_LIST_X = []
    POWERUPS_LIST_Y = []
    
    PowerUpVariables = None
    
    Lives_Images = None
    PowerUp_Images = None

    def __init__(self, Lives, PowerUpVariables, client):
                                
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        self.MIDDLE_Y = self.initiateClass.MIDDLE_Y
        self.MIDDLE_X = self.initiateClass.MIDDLE_X
        self.DOT_RADIUS = self.initiateClass.DOT_RADIUS
        
        self.PowerUpVariables = PowerUpVariables
        
        self.RADIUS = self.initiateClass.OBSTACLE_AND_POWERUPS_RADIUS
        self.DIAMETER = self.initiateClass.OBSTACLE_AND_POWERUPS_DIAMETER
        
        self.TOP = self.initiateClass.TOP
        self.BOTTOM = self.initiateClass.BOTTOM
        self.RIGHT = self.initiateClass.RIGHT
        self.LEFT = self.initiateClass.LEFT
        
        self.Lives_Images = Lives
        self.PowerUp_Images = PowerUpVariables.PowerUp_Images

        self.CLIENT = client
        self.SV = ServerVariables()
        self.CV = ClientVariables
    
    def updateAndDrawObstacles(self, screen, obstacles_movement_y, obstacles_movement_x):
        
        list_size = len(self.CV.OBSTACLE_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size):
                        
            obstacle_y = self.CV.OBSTACLE_LIST_Y[list_num]
            obstacle_x = self.CV.OBSTACLE_LIST_X[list_num]
            
            obstacle_y = obstacle_y + obstacles_movement_y
            obstacle_x = obstacle_x + obstacles_movement_x

            pygame.draw.circle(screen, [0,255,0], [int(obstacle_x), int(obstacle_y)], self.RADIUS, 0)

    
    def updateAndDrawPowerUps(self, screen, powerups_movement_y, powerups_movement_x):
        
        list_size = len(self.CV.POWERUPS_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size):
                        
            powerups_y = self.CV.POWERUPS_LIST_Y[list_num]
            powerups_x = self.CV.POWERUPS_LIST_X[list_num]
            
            powerups_y = powerups_y + powerups_movement_y
            powerups_x = powerups_x + powerups_movement_x

            pygame.draw.circle(screen, [0,255,255], [int(powerups_x), int(powerups_y)], self.RADIUS, 0)

    def checkPowerUpCollisions(self, powerups_movement_y, powerups_movement_x, dot_x, dot_y):
        
        dot_x = self.MIDDLE_X
        dot_y = self.MIDDLE_Y
        
        powerup_x_list = self.CV.POWERUPS_LIST_X #in case one is removed while in for loop. prevent index out of range error
        powerup_y_list = self.CV.POWERUPS_LIST_Y #cleans code up a little also
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
        
        if self.PowerUpVariables.getDotSheild() == True:
            dot_radius = int(dot_radius * 1.5)
        
        list_size = len(powerup_y_list)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size - 1): 
                        
            powerups_y = powerup_y_list[list_num]
            powerups_x = powerup_x_list[list_num]
            
            powerups_y = powerups_y + powerups_movement_y
            powerups_x = powerups_x + powerups_movement_x
            
            distance = math.sqrt(math.pow((powerups_x - dot_x), 2) + math.pow((powerups_y - dot_y), 2));

            if distance <= self.RADIUS + dot_radius:                 
                
                self.CV.POWERUPS_LIST_Y.pop(list_num)
                self.CV.POWERUPS_LIST_X.pop(list_num)
                
                self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.NEW_POWERUP, True)
                
                self.activatePowerUp()


    def checkObstacleCollisions(self, obstacles_movement_y, obstacles_movement_x, dot_x, dot_y):
        
        dot_x = self.MIDDLE_X
        dot_y = self.MIDDLE_Y
        
        obstacles_x_list = self.CV.OBSTACLE_LIST_X #in case one is removed while in for loop. prevent index out of range error
        obstacles_y_list = self.CV.OBSTACLE_LIST_Y
        
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
        
        if self.PowerUpVariables.getDotSheild() == True:
            dot_radius = int(dot_radius * 1.5)
        
        list_size = len(obstacles_y_list)  #both the x and y list are the same, so doesn't matter which is used

        for list_num in range(0, list_size - 1): # prevents crashing for that first obstacle. not sure why.
                        
            obstacles_y = obstacles_y_list[list_num]
            obstacles_x = obstacles_x_list[list_num]
            
            obstacles_y = obstacles_y + obstacles_movement_y
            obstacles_x = obstacles_x + obstacles_movement_x
            
            distance = math.sqrt(math.pow((obstacles_x - dot_x), 2) + math.pow((obstacles_y - dot_y), 2));

            if distance <= self.RADIUS + dot_radius:                 
                                
                self.CV.OBSTACLE_LIST_Y.pop(list_num)
                self.CV.OBSTACLE_LIST_X.pop(list_num)
                                
                if self.PowerUpVariables.getDotSheild() == True:
                    self.PowerUpVariables.setDotSheild(False)
                else:
                    self.Lives_Images.LossLife()
                    
                
                self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.NEW_OBSTACLE, True)

    
        
    def activatePowerUp(self):
        
        power_up_num = random.randrange(0, 12)

        if power_up_num == 0:
            if self.PowerUpVariables.getDotSizeSmall() == True:
                self.PowerUpVariables.setDotSizeSmall(False)
            elif self.PowerUpVariables.getDotSizeLarge() == False:
                self.PowerUpVariables.setDotSizeLarge(True)
            else:
                self.activatePowerUp()                
                
        elif power_up_num == 1:
            if self.PowerUpVariables.getDotSizeLarge() == True:
                self.PowerUpVariables.setDotSizeLarge(False)
            elif self.PowerUpVariables.getDotSizeSmall() == False:
                self.PowerUpVariables.setDotSizeSmall(True)
            else:
                self.activatePowerUp()
                
        elif power_up_num == 2:
            if self.PowerUpVariables.getDotOppositeDirecton() == False:
                self.PowerUpVariables.setDotOppositeDirection(True)
            else:
                self.PowerUpVariables.setDotOppositeDirection(False)
                
        elif power_up_num == 3:
            
            if self.PowerUpVariables.getDotSpeedSlow() == True:
                self.PowerUpVariables.setDotSpeedSlow(False)
            elif self.PowerUpVariables.getDotSpeedFast() == False:
                self.PowerUpVariables.setDotSpeedFast(True)
            else:
                self.activatePowerUp()   
            
        elif power_up_num == 4:
            
            if self.PowerUpVariables.getDotSpeedFast() == True:
                self.PowerUpVariables.setDotSpeedFast(False)
            elif self.PowerUpVariables.getDotSpeedSlow() == False:
                self.PowerUpVariables.setDotSpeedSlow(True)
            else:
                self.activatePowerUp() 
                  
        elif power_up_num == 5:
            
            if self.PowerUpVariables.getDotInvisible() == True:
                self.PowerUpVariables.setDotInvisible(False)
            else:
                self.PowerUpVariables.setDotInvisible(True)
                
        elif power_up_num == 6:
            
            if len(self.PowerUpVariables.getLaserList()) < 9:
                self.PowerUpVariables.setLaserList(True)
            else:
                self.activatePowerUp() 
            
        elif power_up_num == 7:

            if len(self.PowerUpVariables.getBallList()) < 9:
                self.PowerUpVariables.setBallList(True)
            else:
                self.activatePowerUp()
                            
        elif power_up_num == 8:
            
            if self.PowerUpVariables.DOT_SHEILD == False:
                self.PowerUpVariables.setDotSheild(True)
            else:
                self.activatePowerUp()  
                
        elif power_up_num == 9:
            
                self.PowerUpVariables.setMultiLaser(True)
                
        elif power_up_num == 10:
            
            if self.PowerUpVariables.getPowerWave() == False:
                self.PowerUpVariables.setPowerWave(True)
            else:
                self.activatePowerUp()  
                
        elif power_up_num == 11:

            if len(self.PowerUpVariables.getTargetBallList()) < 4:
                self.PowerUpVariables.setTargetBallList(True)
            else:
                self.activatePowerUp()

        
            