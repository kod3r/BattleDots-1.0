'''
Created on Dec 27, 2015

@author: ryan3971
'''

from InitiateClass import InitiateClass

class ClientVariables():
    
    HEIGHT = 0
    WIDTH = 0
   
    TOP = 0
    BOTTOM = 0
    RIGHT = 0
    LEFT = 0
    
    START_GAME = False
    NEW_POWERUP = False
    NEW_OBSTACLE = False
        
    PLAYER_TAG = 0
    DOT_2_X = 0
    DOT_2_Y = 0
    
    OBSTACLE_LIST_X = []
    OBSTACLE_LIST_Y = []
    
    POWERUPS_LIST_X = []
    POWERUPS_LIST_Y = []
    
    DOT_2_SIZE = 1
    DOT_2_INVISIBLE = False
    DOT_2_SHEILD = False
    
    LASER_2 = []
    
    def __init__(self):
        
        self.initiateClass = InitiateClass()
        ClientVariables.HEIGHT = self.initiateClass.getHeight()
        ClientVariables.WIDTH = self.initiateClass.getWidth()
        
        ClientVariables.TOP = self.initiateClass.TOP
        ClientVariables.BOTTOM = self.initiateClass.BOTTOM
        ClientVariables.RIGHT = self.initiateClass.RIGHT
        ClientVariables.LEFT = self.initiateClass.LEFT
        
        ClientVariables.STATUS_NUM = 0
        
        ClientVariables.START_GAME = False
        ClientVariables.NEW_POWERUP = False
        ClientVariables.NEW_OBSTACLE = False
        
        ClientVariables.PLAYER_TAG = 0
        ClientVariables.DOT_2_X = self.RIGHT / 2
        ClientVariables.DOT_2_Y = self.BOTTOM / 2
        
        ClientVariables.OBSTACLE_LIST_X = []
        ClientVariables.OBSTACLE_LIST_Y = []
        
        ClientVariables.POWERUPS_LIST_X = []
        ClientVariables.POWERUPS_LIST_Y = []
        
        ClientVariables.DOT_2_SIZE = 1
        ClientVariables.DOT_2_INVISIBLE = False
        ClientVariables.DOT_2_SHEILD = False
        
        ClientVariables.LASER_2 = []
        