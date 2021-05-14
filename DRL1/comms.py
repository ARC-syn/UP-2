# -*- coding: utf-8 -*-
"""
Created on Thu May 04 05:00:41 2021

@author: MrSan
"""
import socket

class comm:
    def __init__(self):
        # Import socket module
        self.targetlist=[]
        self.s = socket.socket()		
        self.port = 12347				
        self.s.connect(('127.0.0.1', self.port))
        cords = self.s.recv(1024)
        self.targetlist.append(cords)
        
    def gettarget(self):
        return self.targetlst[0]
    
    def sendCords(self, message):
        self.s.send(message.encode('ascii'))
        
    def cleanComms(self):
        self.s.close()	
    