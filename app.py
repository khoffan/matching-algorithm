from flask import Flask, jsonify, request
from flask_cors import CORS
from user_matching import matching
import json


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def welcome_my_api():
    return "Welcome to my API!"
@app.route("/api/matching", methods=['POST'])
def matchingAPI():
    try:
        data = request.get_json()

        if 'customers' not in data :
            return jsonify({'error': 'Invalid request. "customers" must be a list of customer data.'}), 400

        customers = data['customers']

        # Add more input validation if needed

        matched = matching(customers)
        return jsonify({'matches': matched})

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


if __name__ in '__main__':
    app.run(host="0.0.0.0", port=5001)
