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


@app.route("/blog/<num>")
def get_blog(num):
    # This num came from the index.html a tag, where we passed get_blog function as a string to the url_for function
    # passing as well the num as an attribute
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_response.raise_for_status()
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
