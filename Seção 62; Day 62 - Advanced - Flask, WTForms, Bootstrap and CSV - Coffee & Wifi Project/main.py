import wtforms.validators
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, TimeField, SelectField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label="Cafe Name", validators=[DataRequired()])
    location = URLField(label="Location URL (Must contain http://)",
                        validators=[DataRequired(), wtforms.validators.URL(message="Use a valid URL.")])
    opening_time = TimeField(label="Open Time", validators=[DataRequired()])
    closing_time = TimeField(label="Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", choices=["✘", "☕", 2 * "☕", 3 * "☕", 4 * "☕", 5 * "☕"],
                                validators=[DataRequired()])
    wifi_rating = SelectField(label="Wifi Rating", choices=["✘", "💪", 2 * "💪", 3 * "💪", 4 * "💪", 5 * "💪"],
                              validators=[DataRequired()])
    power_outlet_rating = SelectField(label="Power Outlet Rating",
                                      choices=["✘", "🔌", 2 * "🔌", 3 * "🔌", 4 * "🔌", 5 * "🔌", 5 * "🔌"],
                                      validators=[DataRequired()])
    submit = SubmitField(label="Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as csv_file:
            form.opening_time.data = form.opening_time.data.strftime("%I:%M%p")
            form.closing_time.data = form.closing_time.data.strftime("%I:%M%p")
            form_data = [value.data for value in form][0:-2]
            csv_data = csv.writer(csv_file, delimiter=",")
            csv_data.writerow(form_data)
            return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        # for row in csv_data:
        #     list_of_rows.append(row)
        list_of_rows = [row for row in csv_data]
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
