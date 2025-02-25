#!/usr/bin/env python3
"""Setup basic Flask
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def welcome():
    """Display a welcome message
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ POST /users/
    JSON body:
      - email
      - password
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or not pwd:
        return jsonify({"message": "email and password are required"}), 400

    try:
        user = AUTH.register_user(email, pwd)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ POST /sessions/
    JSON body:
      - email
      - password
    Returns:
      - User object JSON represented
      - abort with 401 status
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or not pwd:
        abort(401)

    if not AUTH.valid_login(email, pwd):
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    print(session_id)

    return response


@app.route('/sessions', methods=["DELETE"], strict_slashes=False)
def logout() -> None:
    """ DELETE /sessions/
    JSON body:
      - session_id
    Returns:
      - redirect the user to GET /
      - If the user does not exist, 403 status
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
