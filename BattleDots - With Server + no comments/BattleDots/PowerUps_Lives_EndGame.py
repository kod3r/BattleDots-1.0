'''
Created on Dec 18, 2015

@author: ryan3971
'''

import pygame

class Lives():
    
    HEART = 0
    HEART_RECT = 0
    
    def __init__(self, screen):
        
        self.SCREEN = screen
        
        self.NUMBER_OF_LIVES = 5
                
        self.HEART = pygame.image.load("Images/heart_scaled.png")
        self.HEART_RECT = self.HEART.get_rect()
            
        
    def drawHearts(self):
        
        heart_x = 0
        
        
        for heart_num in range(0, self.NUMBER_OF_LIVES):
            
            heart_x += self.HEART_RECT.width
            self.HEART_RECT.x = heart_x
            
            self.SCREEN.blit(self.HEART, self.HEART_RECT)
            
            
    def LossLife(self):
        self.NUMBER_OF_LIVES -= 1
        
        
        
        
class PowerUpsInUse():
    
    
    
    def __init__(self, screen):
        
        self.IS_SIZE_LARGE = False
        self.IS_SIZE_SMALL = False
        self.IS_SPEED_FAST = False
        self.IS_SPEED_SLOW = False
        self.IS_OPPOSITE_DIRECTION = False
        self.IS_INVISIBLE = False
        self.IS_LASER = []
        self.IS_BOUNCING_BALL = False
        self.IS_SHEILD = False
        self.IS_MULTI_LASER = False
        self.IS_TARGET_BALL = False
        
        self.SIZE_LARGE = pygame.image.load("Images/blue_dot_scaled_1.png")
        self.SIZE_SMALL = pygame.image.load("Images/blue_dot_scaled_2.png")
        self.SPEED_FAST = pygame.image.load("Images/blue_dot_scaled_3.png")
        self.SPEED_SLOW = pygame.image.load("Images/blue_dot_scaled_4.png")
        self.OPPOSITE_DIRECTION = pygame.image.load("Images/blue_dot_scaled_5.png")
        self.INVISIBLE = pygame.image.load("Images/blue_dot_scaled_6.png")
        self.LASER = pygame.image.load("Images/blue_dot_scaled_7.png")
        self.BOUNCING_BALL = pygame.image.load("Images/blue_dot_scaled_8.png")
        self.SHEILD = pygame.image.load("Images/blue_dot_scaled_9.png")
        self.MULTI_LASER = pygame.image.load("Images/blue_dot_scaled_10.png")
        self.TARGET_BALL = pygame.image.load("Images/blue_dot_scaled_11.png")
        
        self.SIZE_LARGE_RECT = self.SIZE_LARGE.get_rect()
        self.SIZE_SMALL_RECT = self.SIZE_SMALL.get_rect()
        self.SPEED_FAST_RECT = self.SPEED_FAST.get_rect()
        self.SPEED_SLOW_RECT = self.SPEED_SLOW.get_rect()
        self.OPPOSITE_DIRECTION_RECT = self.OPPOSITE_DIRECTION.get_rect()
        self.INVISIBLE_RECT = self.INVISIBLE.get_rect()
        self.LASER_RECT = self.LASER.get_rect()
        self.BOUNCING_BALL_RECT = self.BOUNCING_BALL.get_rect()
        self.SHEILD_RECT = self.BOUNCING_BALL.get_rect()
        self.MULTI_LASER_RECT = self.MULTI_LASER.get_rect()
        self.TARGET_BALL_RECT = self.TARGET_BALL.get_rect()
        
        self.SCREEN = screen
        
        
    def drawPowerUpImages(self):
        
        powerUp_Images_List = []
        powerUp_Images_Rect_List = []
        
        distance_y = 0
        
        if self.IS_SIZE_LARGE == True:
            powerUp_Images_List.append(self.SIZE_LARGE)
            self.SIZE_LARGE_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.SIZE_LARGE_RECT)
            distance_y += self.SIZE_LARGE_RECT.height
            
        if self.IS_SIZE_SMALL == True:
            powerUp_Images_List.append(self.SIZE_SMALL)
            self.SIZE_SMALL_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.SIZE_SMALL_RECT)
            distance_y += self.SIZE_SMALL_RECT.height
            
        if self.IS_SPEED_FAST == True:
            powerUp_Images_List.append(self.SPEED_FAST)
            self.SPEED_FAST_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.SPEED_FAST_RECT)
            distance_y += self.SPEED_FAST_RECT.height
            
        if self.IS_SPEED_SLOW == True:
            powerUp_Images_List.append(self.SPEED_SLOW)
            self.SPEED_SLOW_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.SPEED_SLOW_RECT)
            distance_y += self.SPEED_SLOW_RECT.height
            
        if self.IS_OPPOSITE_DIRECTION == True:
            powerUp_Images_List.append(self.OPPOSITE_DIRECTION)
            self.OPPOSITE_DIRECTION_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.OPPOSITE_DIRECTION_RECT)
            distance_y += self.OPPOSITE_DIRECTION_RECT.height
            
        if self.IS_INVISIBLE == True:
            powerUp_Images_List.append(self.INVISIBLE)
            self.INVISIBLE_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.INVISIBLE_RECT)
            distance_y += self.INVISIBLE_RECT.height
            
        if len(self.IS_LASER) != 0:
            
            laser_image_num  = len(self.IS_LASER)   #use to show corresponding image
            
            powerUp_Images_List.append(self.LASER)
            self.LASER_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.LASER_RECT)
            distance_y += self.LASER_RECT.height
            
        if self.IS_BOUNCING_BALL == True:
            powerUp_Images_List.append(self.BOUNCING_BALL)
            self.BOUNCING_BALL_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.BOUNCING_BALL_RECT)
            distance_y += self.BOUNCING_BALL_RECT.height
            
        if self.IS_SHEILD == True:
            powerUp_Images_List.append(self.SHEILD)
            self.SHEILD_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.SHEILD_RECT)
            distance_y += self.SHEILD_RECT.height
            
        if self.IS_MULTI_LASER == True:
            powerUp_Images_List.append(self.MULTI_LASER)
            self.MULTI_LASER_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.MULTI_LASER_RECT)
            distance_y += self.MULTI_LASER_RECT.height
            
        if self.IS_TARGET_BALL == True:
            powerUp_Images_List.append(self.TARGET_BALL)
            self.TARGET_BALL_RECT.y = distance_y
            powerUp_Images_Rect_List.append(self.TARGET_BALL_RECT)
            distance_y += self.TARGET_BALL_RECT.height
            
        list_size = len(powerUp_Images_List)
        
        for num in range(0, list_size):
            self.SCREEN.blit(powerUp_Images_List[num], powerUp_Images_Rect_List[num])

        
    def showSizeLargeImage(self, showImage):
        self.IS_SIZE_LARGE = showImage
        
        
        
    def showSizeSmallImage(self, showImage):
        self.IS_SIZE_SMALL = showImage



    def showSpeedFastImage(self, showImage):
        self.IS_SPEED_FAST = showImage



    def showSpeedSlowImage(self, showImage):
        self.IS_SPEED_SLOW = showImage




    def showOppositeDirectionImage(self, showImage):
        self.IS_OPPOSITE_DIRECTION = showImage




    def showInvisibleImage(self, showImage):
        self.IS_INVISIBLE = showImage




    def showLaserImage(self, showImage):
        
        if showImage == False:
            self.IS_LASER.pop()
        else:
            self.IS_LASER.append(1)


        
    def showBouncingBallImage(self, showImage):
        self.IS_BOUNCING_BALL = showImage
        
        
    def showSheildImage(self, showImage):
        self.IS_SHEILD = showImage
        
    def showMultiLaserImage(self, showImage):
        self.IS_MULTI_LASER = showImage
        
        
    def showTargetBallImage(self, showImage):
        self.IS_TARGET_BALL = showImage
        
