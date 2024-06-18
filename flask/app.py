from flask import Flask, render_template, request
import numpy as np
import logging
from datetime import datetime
from animation import generate_welcome_animation  # Import animation.py
from graph import generate_plot  # Import graph.py

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

Fruits = ["Apple", "Pear", "Grape", "Strawberry",  
          "Raspberry", "Blackcurrant", "Blueberry", "Watermelon", "Banana", "Mango"] 


@app.route("/")
@app.route("/home")
def home():
    welcome_animation_path = generate_welcome_animation(app.root_path)
    return render_template("home.html", welcome_animation_path=welcome_animation_path)

@app.route("/greet", methods=['POST'])
def greet():
    name = request.form['name']
    if not name:
        return render_template("error.html", message="Name cannot be empty.")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("greetings.html", name=name, current_time=current_time)

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
    return render_template("game.html", len=len(Fruits), Fruits=Fruits)

@app.route("/calculate", methods=['POST'])
def calculate():
    try:
        numbers = np.array([int(request.form[f'num{i}']) for i in range(1, 6)])
        submit_type = request.form['submit-type']

        plot_path = None
        if submit_type == 'smallest':
            result = np.min(numbers)
            result_type = 'smallest'
        elif submit_type == 'largest':
            result = np.max(numbers)
            result_type = 'largest'
        elif submit_type == 'sum':
            result = sum_of_digits(numbers)
            result_type = 'sum'
        elif submit_type == 'order':
            result = np.sort(numbers).tolist()  
            result_type = 'ordered'
            plot_path = generate_plot(app.root_path, result)
        else:
            result = None
            result_type = None

        return render_template("result.html", result=result, result_type=result_type, plot_path=plot_path if submit_type == 'order' else None)
    except ValueError:
        return render_template("error.html", message="Invalid input. Please enter valid integers.")

def sum_of_digits(numbers):
    total = np.sum([np.sum([int(digit) for digit in str(abs(num))]) for num in numbers])
    return total

if __name__ == "__main__":
    app.run(debug=True, port=8080)