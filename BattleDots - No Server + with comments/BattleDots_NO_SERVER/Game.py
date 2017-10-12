'''
Created on Dec 18, 2015

@author: ryan3971
'''


import pygame

from Boundaries import Boundaries
from Dot import Dot
#from InitiateClass import InitiateClass
from ManageObjects import ManageObjects
from ObstaclesAndPowerUps import ObstaclesAndPowerUps
from MainMenu import MainMenu
from PowerUps_Lives_EndGame import Lives

import PygButton
from PowerUpVariables import PowerUpVariables
from PowerUps_Lives_EndGame import PowerUpsInUse



class Game():
    
    def __init__(self, screen, backgound):
        
        '''
        Initiates variables
        '''
        
        self.SCREEN = screen
        self.BACKGROUND = backgound
        
        self.PowerUp_Images = 0
        self.PowerUpVariables = 0
        
        self.dot = 0
        self.boundaries = 0
        self.manageObjects_Laser = 0
        self.manageObjects_Ball = 0
        self.manageObjects_Multi_Laser = 0
        self.manageObjects_Power_Wave = 0
        self.manageObjects_Target_Ball = 0
        self.lives = 0
        self.obstaclesAndPowerUps = 0
            
    def game(self):
        
        '''
        Where all the game variables are initialised and the game is run
        '''                 
     
        keepGoing = True
    
        clock = pygame.time.Clock()
        
        self.PowerUp_Images = PowerUpsInUse(self.SCREEN)
        self.PowerUpVariables = PowerUpVariables(self.PowerUp_Images)
        
        self.dot = Dot(self.PowerUpVariables)
        self.boundaries = Boundaries(self.PowerUpVariables)
        self.manageObjects_Laser = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Ball = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Multi_Laser = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Power_Wave = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Target_Ball = ManageObjects(self.PowerUpVariables)
        self.lives = Lives(self.SCREEN)
        self.obstaclesAndPowerUps = ObstaclesAndPowerUps(self.lives, self.PowerUpVariables)
        self.obstaclesAndPowerUps.createObstaclesAndPowerUps()
            
        while keepGoing:
            clock.tick(30)
            
            for event in pygame.event.get():
                            
                if event.type == pygame.QUIT:
                    keepGoing = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
                        break
                    
                    if event.key == pygame.K_SPACE:
                        self.boundaries.PowerUpVariables.speedBoost(True)    #use boundaries to call it
            
            self.SCREEN.blit(self.BACKGROUND, (0, 0)) 
            self.boundaries.updateBoundaries(self.SCREEN)
            
            self.obstaclesAndPowerUps.updateAndDrawObstacles(self.SCREEN, self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X())
            self.obstaclesAndPowerUps.updateAndDrawPowerUps(self.SCREEN, self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X())       
            
            self.obstaclesAndPowerUps.checkPowerUpCollisions(self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X(), self.boundaries.getDotX(), self.boundaries.getDotY())       
            self.obstaclesAndPowerUps.checkObstacleCollisions(self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X(), self.boundaries.getDotX(), self.boundaries.getDotY())       
    
            self.manageObjects_Laser.manageLaser(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Laser, self.SCREEN)
            self.manageObjects_Ball.manageBall(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Ball, self.SCREEN)
            self.manageObjects_Multi_Laser.manageMultiLaser(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Multi_Laser, self.SCREEN)
            self.manageObjects_Power_Wave.managePowerWave(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Power_Wave, self.SCREEN)
            self.manageObjects_Target_Ball.manageTargetBall(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Target_Ball, self.SCREEN)
            
            self.boundaries.drawBoundaries(self.SCREEN) #placed here so manageObject_objects will go under it
            
            self.lives.drawHearts()
            self.PowerUp_Images.drawPowerUpImages()
    
            self.dot.drawDot(self.SCREEN)
            pygame.display.flip()
            
            
            if self.lives.NUMBER_OF_LIVES == 0:
                keepGoing = False
        
        return True