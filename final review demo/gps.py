# -*- coding: utf-8 -*-
"""
Created on Sun May 02 06:33:19 2021

@author: MrSan
"""

import serial
import time
import string
import pynmea2

class gps:
    def __init__(self):
        self.port = "/dev/ttyAMA0"
        self.ser=serial.Serial(self.port, baudrate=9600, timeout=0.5)
        self.dataout = pynmea2.NMEAStreamReader()
        
    def getlan(self):
        self.newdata=self.ser.readline()
        if self.newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(self.newdata)
            return newmsg.lattitude
        else :
            return 0
        
    def getlon(self):
        self.newdata=self.ser.readline()
        if self.newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(self.newdata)
            return newmsg.longitude
        else :
            return 0
        