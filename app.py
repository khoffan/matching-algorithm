from flask import Flask, jsonify, request
from flask_cors import CORS
from user_matching import matching
import json

from components.getRiders import riders_sort

app = Flask(__name__)
CORS(app)
sort_rider = riders_sort()


@app.route("/", methods=["GET"])
def welcome_my_api():
    return "Welcome to my API!"


@app.route("/api/matching", methods=["POST"])
def matchingAPI():
    try:
        data = request.get_json()

        if "customers" not in data:
            return (
                jsonify(
                    {
                        "error": 'Invalid request. "customers" must be a list of customer data.'
                    }
                ),
                400,
            )

        customers = data["customers"]

        # Add more input validation if needed

        matched = matching(customers)
        return jsonify({"matches": matched})

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route("/api/riderlist", methods=["GET"])
def getRider():
    try:
        data = sort_rider
        if not data:
            return (
                jsonify(
                    {"error": 'Invalid request. "riders" must be a list of rider data.'}
                ),
                400,
            )
        riders = data
        return jsonify({"riders": riders})
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route("/api/riderid/<string:id_>", methods=["GET"])
def getRiderId(id_):
    try:
        data = sort_rider
        if not data:
            return (
                jsonify(
                    {"error": 'Invalid request. "riders" must be a list of rider data.'}
                ),
                400,
            )
        rider = next((r for r in data if r["id"] == id_), None)
        if not rider:
            return (
                jsonify(
                    {
                        "error": 'Invalid request. "rider id:{id_}" must be a list of rider data.'
                    }
                ),
                400,
            )
        return jsonify({"riders": rider})
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route("/api/riderlocate/<string:locate>", methods=["GET"])
def getRiderlLocate(locate):
    try:
        data = sort_rider
        rider = []
        if not data:
            return (
                jsonify(
                    {"error": 'Invalid request. "riders" must be a list of rider data.'}
                ),
                400,
            )
        for r in data:
            if r['location'] == locate:
                rider.append(r)
            
        if not rider:
            return (
                jsonify(
                    {
                        "error": f'Invalid request. "rider location: {locate}" must be a list of rider data.'
                    }
                ),
                400,
            )
        return jsonify({"riders": rider})
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5001)

