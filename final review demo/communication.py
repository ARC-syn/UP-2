# -*- coding: utf-8 -*-
"""
Created on Tue May 25 23:39:57 2021

@author: MrSan
"""

import socket
import struct

class comm:
    def __init__(self):
        self.ClientSocket = socket.socket()
        host = '127.0.0.1'
        port = 1233
        
        print('Waiting for connection')
        try:
            self.ClientSocket.connect((host, port))
        except socket.error as e:
            print(str(e))
        print('connected')
        
    def getTarget(self):
        
        #------------send request to server as zero---------------------------
        req = 0
        req = req.to_bytes(2, 'big')
        self.ClientSocket.send(req)
        
        #-----------recive latitude and longituse as response------------------
        lat = self.ClientSocket.recv(4)          #recive latitude
        [lat] = struct.unpack('f', lat)          #conver response from byte to float
        self.lat = lat
        print(lat)
        lon = self.ClientSocket.recv(4)          #recive longitude
        [lon] = struct.unpack('f', lon)          #conver longituse from byte to float
        self.lon = lon
        print(lon)
        
        
    def sendTarget(self, lat, lon):
        #------------------send request as one--------------------------------
        req = 1
        req = req.to_bytes(2, 'big')
        self.ClientSocket.send(req)
        
        #---------------------send target cordinates---------------------------
        lat = bytearray(struct.pack("f", lat))       #convert latitude from float to byte
        self.ClientSocket.send(lat)                  #send latitude in byte formate
        
        lon = bytearray(struct.pack("f", lon))       #convert longitude from float to byte
        self.ClientSocket.send(lon)                  #send longitude in byte formate
        
new = comm()
new.sendTarget(2.345, 5.678)
