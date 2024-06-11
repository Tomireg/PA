document.addEventListener("DOMContentLoaded", init);

function init() {
    // Theme initialization
    let savedTheme = localStorage.getItem('selected-theme') || 'theme1';
    setTheme(savedTheme);

    let themePicker = document.getElementById("theme-picker");
    themePicker.value = savedTheme;
    themePicker.addEventListener("change", function() {
        let selectedTheme = themePicker.value;
        setTheme(selectedTheme);
        localStorage.setItem('selected-theme', selectedTheme);
    });

    // Form validation
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

    // Event listener for the new button (Calculate Largest)
    document.getElementById('calculate-largest').addEventListener('click', function(event) {
        // Call the setSubmitType function with the parameter 'largest'
        setSubmitType('largest');
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