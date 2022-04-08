import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
blog_response.raise_for_status()
all_posts = blog_response.json()

posts_list = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in all_posts]


@app.route('/')
def home():
    return render_template("index.html", posts=posts_list)


@app.route("/post/<int:post_id>")
def post(post_id):
    requested_post = [post for post in posts_list if post.id == post_id][0]
    return render_template("post.html", requested_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
