from flask import Flask, render_template, request, jsonify
import random
import threading
import time

app = Flask(__name__)

# Initial game state
game_state = {
    'snake': [{'x': 10, 'y': 10}],
    'food': {'x': 15, 'y': 15},
    'direction': 'right',
    'score': 0
}

# Function to update game state
def update_game_state():
    global game_state
    while True:
        # Move the snake
        head = game_state['snake'][0].copy()
        if game_state['direction'] == 'up':
            head['y'] -= 1
        elif game_state['direction'] == 'down':
            head['y'] += 1
        elif game_state['direction'] == 'left':
            head['x'] -= 1
        elif game_state['direction'] == 'right':
            head['x'] += 1
        
        # Check if the snake eats food
        if head['x'] == game_state['food']['x'] and head['y'] == game_state['food']['y']:
            game_state['score'] += 1
            game_state['snake'].insert(0, head)
            game_state['food'] = {'x': random.randint(0, 39), 'y': random.randint(0, 29)}
        else:
            game_state['snake'].insert(0, head)
            game_state['snake'].pop()
        
        # Check for collisions
        if (head['x'] < 0 or head['x'] >= 40 or
            head['y'] < 0 or head['y'] >= 30 or
            head in game_state['snake'][1:]):
            game_state['score'] = 0
            game_state['snake'] = [{'x': 10, 'y': 10}]
            game_state['food'] = {'x': 15, 'y': 15}
            game_state['direction'] = 'right'
        
        # Update every 0.1 seconds
        time.sleep(0.1)

threading.Thread(target=update_game_state).start()

# Routes
@app.route("/")
def index():
    return render_template("index.html")

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
            if direction in ['up', 'down', 'left', 'right']:
                game_state['direction'] = direction
    return jsonify(game_state)

if __name__ == "__main__":
    app.run(debug=True, port=8080)