import wtforms.validators
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False, unique=True)
    img_url = db.Column(db.String(250), nullable=False, unique=True)


# db.create_all()
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's"
#                 "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a"
#                 "jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


class EditMovieForm(FlaskForm):
    rating = FloatField(label="Your rating out of 10:", render_kw={"placeholder": "e.g.: 7.5"}, validators=[
        wtforms.validators.NumberRange(max=10, message="Use only numbers ranging from 0 to 10.")
    ])
    review = StringField(label="Your review:", validators=[DataRequired()])
    submit = SubmitField(label="Update changes")


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie = Movie.query.get(request.args["movie_id"])
    form = EditMovieForm()
    if form.validate_on_submit():
        movie.rating = request.form.get("rating")
        movie.review = request.form.get("review")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


if __name__ == '__main__':
    app.run(debug=True)
