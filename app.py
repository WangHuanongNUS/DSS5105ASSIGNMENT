# app.py

from flask import Flask, request, jsonify
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained regression model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the /predict endpoint
@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Get input parameters W and X
        W = float(request.args.get('W'))
        X = float(request.args.get('X'))

        # Prepare features (include constant term)
        features = np.array([[1, W, X]])

        # Make prediction
        prediction = model.predict(features)[0]

        return jsonify({
            'predicted_engagement_score': prediction
        })
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
