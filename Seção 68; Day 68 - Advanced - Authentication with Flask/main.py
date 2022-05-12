from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

# Secret key generated with: python -c 'import secrets; print(secrets.token_hex())'
app.config['SECRET_KEY'] = 'd1de9d2ef868e4379442caab7faffc10ba9e7a442441e4336d1d2a5a99d1de79'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "./static/files/"
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


def password_generation(password):
    return generate_password_hash(method="pbkdf2:sha256", salt_length=8, password=password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User()
        password = password_generation(password=request.form.get("password"))
        new_user.name = request.form.get("name")
        new_user.email = request.form.get("email")
        new_user.password = password
        if User.query.filter_by(email=new_user.email).first():
            flash(message="This e-mail already exists, login instead.", category="error")
            return redirect(url_for("login"))
        db.session.add(new_user)
        db.session.commit()
        login_user(user=new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user is None:
            flash(message="That email does not exist, please try again.", category="error")
        elif check_password_hash(password=request.form.get("password"), pwhash=user.password):
            login_user(user=user)
            return redirect(url_for("secrets"))
        else:
            flash(message="The password does not match, please try again.", category="error")
    return render_template("login.html")


@app.route('/secrets', methods=["GET", "POST"])
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"], path="cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
