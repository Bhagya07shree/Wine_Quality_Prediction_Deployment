from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model
with open('wine_quality_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Wine Quality Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.json
        features = np.array(data['features']).reshape(1, -1)  # Convert to numpy array

        # Make prediction
        prediction = model.predict(features)[0]

        return jsonify({'wine_quality': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
