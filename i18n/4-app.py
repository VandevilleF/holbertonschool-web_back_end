#!/usr/bin/env python3
""" App module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config():
    """ Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """ Get the local timezone
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def welcome():
    """ return index
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)
