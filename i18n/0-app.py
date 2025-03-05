#!/usr/bin/env python3
""" App module
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    render_template("templates/0-index.html")
