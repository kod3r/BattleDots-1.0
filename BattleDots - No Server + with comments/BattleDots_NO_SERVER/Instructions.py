'''
Created on Jan 21, 2016

@author: ryan3971
'''

import pygame
import PygButton
from InitiateClass import InitiateClass


class Instructions():
    
    def __init__(self, screen, backgound):
        
        '''
        Initiates variables
        
        @param screen: The display variable. Used to draw the instructions
        @param screen: The background variable. Used for drawing the background
        '''
        
        self.SCREEN = screen
        self.BACKGROUND = backgound
        
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        
        self.INSTRUCTIONS_TEXT = (
        "Welcome to BattleDots!",
        "",
        "------------------------------------------------",
        "",
        "Use the mouse to move the dot",
        "",
        "------------------------------------------------",
        "",
        "Collide with a blue dot to",
        "",
        "activate a power up",
        "",
        "------------------------------------------------",
        "",
        "Watch out for the green dots",
        "",
        "or you'll lose a life",
        "",
        "------------------------------------------------",
        "",
        "Click the space bar for a speed boost",
        "",
        "------------------------------------------------",
        "",
        "Have fun!",
                                )
        
        
        insFont = pygame.font.SysFont(None, 85)
        self.insLabels = []
        
        for line in self.INSTRUCTIONS_TEXT:
            tempLabel = insFont.render(line, 1, (255, 255, 0))
            self.insLabels.append(tempLabel)
                    
        rect = pygame.Rect(self.WIDTH / 2.35, self.HEIGHT / 1.14, 100,100)
        self.BACK = PygButton.PygButton(rect, 'BACK')


        
    def createInstuctionsScreen(self):
        
        '''
        Draws and continue drawing the instructions until the back button is clicked
        '''
       
        keepGoing = True
        
        clock = pygame.time.Clock()

        while keepGoing:
            clock.tick(30)
            
            for event in pygame.event.get():
                 
                if 'click' in self.BACK.handleEvent(event):
                    keepGoing = False
                    break
                
                
            self.SCREEN.blit(self.BACKGROUND, (0, 0)) 
            
            for i in range(len(self.insLabels)):
                self.SCREEN.blit(self.insLabels[i], (50, 30*i))
            
            self.BACK.draw(self.SCREEN)
            
            pygame.display.flip()
            
        return True