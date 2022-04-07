from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


@app.route("/")
def hello_world():
    return "<h1 style=\"text-align: center\">Hello, world!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src=\"https://i.kym-cdn.com/entries/icons/original/000/026/152/gigachad.jpg\" width=200px>" \
           "<img src=\"https://c.tenor.com/epNMHGvRyHcAAAAd/gigachad-chad.gif\" width=200px, height=112.531px>"


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"


# Using "<" ">" like <something>, will make flask know that a variable value should be placed between <>
# To extract a path from an url, we write it like: <path:something>, <int:something> etc
# @app.route("/username/<name>")
@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello {name}! You are {number} years old.<br>Welcome friend!!!"


if __name__ == '__main__':
    app.run(debug=True)  # Using debug mode to update things in code without needing to stop and start the server again
    # Just by pressing Control + S we can reload the server so our changes in the code will load.
