from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-list-1.db'
Bootstrap(app)
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


def add_movie(**kwargs):
    try:
        db.session.add(Movie(
            title=kwargs.get("title"),
            year=kwargs.get("year"),
            description=kwargs.get("description"),
            rating=kwargs.get("rating"),
            ranking=kwargs.get("rating"),
            review=kwargs.get("review"),
            img=kwargs.get("img")
        ))
        db.session.commit()
    except:
        return False
    else:
        return True


def get_movie(id):
    try:
        movie = Movie.query.get(id)
    except:
        return None
    else:
        return movie


def get_movies():
    try:
        movies = db.session.query(Movie).all()
    except:
        return []
    else:
        return movies


def update_movie(id, **kwargs):
    try:
        movie = Movie.query.get(id)
    except:
        return False
    
    if not movie:
        return False

    movie.title = kwargs.get("title") or movie.title
    movie.year = kwargs.get("year") or movie.year
    movie.description = kwargs.get("description") or movie.description
    movie.rating = kwargs.get("rating") or movie.rating
    movie.ranking = kwargs.get("ranking") or movie.ranking
    movie.review = kwargs.get("review") or movie.review
    movie.img = kwargs.get("img") or movie.img

    try:
        db.session.commit()
    except:
        return False
    else:
        return True


def delete_movie(id):
    try:
        movie = Movie.query.get(id)
    except:
        return False

    if not movie:
        return False

    try:
        db.session.delete(movie)
        db.session.commit()
    except:
        return False
    else:
        return True


@app.route("/")
def home():
    return render_template("index.html", movies=get_movies())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method.upper() == "POST":
        add_movie(**request.form)
        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method.upper() == "POST":
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", id=request.args["id"])


@app.route("/delete", methods=["GET", "POST"])
def delete():
    delete_movie(request.args["id"])
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
