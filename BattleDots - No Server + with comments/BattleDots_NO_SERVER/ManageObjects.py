'''
Created on Dec 1, 2015

@author: ryan3971
'''

#import pygame
#import random
#import sys
#import math

#from Boundaries import Boundaries
#from Dot import Dot
from InitiateClass import InitiateClass
#from ObstaclesAndPowerUps import ObstaclesAndPowerUps
from PowerUpVariables import PowerUpVariables
from shootLaser import shootLaser
from BouncingBall import BouncingBall
from MultiLaser import MultiLaser
from PowerWave import PowerWave
from TargetBall import TargetBall


class ManageObjects():
    
    PowerUpVariables = None
    
    LASER_LIST = []
    DESTROY_LASER = False
    DESTROY_LASER_LIST_NUM = 0
    
    BALL_LIST = []
    
    MULTI_LASER_LIST = []
    DESTROY_MULTI_LASER = False
    DESTROY_MULTI_LASER_LIST_NUM = 0
    
    TARGET_BALL_LIST = []

    
    def __init__(self, PowerUpVariables):
        
        '''
        Initiates variable
        
        @param PowerUpVariables: passes the PowerUpVariables object
        '''
        
        self.PowerUpVariables = PowerUpVariables
    
    def manageLaser(self, dot_location_x, dot_location_y, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object, screen):
        
        '''
        Manages the Laser objects
        
        @param dot_location_x: the x-coordinate of the main dot
        @param dot_location_y: the y-coordinate of the main dot
        @param instantaneous_movement_x: the instantaneous movement of the dot in the x-axis
        @param instantaneous_movement_y: the instantaneous movement of the dot in the y-axis
        @param ManageObjects_Object: ManageObjects object, used to call the MangeObjects class
        @param screen: The display variable. Used to draw the Laser
        
        
        '''
        
        laser_list = self.PowerUpVariables.getLaserList()

        for num in range(0, len(laser_list)):      
            
            new_laser = laser_list[num]
            
            if new_laser == True:
                newLaser = shootLaser()
                newLaser.createLaser(dot_location_x, dot_location_y)
                self.LASER_LIST.append(newLaser)
                
                self.PowerUpVariables.setLaserList(False, num)
                    
                    
        laser_list_size = len(self.LASER_LIST)
                
        for list_num in range(0, laser_list_size):
            self.LASER_LIST[list_num].updateAndDrawLaser(screen, list_num, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object)

        if self.DESTROY_LASER == True:      # removes laser from list after running through for loop to prevent index out of range error
            self.DESTROY_LASER = False
            self.LASER_LIST.pop(self.DESTROY_LASER_LIST_NUM)
            self.PowerUpVariables.destroyLaser()
            
    def removeLaserFromList(self, list_num):
        
        '''
        Removes the Laser objects, destroying the laser
        
        @param list_num: the location of the laser to be destroyed in the Laser list
        '''
        
        self.DESTROY_LASER = True
        self.DESTROY_LASER_LIST_NUM = list_num
        
        
    def manageBall(self, dot_location_x, dot_location_y, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object, screen):
        
        '''
        Manages the Bouncing Ball objects
        
        @param dot_location_x: the x-coordinate of the main dot
        @param dot_location_y: the y-coordinate of the main dot
        @param instantaneous_movement_x: the instantaneous movement of the dot in the x-axis
        @param instantaneous_movement_y: the instantaneous movement of the dot in the y-axis
        @param ManageObjects_Object: ManageObjects object, used to call the MangeObjects class
        @param screen: The display variable. Used to draw the Bouncing Ball
        '''
        
        ball_list = self.PowerUpVariables.getBallList()

        for num in range(0, len(ball_list)):      
            
            new_ball = ball_list[num]
            
            if new_ball == True:
                newBall = BouncingBall()
                newBall.createBall(dot_location_x, dot_location_y)
                self.BALL_LIST.append(newBall)

                self.PowerUpVariables.setBallList(False, num)
                    
        
        ball_list_size = len(self.BALL_LIST)
                    
        for list_num in range(0, ball_list_size):
            self.BALL_LIST[list_num].updateAndDrawBall(screen, instantaneous_movement_x, instantaneous_movement_y)
    
    def manageMultiLaser(self, dot_location_x, dot_location_y, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object, screen):
        
        '''
        Manages the Multi-Laser objects
        
        @param dot_location_x: the x-coordinate of the main dot
        @param dot_location_y: the y-coordinate of the main dot
        @param instantaneous_movement_x: the instantaneous movement of the dot in the x-axis
        @param instantaneous_movement_y: the instantaneous movement of the dot in the y-axis
        @param ManageObjects_Object: ManageObjects object, used to call the MangeObjects class
        @param screen: The display variable. Used to draw the Multi-Laser
        '''
        
        if self.PowerUpVariables.getMultiLaser() == True:
            self.PowerUpVariables.setMultiLaser(False)
            self.PowerUpVariables.showMultiLaserImage(True)
                
            for num in range(0, 30):
                newMultiLaser = MultiLaser()
                newMultiLaser.createMultiLaser(dot_location_x, dot_location_y)
                self.MULTI_LASER_LIST.append(newMultiLaser)
                                
                    
        laser_list_size = len(self.MULTI_LASER_LIST)
                
        for list_num in range(0, laser_list_size):
            self.MULTI_LASER_LIST[list_num].updateAndDrawMultiLaser(screen, list_num, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object)

        if self.DESTROY_MULTI_LASER == True:      # removes laser from list after running through for loop to prevent index out of range error
            self.DESTROY_MULTI_LASER = False
            self.MULTI_LASER_LIST.pop(self.DESTROY_MULTI_LASER_LIST_NUM)
            
            if len(self.MULTI_LASER_LIST) == 0:
                self.PowerUpVariables.showMultiLaserImage(False)

            
    def removeMultiLaserFromList(self, list_num):
        
        '''
        Removes the Multi-Laser objects, destroying the Multi-Lasers
        
        @param list_num: the location of the Multi-Laser to be destroyed in the Multi-Laser list
        '''
        
        self.DESTROY_MULTI_LASER = True
        self.DESTROY_MULTI_LASER_LIST_NUM = list_num        
        
        
    def managePowerWave(self, dot_location_x, dot_location_y, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object, screen):
        
        '''
        Manages the PowerWave objects
        
        @param dot_location_x: the x-coordinate of the main dot
        @param dot_location_y: the y-coordinate of the main dot
        @param instantaneous_movement_x: the instantaneous movement of the dot in the x-axis
        @param instantaneous_movement_y: the instantaneous movement of the dot in the y-axis
        @param ManageObjects_Object: ManageObjects object, used to call the MangeObjects class
        @param screen: The display variable. Used to draw the PowerWave
        '''
        
        if self.PowerUpVariables.getNewPowerWave() == True:
            self.PowerUpVariables.setNewPowerWave(False)
            self.PowerWave = PowerWave(dot_location_x, dot_location_y, screen)
            
        if self.PowerUpVariables.getPowerWave() == True:
            wave = self.PowerWave.drawWave(instantaneous_movement_x, instantaneous_movement_y)
        
            if wave == True:
                self.PowerUpVariables.setPowerWave(False)
            
        
    def manageTargetBall(self, dot_location_x, dot_location_y, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object, screen):
        
        '''
        Manages the TargetBall objects
        
        @param dot_location_x: the x-coordinate of the main dot
        @param dot_location_y: the y-coordinate of the main dot
        @param instantaneous_movement_x: the instantaneous movement of the dot in the x-axis
        @param instantaneous_movement_y: the instantaneous movement of the dot in the y-axis
        @param ManageObjects_Object: ManageObjects object, used to call the MangeObjects class
        @param screen: The display variable. Used to draw the TargetBall
        '''
        
        target_ball_list = self.PowerUpVariables.getTargetBallList()

        for num in range(0, len(target_ball_list)):      
            
            new_target_ball = target_ball_list[num]
            
            if new_target_ball == True:
                newTargetBall = TargetBall()
                newTargetBall.createTargetBall(dot_location_x, dot_location_y)
                self.TARGET_BALL_LIST.append(newTargetBall)

                self.PowerUpVariables.setTargetBallList(False, num)
                    
        
        target_ball_list_size = len(self.TARGET_BALL_LIST)
                    
        for list_num in range(0, target_ball_list_size):
            self.TARGET_BALL_LIST[list_num].updateAndDrawTargetBall(screen, list_num, dot_location_x, dot_location_y, instantaneous_movement_x, instantaneous_movement_y, ManageObjects_Object)
