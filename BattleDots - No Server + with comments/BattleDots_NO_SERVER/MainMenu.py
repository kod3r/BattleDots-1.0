'''
Created on Dec 16, 2015

@author: ryan3971
'''
import pygame
import PygButton
from InitiateClass import InitiateClass


class MainMenu():
    
    def __init__(self, screen, backgound):
        
        '''
        Initiates variables
        
        @param screen: The display variable. Used to draw the main menu
        @param screen: The background variable. Used for drawing the background
        '''
        
        self.SCREEN = screen
        self.BACKGROUND = backgound
        
        self.initiateClass = InitiateClass()
        self.HEIGHT = self.initiateClass.getHeight()
        self.WIDTH = self.initiateClass.getWidth()
        
        self.TITLE_TEXT = ("BattleDots")
        insFont = pygame.font.SysFont(None, 200)
        self.TITLE = insFont.render(self.TITLE_TEXT, 1, (255, 255, 0))

        rect = pygame.Rect(self.WIDTH / 5, self.HEIGHT / 1.75, 200,200)
        self.START_GAME = PygButton.PygButton(rect, 'Start Game')
        
        rect = pygame.Rect(self.WIDTH / 2.35, self.HEIGHT / 1.75, 200,200)
        self.INSTRUCTIONS = PygButton.PygButton(rect, 'Instructions')
        
        rect = pygame.Rect(self.WIDTH / 1.5, self.HEIGHT / 1.75, 200,200)
        self.EXIT = PygButton.PygButton(rect, 'EXIT')

        
    def createMenuScreen(self):
        
        '''
        Draws and continue drawing the main menu untill a button is clicked
        '''
       
        keepGoing = True
        choice = 0
        
        clock = pygame.time.Clock()

        while keepGoing:
            clock.tick(30)
            
            for event in pygame.event.get():
                        
                if event.type == pygame.QUIT:
                    keepGoing = False
                    choice = 0
                    break

                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
                        choice = 0
                        break
                    
                if 'click' in self.START_GAME.handleEvent(event):
                    keepGoing = False
                    choice = 1
                    break
                
                if 'click' in self.INSTRUCTIONS.handleEvent(event):
                    keepGoing = False
                    choice = 2
                    break
                    
                if 'click' in self.EXIT.handleEvent(event):
                    keepGoing = False
                    choice = 0
                    break
                    
                    
            self.SCREEN.blit(self.BACKGROUND, (0, 0)) 
            self.SCREEN.blit(self.TITLE, (0, 0))
            self.START_GAME.draw(self.SCREEN)
            self.INSTRUCTIONS.draw(self.SCREEN)
            self.EXIT.draw(self.SCREEN)


            pygame.display.flip()
            
        return choice