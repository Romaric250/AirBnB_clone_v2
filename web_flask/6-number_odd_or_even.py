#!/usr/bin/python3
"""Flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Return a given string.

    Returns:
        str: The string "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return a given string.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
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
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Display 'Python' followed by the value of the text variable.

    Args:
        text (str, optional): The value passed in the URL. Defaults to "is cool".

    Returns:
        str: The string 'Python' concatenated with the value of the text variable.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """
    Display an HTML page only if n is an integer.

    Args:
        n (int, optional): The value passed in the URL. Defaults to None.

    Returns:
        str: The rendered HTML page if n is an integer.
    """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """
    Display an HTML page only if n is an integer.

    The HTML page contains an H1 tag with the text "Number: n is even|odd"
    inside the <body> tag.

    Args:
        n (int, optional): The value passed in the URL. Defaults to None.

    Returns:
        str: The rendered HTML page if n is an integer.
    """
    if isinstance(n, int):
        eo = "odd" if n % 2 else "even"
        return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run()
