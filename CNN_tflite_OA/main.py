from sonar import sonar
from controll import controll
from CNN_model import CNN_model
import numpy as np
import RPi.GPIO as GPIO

new_model = CNN_model()
new_controll = controll()
front_sonar = sonar(17,18)
right_sonar = sonar(27, 23)
left_sonar = sonar(22, 24)
"""
print('front')
print(front_sonar.getReadings())
print('right')
print(right_sonar.getReadings())
print('left')
print(left_sonar.getReadings())
"""
try:
    while True:
        readings = [[front_sonar.getReadings(), right_sonar.getReadings(), left_sonar.getReadings()]]
        move = new_model.get_prediction(readings)
        print(readings)
        print(move)
        if move == 0:
            new_controll.front()
        elif move == 1:
            new_controll.left()
        elif move == 2:
            new_controll.rigth()
        else:
            reverse()
except KeyboardInterrupt:
    GPIO.cleanup()
    new_controll.clean_control()
    front_sonar.clean_sonar()
    right_sonar.clean_sonar()
    left_sonar.clean_sonar()
    
