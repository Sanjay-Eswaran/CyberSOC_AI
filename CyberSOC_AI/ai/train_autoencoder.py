import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Loading dataset...")
df = pd.read_csv("data/traffic.csv")

# Drop label column (autoencoder is unsupervised)
if "Label" in df.columns:
    df = df.drop(columns=["Label"])

print("Total columns used:", df.shape[1])

# Keep only numeric columns (extra safety)
df = df.select_dtypes(include=[np.number])

# Handle missing / infinite values
df = df.replace([np.inf, -np.inf], np.nan)
df = df.fillna(0)

# Normalize
scaler = MinMaxScaler()
X = scaler.fit_transform(df)

print("Training data shape:", X.shape)

# Autoencoder model
model = Sequential([
    Dense(64, activation="relu", input_shape=(X.shape[1],)),
    Dense(32, activation="relu"),
    Dense(64, activation="relu"),
    Dense(X.shape[1])
])

model.compile(optimizer="adam", loss="mse")

model.fit(
    X, X,
    epochs=10,
    batch_size=64,
    shuffle=True
)

model.save("ai/autoencoder.h5")
print("✅ Autoencoder training completed and model saved")
