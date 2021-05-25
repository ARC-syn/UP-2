import numpy as np
from gym import Env
from gym.spaces import Discrete, Box
import random
"""
from communication import comm
from sonar import sonar
from gps import gps
from image_classifier import img_classifier
"""


class random_sim:
    def __init__(self):
        pass
        """
        self.front_sonar = sonar(18,24)
        self.right_sonar = sonar(19,20)
        self.left_sonar = sonar(21,22)
        self.GPS= gps()
        self.cam = img_classifier()
        self.comms=comm()
        """
    
    def get_readings(self): 
        
        """
        self.comms.getTarget()
        readings = np.array([self.front_sonar.getReadings(), self.front_sonar.getReadings(), self.front_sonar.getReadings(),
                             self.GPS.getlan(), self.GPS.getlon(),
                             self.comms.target_lat, self.comms.target_lon,
                             self.cam.classify_cam()], dtype = np.float32)
        """
        readings = np.array([random.randrange(1,30), random.randrange(1,30), random.randrange(1,30),
                            round(random.uniform(0, 100), 3), round(random.uniform(0, 100), 3),
                            round(random.uniform(0, 100), 3), round(random.uniform(0, 100), 3),
                            random.randrange(0,2)], dtype = np.float32)
        return readings

class TestEnv(Env):
    def __init__(self):
        self.action_space = Discrete(3)
        self.sim_readings = random_sim()
        self.state = self.sim_readings.get_readings()
        #self.state = 8
        self.observation_space = Box(np.array([0, 0, 0, 0, 0,0 ,0, 0]), np.array([30, 30, 30, 100, 100, 100, 100, 1]), dtype = np.float32)
        self.episode_length = 2
        
    def step(self, action):
        #---------------------------------------------apply action---------------------------------
        if action == 0:
            print('front')           
        elif action == 1:
            print('left')
        elif action == 2:
            print('right')
        else: ValueError('invalid action')
        
        self.state = self.sim_readings.get_readings() #get new observations from the real environment
        
        #-------------------------------------------------calculate reward---------------------------
        if min(self.state[:3]) == 15: #reward based on proximity sensor(sonar sensors)
            reward = -1
        else:
            reward = 0.1
        
        if self.state[3] == self.state[5] and self.state[4] == self.state[6]: #reward for reaching the target location(GPS readings)
            reward = reward + 0.1
            
        if self.state[7]:  # reward for finding the target (image classification)
            reward = reward +1
            #self.sim_readings.comms.sendTarget(self.random_sim.GPS.getlan(), self.random_sim.GPS.getlon())
        
        if self.episode_length == 0: #truncate post training
            done = True
        else:
            #self.episode_length= self.episode_length-1
            done = False


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
