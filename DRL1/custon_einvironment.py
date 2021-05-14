# -*- coding: utf-8 -*-
"""
Created on Fri May 14 08:32:05 2021

@author: MrSan
"""

import numpy as np
from gym import Env
from gym.spaces import Discrete, Box
import random
from sonar import sonar
from gps import gps
from controll import controll
from comms import comm

class random_sim:
    def __init__(self):
        
        self.front_sonar = sonar(18,24)
        self.right_sonar = sonar(,)
        self.left_sonar = sonar(,)
        self.GPS= gps()
        self.comms=comm()
    
    def get_readings(self):
        readings = np.array([self.front_sonar.getReadings(), self.front_sonar.getReadings(), self.front_sonar.getReadings(),
                             self.GPS.getlan(),self.GPS.getlon(),
                             self.comms.gettarget(], dtype = np.float32)
        return readings
    def sed_location():
        msg=self.GPS.getlan() + self.GPS.getlon()
        self.comms.sendcords(msg)

class TestEnv(Env):
    def __init__(self):
        self.action_space = Discrete(3)
        self.sim_readings = random_sim()
        #self.state = self.sim_readings.get_readings()
        self.state = 5
        self.observation_space = Box(np.array([0, 0, 0]), np.array([30, 30, 30,100,100]), dtype = np.float32)
        self.episode_length = 2
        self.move=controll()
        
        
    def step(self, action):
        if action == 0:
            self.move.front()          
        elif action == 1:
            self.move.right()
        elif action == 2:
            self.move.left()
        else: ValueError('invalid action')
        
        
        if self.episode_length == 0:
            done = True
        else:
            #self.episode_length= self.episode_length-1
            done = False

        if min(self.state[:4]) == 10:
            reward = -1
        else:
            reward = 1
            
        

        info = {}
        #self.state = self.sim_readings.get_readings()
        return self.state, reward, done, info
    
    def reset(self):
        self.episode_length = 10
        self.state = self.sim_readings.get_readings()
        return self.state
   
    

#----------------------------test environment----------------------------------
"""
env = TestEnv()  
episodes = 2
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0
    
    while not done:
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode, score))
"""
