import json
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
import tensorflowjs as tfjs
import tensorflow as tf

tf.compat.v1.disable_eager_execution() # got an error related to tensorflow v2.0, so I needed to disable eager execution for it to work

with open('trainingData.json') as f:
    data = json.load(f)
    xs = np.array(data['xs'])
    ys = np.array(data['ys'])


# splitting data into training and test data
x_train = xs[:-10000]
y_train = ys[:-10000]
x_test = xs[-10000:]
y_test = ys[-10000:]


# this part is kinda an art - designing the neutral network
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=6))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))



adam = keras.optimizers.Adam(lr=0.001)

model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=10,
          batch_size=128)

          
score = model.evaluate(x_test, y_test, batch_size=128)
print(score)
model.save("Keras-64x2-10epoch")


tfjs.converters.save_keras_model(model, "tfjsmodel")