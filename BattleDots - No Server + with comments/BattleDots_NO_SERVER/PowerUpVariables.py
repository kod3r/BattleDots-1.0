'''
Created on Dec 1, 2015

@author: ryan3971
'''



class PowerUpVariables():
    
    DOT_SPEED_FAST = False
    DOT_SPEED_SLOW = False
    DOT_SPEED = 0
    
    DOT_SIZE_LARGE = False
    DOT_SIZE_SMALL = False
    DOT_SIZE = 0
    
    DOT_OPPOSITE_DIRECTION = False
    DOT_VISIBLE = True
    DOT_SHEILD = False
    
    IS_SPEED_BOOST = False
    SPEED_BOOST_STAGE = 0
    SPEED_BOOST = 0
    
    PowerUp_Images = None
    
    def __init__(self, PowerUpsInUse):
        
        '''
        Initiates variable
        
        @param PowerUpVariables: passes the PowerUpVariables object
        '''
        
        self.DOT_SPEED = 10
        self.DOT_SIZE = 1
        
        self.DOT_SPEED_FAST = False
        self.DOT_SPEED_SLOW = False
        self.DOT_SIZE_LARGE = False
        self.DOT_SIZE_SMALL = False
        self.DOT_OPPOSITE_DIRECTION = False
        self.DOT_INVISIBLE = False
        self.DOT_SHEILD = False
        self.LASER_LIST = []
        self.BALL_LIST = []
        self.MULTI_LASER = False
        self.NEW_POWER_WAVE = False
        self.POWER_WAVE = False
        self.TARGET_BALL_LIST = []

        self.IS_SPEED_BOOST = False
        self.SPEED_BOOST_STAGE = 1
        self.SPEED_BOOST = 1.0
        
        self.PowerUp_Images = PowerUpsInUse

        
    def setDotSpeedFast(self, newSpeed):
        self.DOT_SPEED_FAST = newSpeed
        self.PowerUp_Images.showSpeedFastImage(newSpeed)
        self.setDotSpeed()
    
    def setDotSpeedSlow(self, newSpeed):
        self.DOT_SPEED_SLOW = newSpeed
        self.PowerUp_Images.showSpeedSlowImage(newSpeed)
        self.setDotSpeed()
        
    def setDotSpeed(self):
        
        if self.DOT_SPEED_FAST == True:
            self.DOT_SPEED = 20
        elif self.DOT_SPEED_SLOW == True:
            self.DOT_SPEED = 5
        else:
            self.DOT_SPEED = 10
        
        
    def getDotSpeedFast(self):
        return self.DOT_SPEED_FAST
        
    def getDotSpeedSlow(self):
        return self.DOT_SPEED_SLOW
        
        
    def getDotSpeed(self):
        return self.DOT_SPEED 
        
        
    def setDotSizeLarge(self, newSize):
        self.DOT_SIZE_LARGE = newSize
        self.PowerUp_Images.showSizeLargeImage(newSize)
        self.setDotSize()
        
    def setDotSizeSmall(self, newSize):
        self.DOT_SIZE_SMALL = newSize
        self.PowerUp_Images.showSizeSmallImage(newSize)
        self.setDotSize()
        
    def setDotSize(self):

        if self.DOT_SIZE_LARGE == True:
            self.DOT_SIZE = 3
        elif self.DOT_SIZE_SMALL == True:
            self.DOT_SIZE = 0.25
        else:
            self.DOT_SIZE = 1   
       
    
    def getDotSizeLarge(self):
        return self.DOT_SIZE_LARGE
    
    def getDotSizeSmall(self):
        return self.DOT_SIZE_SMALL
    
    def getDotSize(self):
        return self.DOT_SIZE  
    
    
    def setDotOppositeDirection(self, opposite_direction):
        self.DOT_OPPOSITE_DIRECTION = opposite_direction
        self.PowerUp_Images.showOppositeDirectionImage(opposite_direction)
        
    def getDotOppositeDirecton(self):
        return self.DOT_OPPOSITE_DIRECTION
    
    def setDotInvisible(self, invisible):
        self.DOT_INVISIBLE = invisible
        self.PowerUp_Images.showInvisibleImage(invisible)
        
    def getDotInvisible(self):
        return self.DOT_INVISIBLE
    
    
    
    
    def setLaserList(self, newLaser, index = None):
        
        if index == None:
            self.LASER_LIST.append(True)
            self.PowerUp_Images.showLaserImage(True)
        else:
            self.LASER_LIST[index] = newLaser
        
    def getLaserList(self):
        return self.LASER_LIST
    
    def destroyLaser(self):
        
        if len(self.LASER_LIST) != 0:   #simple precaution. Might need to put image inside also
            self.LASER_LIST.pop()
        self.PowerUp_Images.showLaserImage(False)
            
        
    
    def setBallList(self, newBall, index = None):
        
        if index == None:
            self.BALL_LIST.append(True)
            self.PowerUp_Images.showBouncingBallImage(True)
        else:
            self.BALL_LIST[index] = newBall

                
    def getBallList(self):
        return self.BALL_LIST
    
    
    
    def setDotSheild(self, isSheild):
        self.DOT_SHEILD = isSheild
        self.PowerUp_Images.showSheildImage(isSheild)
    
    def getDotSheild(self):
        return self.DOT_SHEILD
    
    
    def setMultiLaser(self, isMultiLaser):
        self.MULTI_LASER = isMultiLaser
    
    def getMultiLaser(self):
        return self.MULTI_LASER
    
    def showMultiLaserImage(self, showImage):
        self.PowerUp_Images.showMultiLaserImage(showImage)
        
    def setNewPowerWave(self, newWave):
        self.NEW_POWER_WAVE = newWave
        
    def getNewPowerWave(self,):
        return self.NEW_POWER_WAVE
        
    def setPowerWave(self, isPowerWave):
        self.POWER_WAVE = isPowerWave
        self.setNewPowerWave(isPowerWave)
    
    def getPowerWave(self):
        return self.POWER_WAVE
    
    
    
    def setTargetBallList(self, newTargetBall, index = None):
        
        if index == None:
            self.TARGET_BALL_LIST.append(True)
            self.PowerUp_Images.showTargetBallImage(True)
        else:
            self.TARGET_BALL_LIST[index] = newTargetBall

                
    def getTargetBallList(self):
        return self.TARGET_BALL_LIST
    
    
    def speedBoost(self, isSpeed = True):
        self.IS_SPEED_BOOST = isSpeed
        
        self.SPEED_BOOST_STAGE += 1
        speed_boost_stage = self.SPEED_BOOST_STAGE

        if speed_boost_stage == 1:
            self.SPEED_BOOST = 1.5
        elif speed_boost_stage == 2:
            self.SPEED_BOOST = 2.0
        elif speed_boost_stage == 3:
            self.SPEED_BOOST = 2.5
        elif speed_boost_stage == 4:
            self.SPEED_BOOST = 3.0
        elif speed_boost_stage == 5:
            self.SPEED_BOOST = 3.5        
        elif speed_boost_stage == 6:
            self.SPEED_BOOST = 3.0
        elif speed_boost_stage == 7:
            self.SPEED_BOOST = 2.5
        elif speed_boost_stage == 8:
            self.SPEED_BOOST = 2.0
        elif speed_boost_stage == 9:
            self.SPEED_BOOST = 1.5
        elif speed_boost_stage == 10:
            self.SPEED_BOOST = 1.0
            self.SPEED_BOOST_STAGE = 0
            self.IS_SPEED_BOOST = False
                        
            
    def isSpeedBoost(self):
        return self.IS_SPEED_BOOST
    
    def getSpeedBoost(self):
        return self.SPEED_BOOST
        