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



class ObstaclesAndPowerUps():
    
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

    def __init__(self, Lives, PowerUpVariables):

        '''
        Initiates variables
        
        @param PowerUpVariables: passes the PowerUpVariables object
        @param Lives: the number of lives the player has.
        '''
                                
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
        
    def createObstaclesAndPowerUps(self): # try switching to and bottom
        
        '''
        Creates the power ups and obstacles
        '''
        
        for y in range(int(self.TOP), int(self.BOTTOM), self.DIAMETER): #makes it go from positive to negative
            for x in range(int(self.LEFT), int(self.RIGHT), self.DIAMETER):#makes it go from positive to negative                
                num = random.randrange(0, 50)
                
                if (num == 0):
                    obstacle_y = y + self.RADIUS
                    obstacle_x = x + self.RADIUS
                    
                    self.OBSTACLE_LIST_Y.append(obstacle_y)
                    self.OBSTACLE_LIST_X.append(obstacle_x)
                    
                elif num == 1:
                    
                    powerup_y = y + self.RADIUS
                    powerup_x = x + self.RADIUS
                    
                    self.POWERUPS_LIST_Y.append(powerup_y)
                    self.POWERUPS_LIST_X.append(powerup_x)
                    
                    
    def updateAndDrawObstacles(self, screen, obstacles_movement_y, obstacles_movement_x):
        
        '''
        Updates the location and draws the obstacles
        
        @param screen: The display variable. Used to draw the obstacles
        
        @param obstacles_movement_y: the instantaneous movement of the main dot on the y-axis.
        Used to adjust where to obstacles are drawn.
        
        @param obstacles_movement_x: the instantaneous movement of the main dot on the x-axis.
        Used to adjust where to obstacles are drawn.
        '''
        
        list_size = len(self.OBSTACLE_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size):
                        
            obstacle_y = self.OBSTACLE_LIST_Y[list_num]
            obstacle_x = self.OBSTACLE_LIST_X[list_num]
            
            obstacle_y = obstacle_y + obstacles_movement_y
            obstacle_x = obstacle_x + obstacles_movement_x

            pygame.draw.circle(screen, [0,255,0], [int(obstacle_x), int(obstacle_y)], self.RADIUS, 0)

    
    def updateAndDrawPowerUps(self, screen, powerups_movement_y, powerups_movement_x):
        
        '''
        Updates the location and draws the power ups
        
        @param screen: The display variable. Used to draw the power ups
        
        @param powerups_movement_y: the instantaneous movement of the main dot on the y-axis.
        Used to adjust where to power ups are drawn.
        
        @param powerups_movement_x: the instantaneous movement of the main dot on the x-axis.
        Used to adjust where to power ups are drawn.
        '''
        
        list_size = len(self.POWERUPS_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size):
                        
            powerups_y = self.POWERUPS_LIST_Y[list_num]
            powerups_x = self.POWERUPS_LIST_X[list_num]
            
            powerups_y = powerups_y + powerups_movement_y
            powerups_x = powerups_x + powerups_movement_x

            pygame.draw.circle(screen, [0,255,255], [int(powerups_x), int(powerups_y)], self.RADIUS, 0)

    def checkPowerUpCollisions(self, powerups_movement_y, powerups_movement_x, dot_x, dot_y):
        
        '''
        Checks whether the main dot has touched a power up
        
        @param powerups_movement_y: the instantaneous movement of the main dot on the y-axis.
        Used to adjust where to power ups are drawn.
        
        @param powerups_movement_x: the instantaneous movement of the main dot on the x-axis.
        Used to adjust where to power ups are drawn.
        
        @param dot_x: the main dots x-coordinates
        
        @param dot_x: the main dots y-coordinates

        '''
        
        dot_x = self.MIDDLE_X
        dot_y = self.MIDDLE_Y
        
        dot_radius = int(self.DOT_RADIUS * self.PowerUpVariables.getDotSize())
        
        if self.PowerUpVariables.getDotSheild() == True:
            dot_radius = int(dot_radius * 1.5)
        
        list_size = len(self.POWERUPS_LIST_Y)  #both the x and y list are the same, so doesn't matter which is used
        
        for list_num in range(0, list_size): 
                        
            powerups_y = self.POWERUPS_LIST_Y[list_num]
            powerups_x = self.POWERUPS_LIST_X[list_num]
            
            powerups_y = powerups_y + powerups_movement_y
            powerups_x = powerups_x + powerups_movement_x
            
            distance = math.sqrt(math.pow((powerups_x - dot_x), 2) + math.pow((powerups_y - dot_y), 2));

            if distance <= self.RADIUS + dot_radius:                 
                
                self.POWERUPS_LIST_Y.pop(list_num)
                self.POWERUPS_LIST_X.pop(list_num)
                
                self.createNewPowerUps(dot_x, dot_y)
                self.activatePowerUp()


    def checkObstacleCollisions(self, obstacles_movement_y, obstacles_movement_x, dot_x, dot_y):
        
        '''
        Checks whether the main dot has touched an obstacle
        
        @param obstacles_movement_y: the instantaneous movement of the main dot on the y-axis.
        Used to adjust where to obstacles are drawn.
        
        @param obstacles_movement_x: the instantaneous movement of the main dot on the x-axis.
        Used to adjust where to obstacles are drawn.
        
        @param dot_x: the main dots x-coordinates
        
        @param dot_x: the main dots y-coordinates

        '''
        
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
                                
                if self.PowerUpVariables.getDotSheild() == True:
                    self.PowerUpVariables.setDotSheild(False)
                else:
                    self.Lives_Images.LossLife()
                    
                self.createNewObstacle(dot_x, dot_y)
                
                
    
    def createNewPowerUps(self, dot_x, dot_y):        #small chance that powerups will appear on obstacles
        
        '''
        Creates a new power up
        
        @param dot_x: the main dots x-coordinates
        
        @param dot_x: the main dots y-coordinates
        '''
        
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
                    self.createNewPowerUps(dot_x, dot_y)                                                     #see if works
                
            list_size = len(self.OBSTACLE_LIST_Y)
        
            for list_num in range(0, list_size):
                obstacle_y = self.OBSTACLE_LIST_Y[list_num]
                obstacle_x = self.OBSTACLE_LIST_X[list_num]
                
                if obstacle_x == new_powerup_x and obstacle_y == new_powerup_y:
                    self.createNewPowerUps(dot_x, dot_y) 
                    
            
            if dot_x == new_powerup_x and dot_y == new_powerup_y:
                self.createNewObstacle(dot_x, dot_y) 
        
        self.POWERUPS_LIST_Y.append(new_powerup_y)
        self.POWERUPS_LIST_X.append(new_powerup_x)
        
        
    def createNewObstacle(self, dot_x, dot_y):        #small chance that powerups will appear on obstacles
        
        '''
        Creates a new obstacle
        
        @param dot_x: the main dots x-coordinates
        
        @param dot_x: the main dots y-coordinates
        '''
        
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
                    self.createNewObstacle(dot_x, dot_y)                                                     #see if works
                
            list_size = len(self.OBSTACLE_LIST_Y)
        
            for list_num in range(0, list_size):
                obstacle_y = self.OBSTACLE_LIST_Y[list_num]
                obstacle_x = self.OBSTACLE_LIST_X[list_num]
                
                if obstacle_x == new_obstacle_x and obstacle_y == new_obstacle_y:
                    self.createNewObstacle(dot_x, dot_y) 
                    
            if dot_x == new_obstacle_x and dot_y == new_obstacle_y:
                self.createNewObstacle(dot_x, dot_y) 
                    
        
        self.OBSTACLE_LIST_Y.append(new_obstacle_y)
        self.OBSTACLE_LIST_X.append(new_obstacle_x)
        
        
        
        
    def activatePowerUp(self):
        
        '''
        Activates a random power up. Total of 12 different power ups
        '''
        
        power_up_num = random.randrange(0, 11)

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

        
            