'''
Created on Dec 14, 2015

@author: ryan3971
'''

import socket
import threading
import pickle
import multiprocessing

TIMEOUT = 1                      #Time before it stops checking for recieve
BUF_SIZE = 1024                  #max amount of data sent

SOCKET = socket.socket()         # Create a socket object
HOST = ''                        # IP address of PI here
PORT = 12345                     # Reserve a port for your service.
#SOCKET.bind((HOST, PORT))        # Bind to the port



class Server():
            
    def sendPlayerTheirTag(self, socket, playerTag):
        
        playerTagList = [playerTag]     #As a list so client will know it is recieveing the player tag
        socket.send(pickle.dumps(playerTagList))


    def sendData(self, socket, dataList):
        socket.send(dataList)

    
    def main(self, hold):
        
        self.ServerThreadList = []
        playersEntered = 0
        self.i = 1
        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        SOCKET.bind((HOST, PORT))
        SOCKET.listen(2)
        print "Waiting..."
                
        while playersEntered != 2:
            try:
                playerTag = playersEntered
                socket_connection, address = SOCKET.accept()
                
                hold.ServerClass = self
                hold.socket = socket_connection
                
         #       for num in range(100):
                print 1
                process = multiprocessing.Process(target = worker, args = (address, playerTag, 1))
                print 2
                process.start()
                print 3
                    
                self.ServerThreadList.append(socket_connection)
                
                playersEntered += 1
                print "Connected"
                    
            except Exception, e:
                print e
                
                
    def sendDataToOtherPlayers(self, dataList):
        
        dataListUnloaded = pickle.loads(dataList)
        playerTag = dataListUnloaded[0]
        
        if playerTag == 0:
            socket = self.ServerThreadList[1]
            socket.sendData(dataList)
            
                
        elif playerTag == 1:
            socket = self.ServerThreadList[0]
            socket.sendData(dataList)            
    
def worker(address, playerTag, num):
        
        SOCKET_CONNECTION = hold.socket
        ADDRESS = address
        IP = address[0]
        PLAYER_TAG = playerTag
        num = num
        
        print 1
        
        ServerClass = hold.ServerClass
        
        print ServerClass
                
        SOCKET_CONNECTION.settimeout(TIMEOUT)
        ServerClass.sendPlayerTheirTag(SOCKET_CONNECTION, PLAYER_TAG)
        
        i = 0

        while True:
            try:
                dataList = SOCKET_CONNECTION.recv(BUF_SIZE)
                ServerClass.sendDataToOtherPlayers(dataList)
                
                print "THREAD:   ", num , '   -    Server:   ', i
                i += 1
                
            except Exception, e:
                # timed out
                pass
            
            
class hold():
    
    ServerClass = None
    socket = None
    
    def __init__(self):
        
        hold.ServerClass = None
        hold.socket = None
            
if __name__ == '__main__':
    start = Server()
    hold = hold()
    start.main(hold)
                