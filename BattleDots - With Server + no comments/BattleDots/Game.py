'''
Created on Dec 18, 2015

@author: ryan3971
'''


import pygame

from Boundaries import Boundaries
from Dot import Dot
from Dot_2 import Dot_2
#from InitiateClass import InitiateClass
from ManageObjects import ManageObjects
from ObstaclesAndPowerUps import ObstaclesAndPowerUps
from ObstaclesAndPowerUps_2 import ObstaclesAndPowerUps_2
from MainMenu import MainMenu
from PowerUps_Lives_EndGame import Lives

import PygButton
from PowerUpVariables import PowerUpVariables
from PowerUps_Lives_EndGame import PowerUpsInUse
from ServerVariables import ServerVariables
from Client import Client
from ClientVariables import ClientVariables

class Game(ClientVariables):
    
    def __init__(self, screen, backgound, client):
        
        self.SCREEN = screen
        self.BACKGROUND = backgound
        self.CLIENT = client
        self.SV = ServerVariables()
        self.CV = ClientVariables
            
    def game(self):                 
     
        keepGoing = True
    
        clock = pygame.time.Clock()
        
        self.PowerUp_Images = PowerUpsInUse(self.SCREEN)
        self.PowerUpVariables = PowerUpVariables(self.PowerUp_Images, self.CLIENT)
        
        self.dot = Dot(self.PowerUpVariables)
        self.dot_2 = Dot_2(self.PowerUpVariables)#, self.CLIENT)

        
        self.boundaries = Boundaries(self.PowerUpVariables)
        self.manageObjects_Laser = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Ball = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Multi_Laser = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Power_Wave = ManageObjects(self.PowerUpVariables)
        self.manageObjects_Target_Ball = ManageObjects(self.PowerUpVariables)
        self.lives = Lives(self.SCREEN)
        
        
        if self.CV.PLAYER_TAG == 0:
            self.obstaclesAndPowerUps = ObstaclesAndPowerUps(self.lives, self.PowerUpVariables, self.CLIENT)
            done = self.obstaclesAndPowerUps.createObstaclesAndPowerUps()
        else:
            self.obstaclesAndPowerUps_2 = ObstaclesAndPowerUps_2(self.lives, self.PowerUpVariables, self.CLIENT)
            
        
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
            
        #    self.sendClientDataXAndY(self.boundaries.getDotX(), self.boundaries.getDotY())
            
            
            if self.CV.PLAYER_TAG == 0:
                self.obstaclesAndPowerUps.updateAndDrawObstacles(self.SCREEN, self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X())
                self.obstaclesAndPowerUps.updateAndDrawPowerUps(self.SCREEN, self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X())       
                
                self.obstaclesAndPowerUps.checkPowerUpCollisions(self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X(), self.boundaries.getDotX(), self.boundaries.getDotY())       
                self.obstaclesAndPowerUps.checkObstacleCollisions(self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X(), self.boundaries.getDotX(), self.boundaries.getDotY())       
        
            else:
                self.obstaclesAndPowerUps_2.updateAndDrawObstacles(self.SCREEN, self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X())
                self.obstaclesAndPowerUps_2.updateAndDrawPowerUps(self.SCREEN, self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X())       
                
                self.obstaclesAndPowerUps_2.checkPowerUpCollisions(self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X(), self.boundaries.getDotX(), self.boundaries.getDotY())       
                self.obstaclesAndPowerUps_2.checkObstacleCollisions(self.boundaries.getObstaclesAndPowerUpsMovement_Y(), self.boundaries.getObstaclesAndPowerUpsMovement_X(), self.boundaries.getDotX(), self.boundaries.getDotY())       
        
        
            self.manageObjects_Laser.manageLaser(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Laser, self.SCREEN)
            self.manageObjects_Ball.manageBall(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Ball, self.SCREEN)
            self.manageObjects_Multi_Laser.manageMultiLaser(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Multi_Laser, self.SCREEN)
            self.manageObjects_Power_Wave.managePowerWave(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Power_Wave, self.SCREEN)
            self.manageObjects_Target_Ball.manageTargetBall(self.boundaries.getDotX(), self.boundaries.getDotY(), self.boundaries.getInstantaneousMovementX(), self.boundaries.getInstantaneousMovementY(), self.manageObjects_Target_Ball, self.SCREEN)
            
            self.boundaries.drawBoundaries(self.SCREEN) #placed here so manageObject_objects will go under it
            
            self.lives.drawHearts()
            self.PowerUp_Images.drawPowerUpImages()
    
            self.dot.drawDot(self.SCREEN)
            self.dot_2.drawDot2(self.SCREEN, self.boundaries.getDotX(), self.boundaries.getDotY())
            pygame.display.flip()
            
            
            if self.lives.NUMBER_OF_LIVES == 0:
                keepGoing = False
        
        return True
    
    
    
    def sendClientDataXAndY(self, x, y):
        self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.OTHER_DOT, [x, y])
        