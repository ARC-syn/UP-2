# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:50:57 2021

@author: MrSan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 16 17:40:14 2021

@author: MrSan
"""
import socket
import os
from _thread import *


#store target location
class target_list:
    def __init__(self):
        self.lat = 'lat'
        self.lon = 'lon'
        
    def setter(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
#create socket
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

def threaded_client(connection):
    while True:
        Response = connection.recv(2)
        print(Response)
        req = int.from_bytes(Response, "big")
        print(req)
        if req == 0:
            print('sent hi')
            connection.send(str.encode(new.lat))
            #send two float values
            #connection.send(str.encode('hello'))
        if req == 1:
            #print('recived bye')
            Response = connection.recv(1024)
            #receive two float
            print(Response.decode('utf-8'))
            
            new.setter('bad')
        
        print('none')
        
    #connection.send(str.encode('Welcome to the Servern'))
    connection.close()

while True:
    Client, address = ServerSocket.accept()   #connect to client
    print('Connected to: ' + address[0] + ':' + str(address[1])) #print client details
    start_new_thread(threaded_client, (Client, ))  #create a thread for client
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()











