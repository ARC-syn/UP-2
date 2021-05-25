# -*- coding: utf-8 -*-
"""
Created on Tue May 25 23:41:53 2021

@author: MrSan
"""

import socket
import os
from _thread import *
import struct


#store target location
class target_list:
    def __init__(self):
        self.lat = bytearray(struct.pack("f", 0.000))
        self.lon = bytearray(struct.pack("f", 0.000))
        
    def setter(self, lat, lon):
        self.lat = lat
        self.lon = lon
        #self.lon = lon
    
#-------------------------------create socket----------------------------------
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)  #start listening to the port

new = target_list()  #initialize target_list calls to store target cordinates

def threaded_client(connection):                #serve client requests
    while True:
        Response = connection.recv(2)           #recive client request 0 or 1
        req = int.from_bytes(Response, "big")   #decode client request from byte to int
        print(req)
        if req == 0:
            connection.send(new.lat)            #send latitude stored in class target_list class
            connection.send(new.lon)            #send longitude stored in class target_list class
            
        if req == 1:
            lat = connection.recv(4)            #recive latitude from client
            [x] = struct.unpack('f', lat)       #decode from byte to float
            
            lon = connection.recv(4)            #recive longitude from client
            [y] = struct.unpack('f', lon)       #decode to float
            print(x)
            print(y)
            new.setter(lat , lon)              #storre latitude and longitude in target_list class using setter function
               
    connection.close()

#-------------------initiate new client connection-----------------------------------
while True:
    Client, address = ServerSocket.accept()   #connect to client
    print('Connected to: ' + address[0] + ':' + str(address[1])) #print client details
    start_new_thread(threaded_client, (Client, ))  #create a thread for client
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()











