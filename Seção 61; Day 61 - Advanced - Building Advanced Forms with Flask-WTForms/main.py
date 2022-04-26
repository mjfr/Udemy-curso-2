import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = os.environ["CSRF_SK"]
Bootstrap(app)


class SignupForm(FlaskForm):
    email = StringField(label="Email", validators=[validators.DataRequired(),
                                                   validators.Email(message="Type a valid email address. Try again")])
    password = PasswordField(label="Password", validators=[validators.DataRequired(),
                                                           validators.Length(min=8, message="The password must have at"
                                                                                            " least 8 characters.")])
    submit = SubmitField(label="Log In", render_kw={"btn-primary": "true"})  # render_kw used to activate the button
    # with the css change


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = SignupForm()
    email_match = "admin@email.com"
    password_match = "12345678"
    if form.validate_on_submit():
        if form.email.data == email_match and form.password.data == password_match:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
