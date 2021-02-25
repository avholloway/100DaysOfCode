from flask import Flask
from random import randint

the_number = randint(1, 10)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'<h1 style="text-align: center;">Guess a Number between 1 and 10 by adding it to the URL above</h1>'


@app.route("/<int:guess>")
def get_guess(guess):
    if guess == the_number:
        return '<div style="text-align: center; color: green;">' \
            '<h1>You guessed the number!</h1>' \
                '<img src="https://media.giphy.com/media/jYk9SJsM0CBI2K0oa4/giphy.gif" width="300" /></div>'
    else:
        return f'<h1 style="text-align: center; color: red;">Oooo! Too {"high" if guess > the_number else "low"}! Try again!</h1>'


if __name__ == "__main__":
    app.run(debug=True)