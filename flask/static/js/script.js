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

    document.getElementById('contact-form').addEventListener('submit', function(event) {
        // Validate the contact form
        let name = document.getElementById('name').value.trim();
        let email = document.getElementById('email').value.trim();
        let message = document.getElementById('message').value.trim();

        if (name === '' || email === '' || message === '') {
            alert('Please fill in all fields.');
            event.preventDefault();
            return;
        }

        if (!validateEmail(email)) {
            alert('Please enter a valid email address.');
            event.preventDefault();
            return;
        }
    });
}

function setTheme(theme) {
    let themeStylesheet = document.getElementById("theme-stylesheet");
    themeStylesheet.href = `/static/css/${theme}.css`;
}

function setSubmitType(type) {
    // Set the value of the hidden input field 'submit-type' to the specified type
    document.getElementById('submit-type').value = type;
    // Submit the form
    document.getElementById('number-form').submit();
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}