document.addEventListener("DOMContentLoaded", init);

function init() {
    // Theme initialization code
    let savedTheme = localStorage.getItem('selected-theme') || 'theme1';
    setTheme(savedTheme);

    let themePicker = document.getElementById("theme-picker");
    themePicker.value = savedTheme;
    themePicker.addEventListener("change", function() {
        let selectedTheme = themePicker.value;
        setTheme(selectedTheme);
        localStorage.setItem('selected-theme', selectedTheme);
        updateAnimation(selectedTheme);
    });

    // Form validation code
    document.getElementById('number-form').addEventListener('submit', function(event) {
        let valid = true;
        for (let i = 1; i <= 5; i++) {
            let num = document.getElementById('num' + i).value;
            if (isNaN(num) || num.trim() === '') {
                valid = false;
                alert('Please enter valid integers in all fields.');
                break;
            }
        }
        if (!valid) {
            event.preventDefault();
        }
    });

    // Event listener for the new button (Order Numbers)
    document.getElementById('order-numbers').addEventListener('click', function(event) {
        // Call the setSubmitType function with the parameter 'order'
        setSubmitType('order');
    });

    updateAnimation(savedTheme);
}

function setTheme(theme) {
    let themeStylesheet = document.getElementById("theme-stylesheet");
    themeStylesheet.href = `/static/css/${theme}.css`;
}

function updateAnimation(theme) {
    fetch(`/generate_animation/${theme}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('welcome-animation').src = data.url;
        })
        .catch(error => console.error('Error:', error));
}

function setSubmitType(type) {
    // Set the value of the hidden input field 'submit-type' to the specified type
    document.getElementById('submit-type').value = type;
    // Submit the form
    document.getElementById('number-form').submit();
}