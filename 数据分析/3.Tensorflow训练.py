import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
data = pd.read_csv('数据分析/training_data_csv.csv')

# Prepare the data
X = data['playlist_contributing_factors'].values
y = data['estimated_play_count'].values

# Define the model architecture
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[1]),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=50)

# Save the trained model
model.save('relationship_prediction_model')

