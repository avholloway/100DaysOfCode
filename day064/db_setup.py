from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-list-1.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String(255), unique=False, nullable=False)
    img = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return f"<Movie {self.title} ({self.year})>"

if __name__ == "__main__":
    db.create_all()
    db.session.add(Movie(title="There Will Be Blood", year="2010", description="I drink your mulkshake", rating=10, ranking=1, review="I loved it!", img="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT9ryXsOVU9cs-rNjm63cFYpSXuHlgWpdllu66VQxqQojO89Hpz"))
    db.session.commit()