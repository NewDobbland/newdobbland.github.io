from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def rhome():
    return redirect(url_for("home"))

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/projects.html")
def rprojects():
    return redirect(url_for("projects"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/about.html")
def rabout():
    return redirect(url_for("about"))

if __name__ == "__main__":
    app.run(debug=True)