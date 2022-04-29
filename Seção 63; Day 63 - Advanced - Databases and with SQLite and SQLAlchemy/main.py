from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form_dict = {key: value for key, value in request.form.items()}
    if form_dict != {} and form_dict.get("title") != "" and form_dict.get("author") != ""\
            and form_dict.get("rating") != "":
        # all_books.append(form_dict)
        # print(all_books)
        book = Book(title=form_dict["title"], author=form_dict["author"], rating=form_dict["rating"])
        print(book.title)
        print(book.author)
        print(book.rating)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_to_update = Book.query.get(request.args["book_id"])
    if request.form.get("rating") is not None and request.form.get("rating") != "":
        book_to_update.rating = request.form.get("rating")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book_to_update)


@app.route("/delete")
def delete():
    book_to_delete = Book.query.get(request.args["book_id"])
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
