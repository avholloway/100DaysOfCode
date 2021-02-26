from datetime import datetime as dt
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    current_year = dt.now().year
    return render_template(
        "index.html",
        current_year=current_year
    )

if __name__ == "__main__":
    app.run(debug=True)