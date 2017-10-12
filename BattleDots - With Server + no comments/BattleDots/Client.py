'''
Created on Dec 14, 2015

@author: ryan3971
'''

import socket
import threading
import pickle
from ServerVariables import ServerVariables
from InitiateClass import InitiateClass
from ClientVariables import ClientVariables

HOST = '192.168.2.152'
PORT = 12345
TIMEOUT = 1
BUF_SIZE = 1024
SOCKET_CONNECTION = None
CLIENT = None

class ClientReciveThread(threading.Thread, ClientVariables):

    def __init__(self, socket_connection, client):  #client is the class Client() so can call functions within Client()
        threading.Thread.__init__(self)
        self.SOCKET_CONNECTION = socket_connection
        self.SV = ServerVariables()
        self.CV = ClientVariables
        
    def run(self):        
        print "Good"
        while True:
            try:
                
                dataList = self.SOCKET_CONNECTION.recv(BUF_SIZE)
                self.recieveData(dataList)
                
            except Exception, e:
                # timed out
                pass
            
            
    def recieveData(self, dataList):
        
        dataList = pickle.loads(dataList)
        
        if len(dataList) == 1:      # This is the players tag, not data
            playerTag = dataList[0]
            self.CV.PLAYER_TAG = playerTag
            
        else:
            
            playerTag = dataList[0]
            referenceTag = dataList[1]
            data = dataList[2]
            
            if referenceTag == 7:
                print "YAAAAAAAAAAAAAAAAAAAAAAA"
                        
            
            if playerTag != self.CV.PLAYER_TAG:        #id player tag doesn't equal the players tag
               
                if referenceTag == self.SV.START_GAME:
                    self.CV.START_GAME = data
                
                if referenceTag == self.SV.OTHER_DOT:
                    self.CV.DOT_2_X = data[0]
                    self.CV.DOT_2_Y = data[1]
                
                if referenceTag == self.SV.OBSTACLES:
                    self.CV.OBSTACLE_LIST_X.append(data[0])
                    self.CV.OBSTACLE_LIST_Y.append(data[1])
                    print len(self.CV.OBSTACLE_LIST_Y)
                
                if referenceTag == self.SV.POWERUPS:
                    self.CV.POWERUPS_LIST_X.append(data[0])
                    self.CV.POWERUPS_LIST_Y.append(data[1])
                    
                if referenceTag == self.SV.REMOVE_OBSTACLE:
                    self.CV.OBSTACLE_LIST_X.pop(data)
                    self.CV.OBSTACLE_LIST_Y.pop(data)
                
                if referenceTag == self.SV.REMOVE_POWERUP:
                    self.CV.POWERUPS_LIST_X.pop(data)
                    self.CV.POWERUPS_LIST_Y.pop(data)
                    print "REMOVED"
                
                if referenceTag == self.SV.NEW_POWERUP:
                    self.CV.NEW_POWERUP = data

                if referenceTag == self.SV.NEW_OBSTACLE:
                    self.CV.NEW_OBSTACLE = data
                                    
                if referenceTag == self.SV.DOT_SIZE:
                    self.CV.DOT_2_SIZE = data
                    
                if referenceTag == self.SV.DOT_INVISIBLE:
                    self.CV.DOT_2_INVISIBLE = data
                    
                if referenceTag == self.SV.DOT_SHEILD:
                    self.CV.DOT_2_SHEILD = data
                '''
                if referenceTag == self.SV.ADD_LASER:
                    self.LASER_2.append(data)
                    
                if referenceTag == self.SV.REMOVE_LASER:
                    self.LASER_2.pop()
                '''
                    
                '''
                elif referenceTag == 2:
                    print 1
                    
                elif referenceTag == 3:
                    print 1
            
                '''
            
    
     
SOCKET = None

class Client():
    
    START_GAME = False
    
    def __init__(self, host = HOST, port = PORT):
                
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.i = 1

        try:
            self.SOCKET.connect((host, port))
            
         #   for x in range(0, 5):
            self.clientThread = ClientReciveThread(self.SOCKET, self)
            self.clientThread.daemon = True                                 # allows the program to close while the thread is still running
            self.clientThread.start()
            
            self.STATUS = "Connected"
            self.STATUS_NUM = 1
        except:
            self.STATUS = "Connection Failed"
            self.STATUS_NUM = 0
            
    def getStatus(self):
        return self.STATUS, self.STATUS_NUM
    
    def sendData(self, playerTag, referenceTag, data):
        
        dataSent = False
        dataList = [playerTag, referenceTag, data]
        print "SEND:    ",self.i
        self.i += 1
        
        while dataSent == False:
            try:
                self.SOCKET.send(pickle.dumps(dataList))
                dataSent = True
            except:
                dataSent = False
                #except something, not sure what yet
                
    
