from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"<Book {self.title} by {self.title} - {self.rating} / 10>"

if __name__ == "__main__":
    db.create_all()
    book1 = Book(title="THe Little Hen", author="Anthony", rating=5.6)
    db.session.add(book1)
    db.session.commit()