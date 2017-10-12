'''
Created on Dec 22, 2015

@author: ryan3971
'''

class ServerVariables():
    
    def __init__(self):
        
        self.START_GAME = 1
        self.OTHER_DOT = 2
        self.POWERUPS = 3
        self.OBSTACLES = 4  
              
        self.NEW_POWERUP = 5
        self.NEW_OBSTACLE = 6
        self.REMOVE_POWERUP = 7
        self.REMOVE_OBSTACLE = 8
        
        self.DOT_SIZE = 9
        self.DOT_INVISIBLE = 10
        self.DOT_SHEILD = 11
        
        self.ADD_LASER = 12
        self.REMOVE_LASER = 13
