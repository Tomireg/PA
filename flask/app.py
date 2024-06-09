from flask import Flask, render_template, redirect, url_for, request
import subprocess

app = Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/game")
def login():
        return render_template("game.html")

@app.route("/run_snake")
def run_snake():
     subprocess.Popen(["python3", "snake.py"])
     return redirect(url_for("/game"))
     

if __name__ == "__main__":
    app.run(debug=True, port=8080)