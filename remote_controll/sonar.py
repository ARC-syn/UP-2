import RPi.GPIO as GPIO
import time

class sonar():
    def __init__(self, trig, echo):
        GPIO.setmode(GPIO.BCM)
        self.trig = trig
        self.echo = echo
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
    
    def getReadings(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        StartTime = time.time()
        StopTime = time.time()
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
            
        TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        return distance
        
        
    