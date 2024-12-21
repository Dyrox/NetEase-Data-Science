import tensorflow as tf

# Load your TensorFlow model
model = tf.keras.models.load_model('relationship_prediction_model_dense')


def predict(value):
    prediction = model.predict([[value]])
    return prediction

print(predict(60000))