# -*- coding: utf-8 -*-
"""
Created on Thu May 04 05:00:41 2021

@author: MrSan
"""
import socket

class comm:
    def __init__(self):
        self.clientSocket = socket.socket()
        port = 9091
        self.clientSocket.connect(('127.0.0.1', port))
               
    def getTarget(self):
        ak = '0'
        self.clientSocket.send(ak.encode())
        lat = self.clientSocket.recv(1024)
        lon = self.clientSocket.recv(1024)
        self.target_lat = float(lat.decode('utf-8'))
        self.target_lon = float(lon.decode('utf-8'))

    def sendTarget(self, lat, lon):
        ak = 1
        self.clientSocket.send(ak.encode())
        self.clientSocket.send(lat.encode())
        self.clientSocket.send(lon.encode())
        
    def clean_socket():
        pass
        