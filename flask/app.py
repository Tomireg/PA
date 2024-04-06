from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/projects")
def home():
    return render_template("projects.html")

@app.route("/skills")
def home():
    return render_template("skills.html")

@app.route("/about")
def home():
    return render_template("about.html")

@app.route("/contacts")
def home():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)