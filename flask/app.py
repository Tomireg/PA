from flask import Flask, render_template, request, url_for
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

Fruits = ["Apple", "Pear", "Grape", "Strawberry",  
          "Raspberry", "Blackcurrant", "Blueberry", "Watermelon", "Banana", "Mango"] 


def generate_welcome_animation():
    fig, ax = plt.subplots(figsize=(4, 2))  
    fig.patch.set_facecolor('cadetblue')  
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')  

    text = ax.text(0.5, 0.5, "", fontsize=30, ha='center')

    def update(frame):
        if frame < 100:
            alpha = frame / 100
            text.set_text("Welcome")
            text.set_alpha(alpha)
        else:
            text.set_text("Welcome")
            text.set_alpha(1)
        return text,

    anim = FuncAnimation(fig, update, frames=200, interval=30)
    
    animation_dir = os.path.join(app.root_path, 'static', 'assets', 'animation')
    if not os.path.exists(animation_dir):
        os.makedirs(animation_dir)

    gif_path = os.path.join(animation_dir, 'welcome_animation.gif')
    if not os.path.exists(gif_path):  
        anim.save(gif_path, writer='pillow')

    plt.close(fig)

    return url_for('static', filename='assets/animation/welcome_animation.gif')

@app.route("/")
@app.route("/home")
def home():
    welcome_animation_path = generate_welcome_animation()
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
    graph_dir = os.path.join(app.root_path, 'static', 'assets', 'graph')
    if not os.path.exists(graph_dir):
        logging.debug(f"Creating directory: {graph_dir}")
        os.makedirs(graph_dir)

    plt.figure()

    plt.plot(numbers, marker='o', linestyle='-', color='b')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Ordered Numbers')
    
    for i, num in enumerate(numbers):
        plt.text(i, num, str(num), ha='center', va='bottom')

    plot_path = os.path.join(graph_dir, 'plot.png')
    logging.debug(f"Saving plot to: {plot_path}")
    plt.savefig(plot_path)
    plt.close()
    
    if not os.path.exists(plot_path):
        logging.error(f"Failed to save plot to: {plot_path}")
    else:
        logging.debug(f"Plot successfully saved to: {plot_path}")
    
    return url_for('static', filename='assets/graph/plot.png')

if __name__ == "__main__":
    app.run(debug=True, port=8080)