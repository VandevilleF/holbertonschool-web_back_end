#!/usr/bin/env python3
"""Setup basic Flask
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """Display a welcome message
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Registre a user
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or not pwd:
        return jsonify({"message": "email and password are required"}), 400

    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
