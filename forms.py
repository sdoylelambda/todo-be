from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField,SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = EmailField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = EmailField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
