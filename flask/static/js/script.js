const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const cellSize = 10;

// Initialize game state
let gameState = {
    snake: [{ x: 10, y: 10 }],
    food: { x: 15, y: 15 },
    direction: 'right',
    score: 0
};

// Function to draw a cell
function drawCell(x, y, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
}

// Function to draw the game
function drawGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw snake
    gameState.snake.forEach(segment => {
        drawCell(segment.x, segment.y, '#000');
    });

    // Draw food
    drawCell(gameState.food.x, gameState.food.y, 'red');

    // Display score
    ctx.fillStyle = '#000';
    ctx.font = '12px Arial';
    ctx.fillText('Score: ' + gameState.score, 10, 20);
}

// Function to update game state
function updateGameState() {
    fetch('/game_state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ direction: gameState.direction })
    })
    .then(response => response.json())
    .then(state => {
        gameState = state;
        drawGame();
        if (state.score === 0) {
            alert('Game Over! Your score: ' + state.score);
        }
    })
    .catch(error => console.error('Error updating game state:', error));
}

// Event listener for keypress
document.addEventListener('keydown', event => {
    const key = event.key.toLowerCase();
    if (['arrowup', 'arrowdown', 'arrowleft', 'arrowright'].includes(key)) {
        event.preventDefault();
        gameState.direction = key === 'arrowup' ? 'up' :
                               key === 'arrowdown' ? 'down' :
                               key === 'arrowleft' ? 'left' :
                               key === 'arrowright' ? 'right' : gameState.direction;
        updateGameState();
    }
});

// Start the game loop
setInterval(updateGameState, 100);