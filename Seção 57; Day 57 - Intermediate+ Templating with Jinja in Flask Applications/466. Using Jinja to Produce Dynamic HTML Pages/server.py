from flask import Flask, render_template
import random
from datetime import date
# Jinja is a templating language for Python

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    builder_name = "Matheus José"
    # **context here acts like a **kwargs which will need a name and a value. The name is what we will use to recover
    # inside the HTML file
    return render_template("index.html", num=random_number, curr_year=current_year, b_name=builder_name)


if __name__ == '__main__':
    app.run(debug=True)
