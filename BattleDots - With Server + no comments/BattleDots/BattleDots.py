'''
Created on Nov 9, 2015

@author: ryan3971
'''

import pygame
from MainMenu import MainMenu
from Game import Game
from ServerVariables import ServerVariables
from ClientVariables import ClientVariables
import sys


pygame.init()
screen = pygame.display.set_mode((800, 1000), pygame.RESIZABLE)

pygame.display.set_caption("BattleDots")
background = pygame.Surface(screen.get_size()) 
background.fill((255 , 255, 255)) 

class BattleDots(ClientVariables):

    CLIENT = None
    
    def __init__(self):
        
        self.CLIENT = None
        self.SV = ServerVariables()
        self.CV = ClientVariables

    def doMenu(self):
        
        ''' 
        Creates and runs the Main Menu screen
        '''
        
        main = MainMenu(screen, background, self.CLIENT)
        startGame, client = main.createMenuScreen()
        
        if client != None:
            self.CLIENT = client
        
        if startGame == True:
            self.connectAndStart()
        else:
            sys.exit()
                    
    def connectAndStart(self):
        
        '''
        Ensures both players have clicked the "Start Game
         button before starting the game
        '''
        
        self.CLIENT.sendData(self.CV.PLAYER_TAG, self.SV.START_GAME, True)
        startGame = False

        while startGame == False:
            startGame = self.CV.START_GAME
        
        self.CV.START_GAME = False          #reset for next game
        self.doGame()

                    
    def doGame(self):
        
        '''
        Starts the Game
        '''
        game = Game(screen, background, self.CLIENT)
        game.game()
            
        self.doMenu()
    
b = BattleDots()
b.doMenu()
        
''' top left corner is (0,0), therefore up is a negative and down is a positive'''
''' might make aquiring x and y from angle a function in a helper class'''

'''BUGS:
        - when hit boundaries, slightly moves obstacles and powerUps ---FIXED
        - when get powerups when against bondaries, moves obstacles and powerups ---FIXED
        - boundaries not perfectly lined up with boundaries on right and bottom from decimals - I think
        - sometimes error when makeing laser - says index is out of bounds for LASER_X_ON_SCREEN_LOCATION in shootLaser class in updateAndDrawLaser function ---FIXED
        - make things such as speed and size defined by screen size, not a set number
        - importing is a little confusing
        - laser collisions with boundaries not perfect. Should have it do similar collisions to what Dot does
        - BouncingBall would move all wackey when ball was moving against boundaries
        - laser and Bouncing ball collisions with boundaries issues
        - Doesn't draw laser and ball at same time ---FIXED
        - speed boost causes major issues with lassr bouncing
        -if were to grow big, good chance of hitting obstacle near by. Should reduce number of power up and obstacles, and have a clear radius around each one ---SHOULD BE FINE NOE
        -go back to normal size when shoot laser or ball
        -issue with laser
        -Target ball goes outside of boundaries
        -destructor for cleanup needed
        - new power ups and obstacles not working cause of first two lines
        -collisions with multi lasers bad. Do draw boundary after
        -formation of new obstacles and powerups may be off still
        -new objects may not do collisions right away
        -chance that dot appears on powerup or obstacle at start of game
        
NOTE:
        - When adding dots location to stuff, subtract x, and add y - NOT ANYMORE
        - use the if if __name__ == '__main__':  thingy if run into import issue again
IDEAS:
        - ball that follows opponent, updates head towards every 5 seconds, if hit boundaries, destroyed
        - if have sheild, when touch obstacle, destroy sheild and obstacle. will than need to create new obstacle. - issue with that is may be cretate where player is
        - for invisible, only changes alpha. but oppoenet cant see you
        - sheild radius will need to be accounted for for collisions
        - for menu, retunr what button is clicked. depending on what is returned, start designated function
        - obstacles and powerups in set locations, in line with one another, grid-like formation
        - may have PowerWave destroy all objects and power ups
        - if collisions for balls continue to be bad, try including the instantaneous movement x and y in the self coordinates. Might make more accurate
        
        -LAST RESORT - collisions with lasers and ball, draw boundaries after laser and ball are drawn
THINGS:
        - BUTTONS
        - SPRITES
        - SERVERS
        
OTHER:
        -For powerups like incease or decrease speed or size, goes to extreme instead of a gradual change
'''
