#!/usr/bin/python3
"""
A script that starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """
    Display 'C' followed by the value of the text variable.

    Args:
        text (str): The value passed in the URL.

    Returns:
        str: The string 'C'  value of the text variable.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """
    Display 'Python' followed by the value of the text variable.

    Args:
        text (str, optional): The value passed;defaults to "is cool".

    Returns:
        str: ue of the text variable.
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
