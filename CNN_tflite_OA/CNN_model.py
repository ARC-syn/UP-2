import numpy as np
import tflite_runtime.interpreter as tflite

class CNN_model:
    def __init__(self):
        pass
    
    def get_prediction(self, feature_vector):
        interpreter = tflite.Interpreter(model_path="model_int32.tflite")
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        # replace it with reaadings of 3 sensors
        interpreter.set_tensor(input_details[0]['index'], feature_vector)
        interpreter.invoke()
        tflite_model_predictions = interpreter.get_tensor(output_details[0]['index'])
        prediction_classes = np.argmax(tflite_model_predictions, axis=1)
        return prediction_classes