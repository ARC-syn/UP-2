"""
from keras.applications.mobilenetv2 import MobileNetV2
from keras.layers import Input
import tensorflow_hub as hub
"""
import tensorflow as tf
import cv2
import numpy as np
from keras.applications.mobilenetv2 import preprocess_input

class img_classifier:
    def __init__(self):
        self.target_index = 9
        #self.camera = PiCamera()
        #self.rawCapture = PiRGBArray(self.camera)  #warmup camera
        #time.sleep(0.1)
        self.model = tf.keras.applications.MobileNetV2(include_top = True) #load pretrained model
        
    def classify_cam(self):
        #-------------------read image from camera---------------------
        #self.camera.capture(self.rawCapture, format="bgr")
        #image = self.rawCapture.array
        image = cv2.imread("test3.jpg", cv2.IMREAD_COLOR) #read image 
        
        #-------------------pre-process imagae---------------------------
        width = 224
        height = 224
        dim = (width, height)
        image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        image = preprocess_input(image)
        input_data = np.empty((1,224,224,3))
        input_data[0] = image
        
        #-------------------classify processed image-----------------------
        print(np.argmax(self.model.predict(input_data)))
        if np.argmax(self.model.predict(input_data)) == self.target_index:
            return 1
        else:
            return 0
            
        
cam = img_classifier()
cam.classify_cam()