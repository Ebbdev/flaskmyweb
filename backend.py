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

@app.route("/english/about")
def abouten():
    return render_template("abouten.html")

@app.route("/english/projects")
def projectsen():
    return render_template("projectsen.html")

@app.route("/english/support")
def supporsen():
    return render_template("support.html")


@app.route("/supports")
def support():
    return render_template("support.html")

@app.route("/english")
def english():
    return render_template("english.html")


if __name__ == "__main__":
    app.run(debug=True)

