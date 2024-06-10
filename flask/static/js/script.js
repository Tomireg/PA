document.addEventListener("DOMContentLoaded", init);

function init() {
    // Dark mode initialization
    let darkModeStore = localStorage.getItem('dark-mode');

    if (darkModeStore === null) {
        localStorage.setItem("dark-mode", false);
    }
    if (darkModeStore === "true") {
        setDarkMode();
    }

    let myButton = document.getElementById("mybtn");
    myButton.addEventListener("click", clickedDarkMode);

    // Game initialization
    const canvas = document.getElementById('gameCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        setInterval(() => gameLoop(ctx), 100); // Update every 100ms
        document.addEventListener('keydown', handleKeydown);
    }
}

function clickedDarkMode() {
    toggleDarkMode();
    setDarkMode();
}

function toggleDarkMode() {
    if (localStorage.getItem("dark-mode") === "true") {
        localStorage.setItem("dark-mode", false);
    } else {
        localStorage.setItem("dark-mode", true);
    }
}

function setDarkMode() {
    styleBody();
    styleBtn();
    styleNav();
}

function styleBody() {
    let element = document.body;
    element.classList.toggle("dark-mode");
}

function styleBtn() {
    let dmBtn = document.getElementById("mybtn");
    dmBtn.classList.toggle("dmbtn");
}

function styleNav() {
    let allButtons = document.getElementsByClassName("nav-item");
    for (let i = 0; i < allButtons.length; i++) {
        let button = allButtons[i];
        button.classList.toggle("nav-item-dark");
    }
}

// Game functions
function draw(ctx, state) {
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);

    ctx.fillStyle = 'green';
    state.snake_body.forEach(segment => {
        ctx.fillRect(segment[0], segment[1], 10, 10);
    });

    ctx.fillStyle = 'white';
    ctx.fillRect(state.fruit_position[0], state.fruit_position[1], 10, 10);

    ctx.fillStyle = 'white';
    ctx.font = '20px Arial';
    ctx.fillText('Score: ' + state.score, 10, 20);
}

function gameLoop(ctx) {
    fetch('/game_state')
        .then(response => response.json())
        .then(state => {
            if (state.status === "game_over") {
                alert("Game Over! Your score: " + state.score);
                return;
            }
            draw(ctx, state);
        });
}

function handleKeydown(event) {
    const keyDirection = {
        'ArrowUp': 'UP',
        'ArrowDown': 'DOWN',
        'ArrowLeft': 'LEFT',
        'ArrowRight': 'RIGHT'
    };
    const direction = keyDirection[event.key];
    if (direction) {
        fetch('/game_state', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ direction })
        });
    }
}