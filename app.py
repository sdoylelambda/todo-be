from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, login_manager, User, ToDO
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x14B~^\x07\xe1\x197\xda\x18\xa6[[\x05\x03QVg\xce%\xb2<\x80\xa4\x00'
app.config['DEBUG'] = True

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

# db.create_all()

db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''
    return "Hello World"


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit:
            user = User(email=form.username.data,
                        password=generate_password_hash(form.password.data)
                        )
            db.session.add(user)
            db.session.commit()
            return redirect('/login')


@app.route("/login")
def login():
    '''
    Home page - Sign up/Sign in
    '''
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(email=form.username.data)
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect('/todos')
        flash("Invalid details")

    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/todo")
def todo():
    '''
    Home page - View, add, edit, and delete todos
    '''
    return render_template('todo.html')


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True, port=3000)
