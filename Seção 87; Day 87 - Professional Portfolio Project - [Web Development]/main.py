# TODO-1: Build a website that lists cafes with wifi and power for remote working.
import os
import wtforms.validators
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, TimeField, SelectField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Columns(db.Integer, primary_key=True)
    name = db.Columns(db.string(100), unique=True, nullable=False)
    map_url = db.Columns(db.string(300), unique=True, nullable=False)
    img_url = db.Columns(db.string(300), unique=True, nullable=False)
    location = db.Columns(db.string(250), unique=True, nullable=False)
    seats = db.Columns(db.Integer, nullable=False)
    has_toilet = db.Columns(db.Integer, nullable=False)
    has_wifi = db.Columns(db.Integer, nullable=False)
    has_sockets = db.Columns(db.Integer, nullable=False)
    coffee_price = db.Columns(db.string(10), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class CafeForm(FlaskForm):
    name = StringField(label="Cafe Name", validators=[DataRequired()])
    map_url = URLField(label="Google Maps URL", validators=[DataRequired(),
                                                            wtforms.validators.URL(message="Use a valid URL.")])
    img_url = URLField(label="Cafe's Image URL", validators=[DataRequired(),
                                                             wtforms.validators.URL(message="Use a valid URL.")])
    location = StringField(label="Cafe's Location", validators=[DataRequired()])
    seats = IntegerField(label="Number of Seats", validators=[DataRequired()])
    has_toilet = BooleanField(label="Has Toilet?", validators=[DataRequired()])
    has_wifi = BooleanField(label="Has WiFi?", validators=[DataRequired()])
    has_sockets = BooleanField(label="Has Power Socket?", validators=[DataRequired()])
    coffee_price = FloatField(label="Coffee Price", validators=[DataRequired()])
    submit = SubmitField(label="Submit Cafe!")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def get_all():
    cafes = Cafe.query.all()
    cafes_dict = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafe=cafes_dict), 200


@app.route("/search")
def search():
    cafes = Cafe.query.filter_by(location=request.args.get("location"))
    cafes_dict = [cafe.to_dict() for cafe in cafes]
    if len(cafes_dict) == 0:
        return jsonify(response={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return jsonify(cafes_dict), 200


@app.route("/random")
def get_random():
    cafe = choice(Cafe.query.all())
    return jsonify(cafe=cafe.to_dict()), 200


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = Cafe()
        cafe.name = request.form.get("name")
        cafe.map_url = request.form.get("map_url")
        cafe.img_url = request.form.get("img_url")
        cafe.location = request.form.get("location")
        cafe.seats = request.form.get("seats")
        cafe.has_toilet = request.form.get("has_toilet")
        cafe.has_wifi = request.form.get("has_wifi")
        cafe.has_sockets = request.form.get("has_sockets")
        cafe.coffee_price = request.form.get("coffee_price")
        if Cafe.query.filter_by(name=cafe.name).first() is None:
            db.session.add(cafe)
            db.session.commit()
            return jsonify(response={"Ok": "Successfully added the new Cafe."}), 200
        return jsonify(response={"Conflict": "The cafe you're trying to add already exists in the database."}), 409


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    edit_form = CafeForm(
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,
        seats=cafe.seats,
        has_toilet=cafe.has_toilet,
        has_wifi=cafe.has_wifi,
        has_sockets=cafe.has_sockets,
        coffee_price=cafe.coffee_price
    )
    if edit_form.validate_on_submit():
        cafe.name = edit_form.name.data
        cafe.map_url = edit_form.map_url.data
        cafe.img_url = edit_form.img_url.data
        cafe.location = edit_form.location.data
        cafe.seats = edit_form.seats.data
        cafe.has_toilet = edit_form.has_toilet.data
        cafe.has_wifi = edit_form.has_wifi.data
        cafe.has_sockets = edit_form.has_sockets.data
        cafe.coffee_price = edit_form.coffee_price.data
        db.session.commit()
    # name = request.form.get("new_name")
    # map_url = request.form.get("new_map_url")
    # img_url = request.form.get("new_img_url")
    # location = request.form.get("new_location")
    # seats = request.form.get("new_seats")
    # has_toilet = request.form.get("new_has_toilet")
    # has_wifi = request.form.get("new_has_wifi")
    # has_sockets = request.form.get("new_has_sockets")
    # coffee_price = request.form.get("new_coffee_price")
    # if cafe is not None:
    #     cafe.name = name
    #     cafe.map_url = map_url
    #     cafe.img_url = img_url
    #     cafe.location = location
    #     cafe.seats = seats
    #     cafe.has_toilet = has_toilet
    #     cafe.has_wifi = has_wifi
    #     cafe.has_sockets = has_sockets
    #     cafe.coffee_price = coffee_price
    #     db.session.commit()
        return jsonify(response={"Ok": "Successfully updated the cafe's data."}), 200, redirect(url_for("get_all"))
    return jsonify(response={"Not Found": "The cafe's id was not found. Try using a valid id number."})


@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.filter_by(id=cafe_id).first()
    if cafe_to_delete is not None:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"Ok": "Successfully deleted the cafe."}), 200, redirect(url_for("home"))
    return jsonify(response={"Not Found": "The cafe id was not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
