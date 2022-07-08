# TODO-1: Build a website that lists cafes with wifi and power for remote working.
import os
import wtforms.validators
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, TimeField, SelectField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    map_url = db.Column(db.String(400), unique=True, nullable=False)
    img_url = db.Column(db.String(400), unique=True, nullable=False)
    location = db.Column(db.String(250), unique=True, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# db.create_all()


class CafeForm(FlaskForm):
    name = StringField(label="Nome do Café", validators=[DataRequired()])
    map_url = URLField(label="URL do Google Maps", validators=[DataRequired(),
                                                               wtforms.validators.URL(message="Use a valid URL.")])
    img_url = URLField(label="URL de uma Foto do Café", validators=[DataRequired(),
                                                                    wtforms.validators.URL(message="Use a valid URL.")])
    location = StringField(label="Endereço do Café", validators=[DataRequired()])
    seats = IntegerField(label="Número de Acentos", validators=[DataRequired()])
    has_toilet = BooleanField(label="Tem Banheiro?")
    has_wifi = BooleanField(label="Tem WiFi?")
    has_sockets = BooleanField(label="Tem Tomadas?")
    coffee_price = FloatField(label="Preço do Café", validators=[DataRequired()])
    submit = SubmitField(label="Registrar Café!")


@app.route("/")
def home():
    return render_template("index.html")


def get_all():
    cafes = Cafe.query.all()
    return [cafe.to_dict() for cafe in cafes]


@app.route("/api/all")
def get_all_json():
    cafes_dict = get_all()
    return jsonify(cafe=cafes_dict), 200


@app.route("/web/all")
def get_all_html():
    cafes_dict = get_all()
    print(cafes_dict)
    return render_template("cafes.html", cafes=cafes_dict)


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


@app.route("/api/add", methods=["POST"])
def add_cafe_api():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = Cafe()
        cafe.name = request.args.get("name")
        cafe.map_url = request.args.get("map_url")
        cafe.img_url = request.args.get("img_url")
        cafe.location = request.args.get("location")
        cafe.seats = request.args.get("seats")
        cafe.has_toilet = request.args.get("has_toilet")
        cafe.has_wifi = request.args.get("has_wifi")
        cafe.has_sockets = request.args.get("has_sockets")
        cafe.coffee_price = request.args.get("coffee_price")
        if Cafe.query.filter_by(name=cafe.name).first() is None:
            db.session.add(cafe)
            db.session.commit()
            return jsonify(response={"Ok": "Successfully added the new Cafe."}), 200
        return jsonify(response={"Conflict": "The cafe you're trying to add already exists in the database."}), 409


@app.route("/web/add", methods=["GET", "POST"])
def add_cafe_html():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = Cafe()
        cafe.name = request.form.get("name")
        cafe.map_url = request.form.get("map_url")
        cafe.img_url = request.form.get("img_url")
        cafe.location = request.form.get("location")
        cafe.seats = request.form.get("seats")
        cafe.has_toilet = bool(request.form.get("has_toilet"))
        cafe.has_wifi = bool(request.form.get("has_wifi"))
        cafe.has_sockets = bool(request.form.get("has_sockets"))
        cafe.coffee_price = request.form.get("coffee_price")
        if Cafe.query.filter_by(name=cafe.name).first() is None:
            db.session.add(cafe)
            db.session.commit()
            return redirect(url_for("get_all_html"))
    return render_template("add_cafe.html", form=form)


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
