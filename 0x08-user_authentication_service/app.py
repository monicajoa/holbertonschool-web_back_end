#!/usr/bin/env python3
""" [Module that holds Basic Flask app]
"""

from flask import Flask, jsonify, abort, request, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Method log in, responds to the POST / sessions path,
        create a new session for the user, save the session id as a cookie,
        Return a JSON payload of the form
    """
    email_data = request.form.get("email")
    password_data = request.form.get("password")
    if not AUTH.valid_login(email_data, password_data):
        abort(401)
    else:
        session_id = AUTH.create_session(email_data)
        response = jsonify({"email": email_data, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ Method Log out, responds to the DELETE /sessions route,
        find for the user with the requested session ID
    """
    session_id = request.cookies.get("session_id")
    search_user = AUTH.get_user_from_session_id(session_id)
    if search_user:
        AUTH.destroy_session(search_user.id)
        return redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
