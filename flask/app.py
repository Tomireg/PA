from flask import Flask, render_template, jsonify, request
from snake import game

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
def game_view():
    return render_template("game.html")

@app.route("/game_state", methods=['GET', 'POST'])
def game_state():
    if request.method == 'POST':
        direction = request.json.get('direction')
        if direction:
            game.update_direction(direction)
        running = game.update()
        if not running:
            return jsonify({"status": "game_over"})
    return jsonify(game.get_state())

if __name__ == "__main__":
    app.run(debug=True, port=8080)