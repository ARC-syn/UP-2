# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:07:32 2021
@author: MrSan
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#from tensorflow.contrib import lite
from tensorflow.keras.layers.experimental import preprocessing

np.set_printoptions(suppress = True)
dataset = pd.read_csv("training_data.txt", names = ["frontsensor", "rigthsensor", "leftsensor", "move"])
dataset.head()
dataset_features = dataset.copy()
dataset_labels = dataset_features.pop('move')
dataset_features = np.array(dataset_features)
print(dataset_features)
print(dataset_labels)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, activation = tf.nn.relu),
    tf.keras.layers.Dense(3, activation = tf.nn.softmax),
    tf.keras.layers.Dense(4, activation = 'relu')                                               
])

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy')
model.fit(dataset_features, dataset_labels, epochs = 50)

feature_vector = np.array([[20, 25, 20]], dtype = int)
output = model.predict(feature_vector)
print(output)
print(np.argmax(output, axis=1))
print(type(output))
model.summary()

###write out the keras file
#keras_file = "linear.h5"
#keras.models.save_model(model, keras_file)

#saved_model_dir = "C:/Users/MrSan/Desktop/CNN_model/linear.h5"


#converter = tf.lite.TFLiteConverter.from_keras_model(model) # path to the SavedModel directory
#tflite_model = converter.convert()

# Save the model.
#with open('model.tflite', 'wb') as f:
#  f.write(tflite_model)
###convert the keras file to tf-lite
#converter = lite.TocoConverter.from_keras_model_file(keras_file)
#open("linear.tflite", "wb").write(tflite_model)

