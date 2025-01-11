from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        # Example: Simulating prediction logic
        feature1 = data.get('feature1', 0)
        feature2 = data.get('feature2', 0)
        feature3 = data.get('feature3', 0)

        # Basic logic, replace with your prediction logic
        result = feature1 + feature2 + feature3

        # Return prediction result as JSON
        return jsonify({'prediction': result})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port to 5001
