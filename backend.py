from flask import Flask
from flask import render_template , redirect


app = Flask(__name__ ,static_url_path='/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/supports")
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)

