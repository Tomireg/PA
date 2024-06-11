from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

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
def game():
    return render_template("game.html")

@app.route("/calculate", methods=['POST'])
def calculate():
    try:
        # Retrieve form data
        numbers = [
            int(request.form['num1']),
            int(request.form['num2']),
            int(request.form['num3']),
            int(request.form['num4']),
            int(request.form['num5'])
        ]

        # Calculate the smallest number using numpy
        smallest_number = np.min(numbers)

        # Render the result page with the smallest number
        return render_template("result.html", smallest_number=smallest_number)
    except ValueError:
        # Handle the case where the input is not valid integers
        return "Invalid input. Please enter valid integers.", 400

if __name__ == "__main__":
    app.run(debug=True, port=8080)