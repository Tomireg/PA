from flask import Flask, render_template, request, url_for
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

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
    plot_path = None  # Initialize plot_path
    try:
        numbers = np.array([int(request.form[f'num{i}']) for i in range(1, 6)])
        submit_type = request.form['submit-type']

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
            result = np.sort(numbers).tolist()  # Converting the sorted array back to a list
            result_type = 'ordered'
            plot_path = generate_plot(result)
        else:
            result = None
            result_type = None

        return render_template("result.html", result=result, result_type=result_type, plot_path=plot_path if submit_type == 'order' else None)
    except ValueError:
        return render_template("error.html", message="Invalid input. Please enter valid integers.")

def sum_of_digits(numbers):
    total = np.sum([np.sum([int(digit) for digit in str(abs(num))]) for num in numbers])
    return total

def generate_plot(numbers):
    # Ensure the static directory exists
    static_dir = os.path.join(app.root_path, 'static')
    if not os.path.exists(static_dir):
        logging.debug(f"Creating directory: {static_dir}")
        os.makedirs(static_dir)

    fig, ax = plt.subplots()  # Create a new figure

    # Plot the line with axes
    ax.plot(numbers, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Ordered Numbers')
    
    # Annotate each point with its value
    for i, num in enumerate(numbers):
        ax.text(i, num, str(num), ha='center', va='bottom')

    plot_path = os.path.join(static_dir, 'plot.png')
    logging.debug(f"Saving plot to: {plot_path}")
    fig.savefig(plot_path)
    plt.close(fig)  # Close the figure to free up memory
    
    if not os.path.exists(plot_path):
        logging.error(f"Failed to save plot to: {plot_path}")
    else:
        logging.debug(f"Plot successfully saved to: {plot_path}")
    
    return 'plot.png'

if __name__ == "__main__":
    app.run(debug=True, port=8080)