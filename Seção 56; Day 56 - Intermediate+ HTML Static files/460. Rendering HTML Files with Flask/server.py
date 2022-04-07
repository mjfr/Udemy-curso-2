from flask import Flask, render_template
# All HTML templates must be inside a "templates" folder
# Static files like images or css, they must be inside "static" folder

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
