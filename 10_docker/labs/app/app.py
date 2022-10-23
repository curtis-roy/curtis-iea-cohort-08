#!/bin/env python3

"""Dockerized app"""

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():

    """Hello."""
    return os.environ.get('RESPONSE', "No response provided!") + "\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
