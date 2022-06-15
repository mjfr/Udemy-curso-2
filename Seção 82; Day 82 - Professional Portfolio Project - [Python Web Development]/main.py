# TODO - 1: Make a website to show off my skills
# This is the second portfolio project from the course.

from flask import Flask, render_template, send_from_directory
from datetime import date

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./static/files/"


@app.route("/")
def home():
    year = date.today().year
    return render_template("index.html", year=year)


@app.route("/curriculum")
def cv_download():
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"], path="Blender-Keyboard-Shortcuts.pdf")


if __name__ == "__main__":
    app.run(debug=True)
