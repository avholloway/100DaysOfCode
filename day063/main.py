from flask import Flask, render_template, request, redirect, url_for
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


def add_book(title, author, rating):
    try:
        db.session.add(Book(title=title, author=author, rating=rating))
        db.session.commit()
    except:
        return False
    else:
        return True


def get_book(id):
    try:
        book = Book.query.get(id)
    except:
        return None
    else:
        return book


def get_books():
    try:
        books = db.session.query(Book).all()
    except:
        return []
    else:
        return books


def update_book(id, **kwargs):
    try:
        book = Book.query.get(id)
    except:
        return False
    
    if not book:
        return False

    title = kwargs.get("title")
    if title:
        book.title = title

    author = kwargs.get("author")
    if author:
        book.author = author

    rating = kwargs.get("rating")
    if rating:
        book.rating = rating

    try:
        db.session.commit()
    except:
        return False
    else:
        return True


def delete_book(id):
    try:
        book = Book.query.get(id)
    except:
        return False

    if not book:
        return False

    try:
        db.session.delete(book)
        db.session.commit()
    except:
        return False
    else:
        return True


@app.route('/')
def home():
    return render_template("index.html", books=get_books())


@app.route("/delete")
def delete():
    delete_book(request.args["id"])
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():

    # posts can update or create books
    if request.method.upper() == "POST":
        
        # update
        if (id := request.form["id"]):
            
            update_book(id, title=request.form["title"], author=request.form["author"], rating=request.form["rating"])

        # create
        else:
            add_book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
            
        # back to the listings
        return redirect(url_for("home")) 

    # gets can read by query param id, otherwise blank form
    elif request.method.upper() == "GET":

        if (id := request.args.get("id")):
            book = get_book(id)
        else:
            book = {"id":"","title":"","author":"","rating":""}
        return render_template("add.html", book=book)

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)