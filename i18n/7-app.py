#!/usr/bin/env python3
""" App module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config():
    """ Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """ Before request
    """
    g.user = get_user()


def get_user():
    """ Find user
    """
    user_id = request.args.get('login_as')
    if user_id is not None and user_id.isdigit():
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]

    return None


def get_locale():
    """ Get the local timezone
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    user = get_user()
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """ Get timezone
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            return
    user = get_user()
    if user and user.get('timezone'):
        try:
            return pytz.timezone(user['timezone']).zone
        except UnknownTimeZoneError:
            return

    return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/', strict_slashes=False)
def welcome():
    """ return index
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)
