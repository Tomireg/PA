from flask import Flask, render_template, request, jsonify
import random
import threading
import time

app = Flask(__name__)

# Initial game state
game_state = {
    'snake_body': [[100, 50], [90, 50], [80, 50], [70, 50]],
    'fruit_position': [random.randrange(1, 72) * 10, random.randrange(1, 48) * 10],
    'direction': 'RIGHT',
    'score': 0,
    'status': 'running'
}
game_speed = 0.1  # Game speed in seconds

def update_game_state():
    global game_state
    while game_state['status'] == 'running':
        snake_body = game_state['snake_body']
        fruit_position = game_state['fruit_position']
        direction = game_state['direction']
        
        new_head = list(snake_body[0])
        
        if direction == 'UP':
            new_head[1] -= 10
        if direction == 'DOWN':
            new_head[1] += 10
        if direction == 'LEFT':
            new_head[0] -= 10
        if direction == 'RIGHT':
            new_head[0] += 10
        
        # Check for collision with boundaries
        if (new_head[0] < 0 or new_head[0] >= 720 or
            new_head[1] < 0 or new_head[1] >= 480 or
            new_head in snake_body):
            game_state['status'] = 'game_over'
            return
        
        snake_body.insert(0, new_head)
        
        if new_head == fruit_position:
            game_state['score'] += 10
            game_state['fruit_position'] = [random.randrange(1, 72) * 10, random.randrange(1, 48) * 10]
        else:
            snake_body.pop()
        
        game_state['snake_body'] = snake_body
        
        time.sleep(game_speed)

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
            direction = data['direction']
            current_direction = game_state['direction']
            if direction == 'UP' and current_direction != 'DOWN':
                game_state['direction'] = direction
            if direction == 'DOWN' and current_direction != 'UP':
                game_state['direction'] = direction
            if direction == 'LEFT' and current_direction != 'RIGHT':
                game_state['direction'] = direction
            if direction == 'RIGHT' and current_direction != 'LEFT':
                game_state['direction'] = direction
    return jsonify(game_state)

if __name__ == "__main__":
    threading.Thread(target=update_game_state).start()
    app.run(debug=True, port=8080)