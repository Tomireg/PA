from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initial game state
game_state = {
    'snake_body': [[100, 50], [90, 50], [80, 50], [70, 50]],
    'fruit_position': [150, 150],
    'direction': 'RIGHT',
    'score': 0,
    'status': 'running'
}

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

@app.route("/game_state", methods=['GET', 'POST'])
def game_state_route():
    global game_state
    if request.method == 'POST':
        data = request.json
        if 'direction' in data:
            game_state['direction'] = data['direction']
    return jsonify(game_state)

if __name__ == "__main__":
    app.run(debug=True, port=8080)