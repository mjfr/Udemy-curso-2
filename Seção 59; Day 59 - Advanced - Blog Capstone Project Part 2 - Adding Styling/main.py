from flask import Flask, render_template, url_for, redirect
import requests

app = Flask(__name__)
BLOG_API_ENDPOINT = "https://api.npoint.io/e25f421f3e7a31651e40"


def api_content():
    return requests.get(BLOG_API_ENDPOINT)


@app.route("/")
def home():
    home_bg = url_for("static", filename="assets/img/home-bg.jpg")
    all_posts = api_content()
    title = "Upgraded Blog!"
    subtitle = "A Blog made using Python, Flask, Jinja and Bootstrap"
    return render_template("index.html", bg=home_bg, posts=all_posts.json(), title=title, subtitle=subtitle)


@app.route("/about")
def about():
    about_bg = url_for("static", filename="assets/img/about-bg.jpg")
    title = "About"
    subtitle = "Lorem ipsum dolor sit amet."
    return render_template("about.html", bg=about_bg, title=title, subtitle=subtitle)


@app.route("/contact")
def contact():
    contact_bg = url_for("static", filename="assets/img/contact-bg.jpg")
    title = "Contact Us!"
    subtitle = "Lorem ipsum dolor sit amet"
    return render_template("contact.html", bg=contact_bg, title=title, subtitle=subtitle)


@app.route("/post/<int:post_id>")
def full_post(post_id):
    all_posts = api_content()
    try:
        post = all_posts.json()[post_id-1]
    except IndexError:
        print(f"There is no #{post_id-1} id. Redirecting to home.")
    else:
        post_bg = post["bg_image"]
        title = post["title"]
        subtitle = post["subtitle"]
        return render_template("post.html", bg=post_bg, post=post, title=title, subtitle=subtitle)
    return redirect("/", code=301)


if __name__ == '__main__':
    app.run(debug=True)
