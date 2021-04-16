import numpy as np
from gym import Env
from gym.spaces import Discrete, Box
import random

class random_sim:
    def __init__(self):
        pass
    
    def get_readings(self):
        readings = np.array([random.randrange(1,30), random.randrange(1,30), random.randrange(1,30)])
        return tuple(readings)

class TestEnv(Env):
    def __init__(self):
        self.action_space = Discrete(3)
        self.sim_readings = random_sim()
        self.state = self.sim_readings.get_readings()
        self.observation_space = Box(np.array([0, 0, 0]), np.array([30, 30, 30]), dtype = np.float32)
        self.episode_length = 2
        
    def step(self, action):
        if action == 0:
            print('front')           
        elif action == 1:
            print('left')
        elif action == 2:
            print('right')
        else: ValueError('invalid action')
        
        
        if self.episode_length == 0:
            done = True
        else:
            self.episode_length= self.episode_length-1
            done = False

        if min(self.state) == 10:
            reward = -1
        else:
            reward = 1

        info = {}
        self.state = self.sim_readings.get_readings()
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
