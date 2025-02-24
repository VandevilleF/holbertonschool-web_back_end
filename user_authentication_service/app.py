#!/usr/bin/env python3
"""Setup basic Flask
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """Display a welcome message
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
