from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route("/random")
def get_random():
    cafes = Cafe.query.all()
    cafe = choice(cafes)
    return jsonify(cafe=cafe.to_dict()), 200
    # A way to convert a dictionary to json using jsonify and above in the "Cafe" class, is another way
    # return jsonify(cafe={
    #     "id": cafe.id,
    #     "name": cafe.name,
    #     "map_url": cafe.map_url,
    #     "image": cafe.img_url,
    #     "location": cafe.location,
    #     "has_sockets": cafe.has_sockets,
    #     "has_toilet": cafe.has_toilet,
    #     "has_wifi": cafe.has_wifi,
    #     "can_take_calls": cafe.can_take_calls,
    #     "seats": cafe.seats,
    #     "coffee_price": cafe.coffee_price
    # })


@app.route("/all")
def get_all():
    cafes = Cafe.query.all()
    cafes_dict = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafe=cafes_dict), 200


@app.route("/search")
def search():
    cafes = Cafe.query.filter_by(location=request.args.get("loc"))
    cafes_dict = [cafe.to_dict() for cafe in cafes]
    if len(cafes_dict) == 0:
        return jsonify(response={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return jsonify(cafes_dict), 200


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add():
    cafe = Cafe()
    cafe.name = request.form.get("name")
    cafe.map_url = request.form.get("map_url")
    cafe.img_url = request.form.get("img_url")
    cafe.location = request.form.get("location")
    cafe.seats = request.form.get("seats")
    cafe.has_toilet = bool(request.form.get("has_toilet"))
    cafe.has_wifi = bool(request.form.get("has_wifi"))
    cafe.has_sockets = bool(request.form.get("has_sockets"))
    cafe.can_take_calls = bool(request.form.get("can_take_calls"))
    cafe.coffee_price = request.form.get("coffee_price")
    if Cafe.query.filter_by(name=request.form.get("name")).first() is None:
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={"Ok": "Successfully added the new cafe."}), 200
    return jsonify(response={"Conflict": "The cafe you're trying to add already exists in the database."}), 409


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    coffee_price = request.args.get("new_price")
    if cafe is not None:
        cafe.coffee_price = coffee_price
        db.session.commit()
        return jsonify(response={"Ok": "Successfully updated the price."}), 200
    return jsonify(response={"Not Found": "The price was not updated. Please try again using a valid id."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = "TopSecretAPIKey"
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if request.args.get("api_key") == api_key:
        if cafe is not None:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Ok": "Successfully deleted the cafe."}), 200
        return jsonify(response={"Not Found": "The cafe id was not found. No cafe was deleted."}), 404
    return jsonify(response={"Forbidden": "You don't have permission to delete the cafe."}), 403


if __name__ == '__main__':
    app.run(debug=True)
