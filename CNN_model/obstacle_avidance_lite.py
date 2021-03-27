import numpy as np
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(input_details[0]['shape'])
print(output_details[0]['shape'])
print(input_details[0]['dtype'])

# replace it with reaadings of 3 sensors
feature_vector = np.array([[10, 25, 20]], dtype = np.int32)

interpreter.set_tensor(input_details[0]['index'], feature_vector)
interpreter.invoke()
tflite_model_predictions = interpreter.get_tensor(output_details[0]['index'])
print(tflite_model_predictions)
prediction_classes = np.argmax(tflite_model_predictions, axis=1)
print(prediction_classes)
