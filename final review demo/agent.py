from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from custom_einvironment import TestEnv
from tensorflow.keras.layers import Dense, Flatten
import tensorflow as tf
import keras
#tf.compat.v1.enable_eager_execution()

#initialize environment
env = TestEnv()
states = env.observation_space.shape
actions = env.action_space.n
print(states)
print(actions)
print(env.observation_space.sample())

#fully connected network
def build_model(states, actions):
    model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(1,8)),
    tf.keras.layers.Dense(8, activation = tf.nn.relu),
    tf.keras.layers.Dense(8, activation = tf.nn.softmax),
    tf.keras.layers.Dense(actions, activation = 'relu')                                               
    ])
    return model

#initialize nural network
model = build_model(states, actions)
model.summary()

#initialize rl policy map
def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions, 
                   nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

#train model
dqn = build_agent(model, actions)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])
dqn.fit(env, nb_steps=100, visualize=False, verbose=1)

#save model as pb
#model.save('C:/Users/MrSan/Desktop/reinforcement_learning/models')

"""--------------------------tflite conversion---------------------------------
# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.invoke()
# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)

print('type of model')
#print(type(model))
print(type(interpreter))
# Convert the model.
#converter = tf.lite.TFLiteConverter.from_keras_model(model)
#tflite_model = converter.convert()
# Save the model.
#with open('model.tflite', 'wb') as f:
#  f.write(tflite_model)
----------------------------------------------------------------------------"""