#!/usr/bin/python3
"""
A script that starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """
    Return a given string.

    Returns:
        str: The string "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Return a given string.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Display 'C' followed by the value of the text variable.

    Args:
        text (str): The value passed in the URL.

    Returns:
        str: The string 'C' concatenated with the value of the text variable.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    Display 'Python' followed by the value of the text variable.

    Args:
        text (str, optional): The value passed in the URL.
            Defaults to "is cool".

    Returns:
        str: The string 'Python' concatenated with the valu
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    Display 'n is a number' only if n is an integer.

    Args:
        n (int): The value passed in the URL.

    Returns:
        str: The string 'n is a number' if n is an integer.
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
