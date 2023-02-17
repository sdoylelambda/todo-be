from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class TodoForm(FlaskForm):
    task_name = StringField('Name', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Complete', 'Complete'), ('Not Started', 'Not Started ')])
    submit = SubmitField('Add Task')
