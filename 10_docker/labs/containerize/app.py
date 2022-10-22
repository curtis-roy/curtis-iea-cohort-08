#!/bin/env python3

"""Test flask app for docker lab.  Cleaned up for PEP8 specs."""

import os
from flask import Flask, redirect, request, url_for

signatures = []

app = Flask(__name__)

font = os.environ["DISPLAY_FONT"] = "arial"
font_color = os.environ["DISPLAY_COLOR"] = "red"
environment = os.environ["ENVIRONMENT"] = "MARVIN"


@app.route("/", methods=["GET"])
def index():
    """Generates simple Flask web guestbook"""
    html = """
    Signatures: <br />
    <font face="%(font)s" color="%(color)s">
        %(messages)s
    </font><br /> <br />
    <form action="/signatures" method="post">
        Sign the Guestbook: <input type="text" name="message"><br>
        <input type="submit" value="Sign">
    </form>

    <br />
    <br />
    Debug Info: <br />
    ENVIRONMENT is %(environment)s
    """
    messages_html = "<br />".join(signatures)
    return html % {
        "font": font,
        "color": font_color,
        "messages": messages_html,
        "environment": environment,
    }


@app.route("/signatures", methods=["POST"])
def write():
    """Output"""
    message = request.form.get("message")
    signatures.append(message)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
