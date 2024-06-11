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
        numbers = [
            int(request.form['num1']),
            int(request.form['num2']),
            int(request.form['num3']),
            int(request.form['num4']),
            int(request.form['num5'])
        ]

        # Check which button was clicked
        submit_type = request.form['submit-type']

        if submit_type == 'smallest':
            result = min(numbers)
            result_type = 'smallest'
        elif submit_type == 'largest':
            result = max(numbers)
            result_type = 'largest'
        else:
            result = None
            result_type = None

        # Render the result page with the result and result_type
        return render_template("result.html", result=result, result_type=result_type)
    except ValueError:
        return "Invalid input. Please enter valid integers.", 400
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)