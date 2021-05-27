#!/usr/bin/env python3
""" [Module that holds Basic Flask app]
"""

from flask import Flask, jsonify, abort, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def basic_flask_app() -> str:
    """ Method Basic Flask app, that create and set up
        a basic Flask app, Return a JSON payload.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Method Register user, Define a users function that implements
        the POST /users route, Return a 400 status code
    """
    email_data = request.form.get('email')
    password_data = request.form.get('password')
    try:
        AUTH.register_user(email_data, password_data)
        return jsonify({"email": email_data, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
