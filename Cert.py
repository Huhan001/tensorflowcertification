import tensorflow as tf
import numpy as np
import pandas as pd
import logging

#--------------------------------------------- installing all packages

#logger = tf.get_logger()
#logger.setLevel(logging.ERROR)

#..............................................this is to identify the error.
#celsius_q = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
#fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

#for i,c in enumerate(celsius_q):
#    print("{} this is the centigrade, while {} this is the fahrenheit".format(c, fahrenheit_a[i]))

#___________________________________________________________________  begin
#l0 = tf.keras.layers.Dense(units=1, input_shape= [1]) # defines the layer

#model = tf.keras.Sequential([l0])
#model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(0.1))

#history = model.fit(celsius_q, fahrenheit_a, epochs=700, verbose=False)
#print("Finished training the model")

#import matplotlib.pyplot as plt
#plt.xlabel('Epoch Number')
#plt.ylabel("Loss Magnitude")
#plt.plot(history.history['loss'])
#plt.show()
#----------------------------------------------------------------- So far learnt a few steps however the udacity tutorial isnt off to a good start.

