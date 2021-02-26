import requests
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


@app.route("/guess/<string:name>")
def guess(name):
    resp = requests.get(f"https://api.agify.io/?name={name}")
    resp.raise_for_status()
    age = resp.json()["age"]
    resp = requests.get(f"https://api.genderize.io/?name={name}")
    resp.raise_for_status()
    gender = resp.json()["gender"]
    return render_template(
        "guess.html",
        name=name,
        age=age,
        gender=gender
    )


@app.route("/blog")
def blog_listing():
    resp = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    resp.raise_for_status()
    data = resp.json()
    return render_template("blog-listing.html", data=data)


@app.route("/post/<int:id>")
def get_post(id):
    resp = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    resp.raise_for_status()
    data = resp.json()
    for post in data:
        if post["id"] == id:
            return render_template("post.html", post=post)
    return "404 their big guy"

if __name__ == "__main__":
    app.run(debug=True)