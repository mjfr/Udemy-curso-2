from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterUserForm(FlaskForm):
    name = StringField("Your name", validators=[DataRequired()])
    email = EmailField("Your email", validators=[DataRequired()])
    password = PasswordField("Your password", validators=[DataRequired()])
    password_confirmation = PasswordField("Confirm your password", validators=[DataRequired()])
    submit = SubmitField("Register!")


class LoginUserForm(FlaskForm):
    email = EmailField("Your email", validators=[DataRequired()])
    password = PasswordField("Your password", validators=[DataRequired()])
    submit = SubmitField("Login!")
