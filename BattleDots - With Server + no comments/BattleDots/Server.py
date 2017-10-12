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
HOST = '192.168.2.152'                        # IP address of PI here
PORT = 12345                     # Reserve a port for your service.
#SOCKET.bind((HOST, PORT))        # Bind to the port



class Server():

    def worker(self, socket_connection, address, playerTag, num):
        
        self.SOCKET_CONNECTION = socket_connection
        self.ADDRESS = address
        self.IP = address[0]
        self.PLAYER_TAG = playerTag
        self.num = num
        
        self.SOCKET_CONNECTION.settimeout(TIMEOUT)
        self.sendPlayerTheirTag(self.PLAYER_TAG)

        while True:
            try:
                dataList = self.SOCKET_CONNECTION.recv(BUF_SIZE)
                self.sendDataToOtherPlayers(dataList)
                
                print "THREAD:   ", self.num , '   -    Server:   ', self.i
                self.i += 1
                
            except Exception, e:
                # timed out
                pass
            
    def sendPlayerTheirTag(self, playerTag):
        
        playerTagList = [playerTag]     #As a list so client will know it is recieveing the player tag
        self.SOCKET_CONNECTION.send(pickle.dumps(playerTagList))


    def sendData(self, dataList):
        self.SOCKET_CONNECTION.send(dataList)

    
    def main(self):
        
        self.ServerThreadList = []
        playersEntered = 0
        self.i = 1
        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        SOCKET.bind((HOST, PORT))
        SOCKET.listen(2)
        print "Waiting..."
                
        while True:#playersEntered != 2:
            try:
                playerTag = playersEntered
                socket_connection, address = SOCKET.accept()
                
         #       for num in range(100):
                print 1
                process = multiprocessing.Process(target = self.worker, args = (socket_connection, address, playerTag, 1))
                print 2
                process.start()
                print 3
                    
                self.ServerThreadList.append(self.server)
                
                playersEntered += 1
                print "Connected"
                    
            except Exception, e:
                print e
                
                
    def sendDataToOtherPlayers(self, dataList):
        
        dataListUnloaded = pickle.loads(dataList)
        playerTag = dataListUnloaded[0]
        
        if playerTag == 0:
            self.ServerThreadList[1].sendData(dataList)
            
                
        elif playerTag == 1:
            self.ServerThreadList[0].sendData(dataList)
            
            
start = Server()
start.main()
            
