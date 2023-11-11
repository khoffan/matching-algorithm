from flask import Flask, jsonify, request
from user_matching import matching
import json


app = Flask(__name__)

@app.route("/api/matching", methods=['POST'])
def hello_world():
    data = request.get_json()

    if 'customers' not in data or 'riders' not in data:
            return jsonify({'error': 'Invalid request. "customers" and "riders" are required.'}), 400

    customers = data['customers']
    riders = data['riders']

    matched = matching(customers,riders)
    return jsonify({'matches': matched})


if __name__ in '__main__':
    app.run(debug=True)