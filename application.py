from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} - {self.author}"

@app.route('/')
def index():
    return ('hello')

@app.route('/books')
def get_books():

    return {"books": "books data"}