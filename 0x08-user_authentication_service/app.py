#!/usr/bin/env python3
""" [Module that holds Basic Flask app]
"""

from flask import Flask, jsonify, request, abort, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def basic_flask_app(): -> str:
    """ Method Basic Flask app, that create and set up
        a basic Flask app, Return a JSON payload.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
