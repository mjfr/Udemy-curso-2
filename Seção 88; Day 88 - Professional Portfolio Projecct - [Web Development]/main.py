# TODO 1 - Build a todo list website.
import os
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import SignUpForm, LoginForm
from datetime import date

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///online_todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    todo_lists = db.relationship("TodoList", back_populates="owner")


class TodoList(db.Model):
    __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=True)
    creation_date = db.Column(db.String(40), nullable=False)
    items = db.relationship("ListItem", back_populates="list_item")
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = db.relationship("User", back_populates="todo_lists")


class ListItem(db.Model):
    __tablename__ = "list_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    conclusion_state = db.Column(db.Boolean, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("todo_lists.id"))
    list_item = db.relationship("TodoList", back_populates="list_items")


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = SignUpForm()
    if request.method == "POST":
        new_user = User()
        new_user.name = form.name.data
        new_user.email = form.email.data
        new_user.password = generate_password_hash(method="pbkdf2:sha256", salt_length=8, password=form.password.data)
        if User.query.filter_by(email=new_user.email).first() is not None:
            flash(message="This email is already in use.", category="error")
            # return redirect(url_for("register"))
        if form.password.data != form.password_confirmation.data:
            flash(message="The password does not match the confirmation.", category="error")
            # return redirect(url_for("register"))
        if form.validate_on_submit():
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("get_lists"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None:
                flash(message="This email is not registered.", category="error")
            if not check_password_hash(pwhash=user.password, password=form.password.data):
                flash(message="Password does not match the registered one.", category="error")
            login_user(user)
            return redirect(url_for("get_lists"))
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


# Pensando nesta parte em fazer tudo dentro da mesma rota: Adicionar, ver e editar as listas e items de cada lista.
@app.route("/lists")
def lists():
    pass


if __name__ == "__main__":
    app.run(debug=True)
