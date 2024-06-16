from flask import Flask, render_template, request, redirect, flash, url_for
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging
from dotenv import load_dotenv
import secrets
from forms import ContactForm
from flask_mail import Mail, Message
import re



secret_key = secrets.token_hex(16)  # Generates a 32-character hexadecimal string (16 bytes)
print(secret_key)


load_dotenv()
# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = '275deb8819b3d4107e63d15eab37ffd1'

app.config['MAIL_SERVER'] = 'live.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587  # You can also use 2525 or 25
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = 'ec21ca007c74102a951c37285636c289'  # Replace with your actual password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Custom validation
        if not name or not email or not message:
            flash('All fields are required!')
            return redirect(url_for('contact'))
       
        if len(name) < 2 or len(name) > 50:
            flash('Name must be between 2 and 50 characters.')
            return redirect(url_for('contact'))
       
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address.')
            return redirect(url_for('contact'))
       
        if len(message) < 10:
            flash('Message must be at least 10 characters long.')
            return redirect(url_for('contact'))

        # Compose email
        msg = Message(subject='Contact Form Submission',
                      sender=email,
                      recipients=['pythonassingmentflasktest@gmail.com'],
                      body=f"Name: {name}\nEmail: {email}\nMessage: {message}")

        # Send email
        mail.send(msg)
        flash('Thank you for submitting your message!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

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