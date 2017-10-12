'''
Created on Dec 1, 2015

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

class ObstaclesAndPowerUps(ClientVariables):
    
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

    def createObstaclesAndPowerUps(self): # try switching to and bottom
                
        i = 1
        
        for y in range(int(self.TOP), int(self.BOTTOM), self.DIAMETER): 
            for x in range(int(self.LEFT), int(self.RIGHT), self.DIAMETER):            
                num = random.randrange(0, 50)
                
                if (num == 0):
                    obstacle_y = y + self.RADIUS
                    obstacle_x = x + self.RADIUS
                    
                    self.OBSTACLE_LIST_Y.append(obstacle_y)
                    self.OBSTACLE_LIST_X.append(obstacle_x)
                    
                    print i
                    i += 1
                    
                    self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.OBSTACLES, [obstacle_x, obstacle_y])
                    
                elif num == 1:
                    
                    powerup_y = y + self.RADIUS
                    powerup_x = x + self.RADIUS
                    
                    self.POWERUPS_LIST_Y.append(powerup_y)
                    self.POWERUPS_LIST_X.append(powerup_x)
                    
                #    print i
                #    i += 1
                    
                #    self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.POWERUPS, [powerup_x, powerup_y])

        return True
                    
    def updateAndDrawObstacles(self, screen, obstacles_movement_y, obstacles_movement_x):
        
        list_size = len(self.OBSTACLE_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size):
                        
            obstacle_y = self.OBSTACLE_LIST_Y[list_num]
            obstacle_x = self.OBSTACLE_LIST_X[list_num]
            
            obstacle_y = obstacle_y + obstacles_movement_y
            obstacle_x = obstacle_x + obstacles_movement_x

            pygame.draw.circle(screen, [0,255,0], [int(obstacle_x), int(obstacle_y)], self.RADIUS, 0)

    
    def updateAndDrawPowerUps(self, screen, powerups_movement_y, powerups_movement_x):
        
        list_size = len(self.POWERUPS_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size):
                        
            powerups_y = self.POWERUPS_LIST_Y[list_num]
            powerups_x = self.POWERUPS_LIST_X[list_num]
            
            powerups_y = powerups_y + powerups_movement_y
            powerups_x = powerups_x + powerups_movement_x

            pygame.draw.circle(screen, [0,255,255], [int(powerups_x), int(powerups_y)], self.RADIUS, 0)

    def checkPowerUpCollisions(self, powerups_movement_y, powerups_movement_x, dot_x, dot_y):
        
        dot_x = self.MIDDLE_X
        dot_y = self.MIDDLE_Y
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
        
        if self.PowerUpVariables.getDotSheild() == True:
            dot_radius = int(dot_radius * 1.5)
        
        list_size = len(self.POWERUPS_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size - 1): 
                        
            powerups_y = self.POWERUPS_LIST_Y[list_num]
            powerups_x = self.POWERUPS_LIST_X[list_num]
            
            powerups_y = powerups_y + powerups_movement_y
            powerups_x = powerups_x + powerups_movement_x
            
            distance = math.sqrt(math.pow((powerups_x - dot_x), 2) + math.pow((powerups_y - dot_y), 2));

            if distance <= self.RADIUS + dot_radius:                 
                
                self.POWERUPS_LIST_Y.pop(list_num)
                self.POWERUPS_LIST_X.pop(list_num)
                
                self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.REMOVE_POWERUP, list_num)
                
                self.createNewPowerUps(dot_x, dot_y, self.CV.DOT_2_X, self.CV.DOT_2_Y)
                self.activatePowerUp()
                
            if self.CV.NEW_POWERUP == True:
                self.CV.NEW_POWERUP = False
                self.createNewPowerUps(dot_x, dot_y, self.CV.DOT_2_X, self.CV.DOT_2_Y)


    def checkObstacleCollisions(self, obstacles_movement_y, obstacles_movement_x, dot_x, dot_y):
        
        dot_x = self.MIDDLE_X
        dot_y = self.MIDDLE_Y
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
        
        if self.PowerUpVariables.getDotSheild() == True:
            dot_radius = int(dot_radius * 1.5)
        
        list_size = len(self.OBSTACLE_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used

        for list_num in range(0, list_size - 1): # prevents crashing for that first obstacle. not sure why.
                        
            obstacles_y = self.OBSTACLE_LIST_Y[list_num]
            obstacles_x = self.OBSTACLE_LIST_X[list_num]
            
            obstacles_y = obstacles_y + obstacles_movement_y
            obstacles_x = obstacles_x + obstacles_movement_x
            
            distance = math.sqrt(math.pow((obstacles_x - dot_x), 2) + math.pow((obstacles_y - dot_y), 2));

            if distance <= self.RADIUS + dot_radius:                 
                                
                self.OBSTACLE_LIST_Y.pop(list_num)
                self.OBSTACLE_LIST_X.pop(list_num)
                
                self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.REMOVE_OBSTACLE, list_num)
                                
                if self.PowerUpVariables.getDotSheild() == True:
                    self.PowerUpVariables.setDotSheild(False)
                else:
                    self.Lives_Images.LossLife()
                    
                self.createNewObstacle(dot_x, dot_y, self.CV.DOT_2_X, self.CV.DOT_2_Y)
                
            if self.CV.NEW_OBSTACLE == True:
                self.CV.NEW_OBSTACLE = False
                self.createNewObstacle(dot_x, dot_y, self.CV.DOT_2_X, self.CV.DOT_2_Y)
                
    
    def createNewPowerUps(self, dot_x, dot_y, dot_x_2, dot_y_2):        #small chance that powerups will appear on obstacles
        #Not working cause of bellow
        area_x = self.RIGHT / self.DIAMETER
        area_y = self.BOTTOM / self.DIAMETER
        
        available_location = False
        
        while available_location == False:
            
            available_location = True
            
            new_powerup_x = random.randrange(0, int(area_x))
            new_powerup_y = random.randrange(0, int(area_y))
            
            new_powerup_x = new_powerup_x * self.DIAMETER
            new_powerup_y = new_powerup_y * self.DIAMETER
                        
            new_powerup_x = new_powerup_x + self.RADIUS
            new_powerup_y = new_powerup_y + self.RADIUS
            
            list_size = len(self.POWERUPS_LIST_Y)
            for list_num in range(0, list_size):
                
                powerups_y = self.POWERUPS_LIST_Y[list_num]
                powerups_x = self.POWERUPS_LIST_X[list_num]
                
                if powerups_x == new_powerup_x and powerups_y == new_powerup_y:
                    self.createNewPowerUps(dot_x, dot_y, dot_x_2, dot_y_2)                                                     #see if works
                
            list_size = len(self.OBSTACLE_LIST_Y)
        
            for list_num in range(0, list_size):
                obstacle_y = self.OBSTACLE_LIST_Y[list_num]
                obstacle_x = self.OBSTACLE_LIST_X[list_num]
                
                if obstacle_x == new_powerup_x and obstacle_y == new_powerup_y:
                    self.createNewPowerUps(dot_x, dot_y, dot_x_2, dot_y_2) 
                    
            
            if dot_x == new_powerup_x and dot_y == new_powerup_y:
                self.createNewObstacle(dot_x, dot_y, dot_x_2, dot_y_2)
                
            if dot_x_2 == new_powerup_x and dot_y_2 == new_powerup_y:
                self.createNewObstacle(dot_x, dot_y, dot_x_2, dot_y_2) 
        
        self.POWERUPS_LIST_Y.append(new_powerup_y)
        self.POWERUPS_LIST_X.append(new_powerup_x)
        
        self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.POWERUPS, [new_powerup_x, new_powerup_y])

        
        
    def createNewObstacle(self, dot_x, dot_y, dot_x_2, dot_y_2):        #small chance that powerups will appear on obstacles
        
        area_x = self.RIGHT / self.DIAMETER
        area_y = self.BOTTOM / self.DIAMETER
        
        available_location = False
        
        while available_location == False:
            
            available_location = True
            
            new_obstacle_x = random.randrange(0, int(area_x))
            new_obstacle_y = random.randrange(0, int(area_y))
            
            new_obstacle_x = new_obstacle_x * self.DIAMETER
            new_obstacle_y = new_obstacle_y * self.DIAMETER
                        
            new_obstacle_x = new_obstacle_x + self.RADIUS
            new_obstacle_y = new_obstacle_y + self.RADIUS
            
            list_size = len(self.POWERUPS_LIST_Y)
            for list_num in range(0, list_size):
                
                powerups_y = self.POWERUPS_LIST_Y[list_num]
                powerups_x = self.POWERUPS_LIST_X[list_num]
                
                if powerups_x == new_obstacle_x and powerups_y == new_obstacle_y:
                    self.createNewObstacle(dot_x, dot_y, dot_x_2, dot_y_2)                                                     #see if works
                
            list_size = len(self.OBSTACLE_LIST_Y)
        
            for list_num in range(0, list_size):
                obstacle_y = self.OBSTACLE_LIST_Y[list_num]
                obstacle_x = self.OBSTACLE_LIST_X[list_num]
                
                if obstacle_x == new_obstacle_x and obstacle_y == new_obstacle_y:
                    self.createNewObstacle(dot_x, dot_y, dot_x_2, dot_y_2) 
                    
            if dot_x == new_obstacle_x and dot_y == new_obstacle_y:
                self.createNewObstacle(dot_x, dot_y, dot_x_2, dot_y_2) 
                
            if dot_x_2 == new_obstacle_x and dot_y_2 == new_obstacle_y:
                self.createNewObstacle(dot_x, dot_y, dot_x_2, dot_y_2) 
                    
        
        self.OBSTACLE_LIST_Y.append(new_obstacle_y)
        self.OBSTACLE_LIST_X.append(new_obstacle_x)
        
        
        self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.OBSTACLES, [new_obstacle_x, new_obstacle_y])

        
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

        
            