const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, 'training_data_csv.csv');
const dataset = [];

fs.createReadStream(dataPath)
  .pipe(csv())
  .on('data', (row) => {
    // Extract the relevant columns and convert them to numeric values
    const factor = parseFloat(row.playlist_contributing_factors);
    const count = parseFloat(row.estimated_play_count);

    // Add the data to the dataset
    dataset.push({ factor, count });
  })
  .on('end', () => {
    // Prepare the data
    const X = dataset.map((data) => data.factor);
    const y = dataset.map((data) => data.count);

    // Define the model architecture
    const model = tf.sequential();
    model.add(tf.layers.dense({ units: 64, activation: 'relu', inputShape: [1] }));
    model.add(tf.layers.dense({ units: 1 }));

    // Compile the model
    model.compile({ optimizer: 'adam', loss: 'meanSquaredError' });

    // Convert the data to TensorFlow tensors
    const xTensor = tf.tensor2d(X, [X.length, 1]);
    const yTensor = tf.tensor2d(y, [y.length, 1]);

    // Train the model
    model.fit(xTensor, yTensor, { epochs: 50 })
      .then(() => {
        // Save the trained model
        const savePath = path.join(__dirname, 'TFJSmodel');
        model.save('file://${savePath}')
          .then(() => console.log('Model saved successfully.'))
          .catch((error) => console.error('Error saving model:', error));
      })
      .catch((error) => console.error('Error training model:', error));
  });
