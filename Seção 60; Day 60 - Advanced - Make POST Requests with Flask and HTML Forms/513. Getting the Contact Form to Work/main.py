import os

from flask import Flask, render_template, url_for, redirect, request
import requests
import smtplib

app = Flask(__name__)
BLOG_API_ENDPOINT = "https://api.npoint.io/e25f421f3e7a31651e40"
EMAIL_SITE = os.environ["EMAIL"]
EMAIL_PASSWORD = os.environ["PASSWORD"]
HOST = "smtp-mail.outlook.com"


def email_sender(name, email, phone, message):
    with smtplib.SMTP(host=HOST) as connection:
        connection.starttls()
        connection.login(user=EMAIL_SITE, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_SITE, to_addrs=EMAIL_SITE, msg=f"Subject:Contact me! [BLOG]\n\nName: {name}"
                                                                           f"\nEmail: {email}\nPhone: {phone}"
                                                                           f"\nMessage: {message}")


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


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_bg = url_for("static", filename="assets/img/contact-bg.jpg")
    if request.method == "GET":
        title = "Contact Us!"
        subtitle = "Lorem ipsum dolor sit amet"
        return render_template("contact.html", bg=contact_bg, title=title, subtitle=subtitle)
    title = "Success"
    subtitle = "Your message was sent!"
    contact_data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "message": request.form.get("message")
    }
    email_sender(contact_data["name"], contact_data["email"], contact_data["phone"], contact_data["message"])
    return render_template("form-entry.html", bg=contact_bg, title=title, subtitle=subtitle)


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
