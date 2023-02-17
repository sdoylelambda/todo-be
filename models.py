from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20))

    def __repr__(self):
        return '<User %r>' % self.username


class ToDO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    due_date = db.Column(db.String(10))
    complete = db.Column(db.Boolean)


with app.app_context():
    db.create_all()

    seed_user = User(username="TestUser", password="Password123")

#     db.session.add(User())
#     db.session.add(User())
#     db.session.add(ToDO())
