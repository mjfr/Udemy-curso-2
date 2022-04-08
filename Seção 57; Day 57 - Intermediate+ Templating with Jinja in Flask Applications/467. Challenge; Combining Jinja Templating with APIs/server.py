from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess", methods=["GET", "POST"])
def guess_name():
    name = request.form.get('name').title()
    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    genderize_response.raise_for_status()
    gender = genderize_response.json()["gender"]
    agify_response = requests.get(f"https://api.agify.io?name={name}")
    agify_response.raise_for_status()
    age = agify_response.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
