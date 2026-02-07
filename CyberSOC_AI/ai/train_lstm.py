import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

X = np.random.rand(200, 5, 1)
y = np.random.randint(0, 2, 200)

model = Sequential([
    LSTM(64, input_shape=(5, 1)),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy")
model.fit(X, y, epochs=5)

model.save("ai/lstm.h5")
print("LSTM trained")
