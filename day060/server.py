import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)


def fetch_posts():
    resp = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
    resp.raise_for_status()
    return resp.json()


@app.route("/")
def page_home():
    return render_template("index.html", posts=fetch_posts())


@app.route("/about")
def page_about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def page_contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        print(f"{name=}, {message=}")
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    elif request.method == "GET":
        return render_template("contact.html")


@app.route("/post/<int:id>")
def page_post(id):
    return render_template("post.html", post=[post for post in fetch_posts() if post['id'] == id][0])


if __name__ == "__main__":
    app.run(debug=True)