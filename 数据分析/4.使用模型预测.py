import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Load the data from CSV
data = pd.read_csv('数据分析/training_data_csv.csv')

# Prepare the data
X = data['playlist_contributing_factors'].values.reshape(-1, 1)
y = data['estimated_play_count'].values

# Generate a range of values for prediction
min_value = X.min()
max_value = 100000
step = 10
X_range = np.arange(min_value, max_value, step).reshape(-1, 1)

# Load your TensorFlow model
model = tf.keras.models.load_model('relationship_prediction_model_dense')

# Make predictions on the range of values
y_pred_range = model.predict(X_range)

# Plot the original data
plt.scatter(X, y, color='blue', label='Original Data')

# Plot the predicted data on the range of values
plt.plot(X_range, y_pred_range, color='red', label='Predicted Data')

# Set plot labels, title, and legend
plt.xlabel('Playlist Contributing Factors')
plt.ylabel('Estimated Play Count')
plt.title('Custom TensorFlow Model (relationship_prediction_model_dense)')
plt.legend()

# Show the plot
plt.show()
