'''
Created on Dec 16, 2015

@author: ryan3971
'''
import pygame
import PygButton
from InitiateClass import InitiateClass
from Client import Client



class MainMenu():
    
    def __init__(self, screen, backgound, client):
        
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
        
        rect = pygame.Rect(self.WIDTH / 2.3, self.HEIGHT / 1.75, 200,200)
        self.CONNECT = PygButton.PygButton(rect, 'CONNECT')

        rect = pygame.Rect(self.WIDTH / 1.5, self.HEIGHT / 1.75, 200,200)
        self.EXIT = PygButton.PygButton(rect, 'EXIT')
        
        
        self.CLIENT = client
        
        if self.CLIENT != None:
            self.CLIENT_STATUS_NUM = 1
            self.CLIENT_STATUS_TEXT = ("Connected")
        else:
            self.CLIENT_STATUS_NUM = 0
            self.CLIENT_STATUS_TEXT = ("Not Connected")
        
        insFont = pygame.font.SysFont(None, 100)
        self.CLIENT_STATUS = insFont.render(self.CLIENT_STATUS_TEXT, 1, (255, 255, 0))

        
    def createMenuScreen(self):
       
        keepGoing = True
        startGame = False
        client = None
        
        clock = pygame.time.Clock()

        while keepGoing:
            clock.tick(30)
            
            for event in pygame.event.get():
                        
                if event.type == pygame.QUIT:
                    keepGoing = False
                    startGame = False
                    break

                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
                        startGame = False
        
                    
                if 'click' in self.START_GAME.handleEvent(event):
                    
                    if self.CLIENT != None:
                        keepGoing = False
                        startGame = True
                        break
                
                
                if 'click' in self.CONNECT.handleEvent(event):
                    
                    if self.CLIENT_STATUS_NUM == 0:
                        client = Client()
                        self.CLIENT_STATUS_TEXT, self.CLIENT_STATUS_NUM = client.getStatus()
                        
                        if self.CLIENT_STATUS_NUM == 1:
                            self.CLIENT = client
                            
                    else:
                        self.CLIENT_STATUS_TEXT = "Already Connected"
                        
                    insFont = pygame.font.SysFont(None, 100)
                    self.CLIENT_STATUS = insFont.render(self.CLIENT_STATUS_TEXT, 1, (255, 255, 0))
                    break
                    
                if 'click' in self.EXIT.handleEvent(event):
                    keepGoing = False
                    startGame = False
                    
            #       if self.CLIENT_STATUS_NUM == 1:
            #            self.CLIENT.disconnect()
                    
                    break
                    
                    
            self.SCREEN.blit(self.BACKGROUND, (0, 0)) 
            self.SCREEN.blit(self.TITLE, (0, 0))
            self.SCREEN.blit(self.CLIENT_STATUS, (self.WIDTH / 3, self.HEIGHT / 2.5))

            self.START_GAME.draw(self.SCREEN)
            self.CONNECT.draw(self.SCREEN)
            self.EXIT.draw(self.SCREEN)

            
            pygame.display.flip()
                
            pygame.display.flip()
            
        return startGame, self.CLIENT
