# TODO - 1: Make a website to show off my skills
# This is the second portfolio project from the course.

from flask import Flask, render_template, redirect, url_for, request
from datetime import date

app = Flask(__name__)


@app.route("/")
def home():
    year = date.today().year
    return render_template("index.html", year=year)


if __name__ == "__main__":
    app.run(debug=True)
