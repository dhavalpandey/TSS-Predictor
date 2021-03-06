import tensorflow as tf
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Data
scores = list(map(int, input("Enter your current TSS: ").split()))

input_grades = scores[:-1]
output_grades = scores[1:]

scores_prev = np.array(input_grades,  dtype=float)
scores_now = np.array(output_grades,  dtype=float)

# Model Layers
l0 = tf.keras.layers.Dense(units=50, input_shape=[1])
l1 = tf.keras.layers.Dense(units=50)
l2 = tf.keras.layers.Dense(units=50)

# Model
model = tf.keras.Sequential([l0, l1, l2])
model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(1))

history = model.fit(scores_prev, scores_now, epochs=500, verbose=False)
print("Finished training the model.")


def predict_next_score(current_score):
    if round(model.predict([current_score])[0][0]) > 100:
        num = 100
    else:
        num = round(model.predict([current_score])[0][0])
    print(num)


predict_next_score(scores[-1])
