import RPi.GPIO as GPIO
import time

class controll:
    def __init__(self):
        self.In1 = 5
        self.In2 = 6
        self.In3 = 26
        self.In4 = 16
        self.enA = 12
        self.enB = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        GPIO.setup(self.In3, GPIO.OUT)
        GPIO.setup(self.In4, GPIO.OUT)
        GPIO.setup(self.enA, GPIO.OUT)
        GPIO.setup(self.enB, GPIO.OUT)
        """
        p=GPIO.PWM(self.enA,1000)
        p.start(25)
        q=GPIO.PWM(self.enB, 1000)
        q.start(25)
    """
        GPIO.output(self.enA, True)
        GPIO.output(self.enB, True)
        
    def front(self):
        GPIO.output(self.In1, False)
        GPIO.output(self.In2, True)
        GPIO.output(self.In3, True)
        GPIO.output(self.In4, False)
        
    def right(self):
        GPIO.output(self.In1, False)
        GPIO.output(self.In2, True)
        GPIO.output(self.In3, False)
        GPIO.output(self.In4, False)
        
    def left(self):
        GPIO.output(self.In1, False)
        GPIO.output(self.In2, False)
        GPIO.output(self.In3, True)
        GPIO.output(self.In4, False)
        
    def reverse(self):
        GPIO.output(self.In1, False)
        GPIO.output(self.In2, False)
        GPIO.output(self.In3, False)
        GPIO.output(self.In4, False)
        
    def working(self):
        GPIO.output(self.In1, False)
        GPIO.output(self.In2, True)
        GPIO.output(self.In3, False)
        GPIO.output(self.In4, True)
        time.sleep(10)
        
    def clean_control(self):
        GPIO.output(self.enA, False)
        GPIO.output(self.enB, False)
        GPIO.output(self.In1, False)
        GPIO.output(self.In2, False)
        GPIO.output(self.In3, False)
        GPIO.output(self.In4, False)
        GPIO.cleanup()
        
"""  
new_control = controll()
new_control.front()
time.sleep(4)
GPIO.cleanup()
#new_control.clean()
"""