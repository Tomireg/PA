document.addEventListener("DOMContentLoaded", init);

function init() {

    let savedTheme = localStorage.getItem('selected-theme') || 'theme1';
    setTheme(savedTheme);

    let themePicker = document.getElementById("theme-picker");
    if (themePicker) {
        themePicker.value = savedTheme;
        themePicker.addEventListener("change", function () {
            let selectedTheme = themePicker.value;
            setTheme(selectedTheme);
            localStorage.setItem('selected-theme', selectedTheme);
        });
    }

    let numberForm = document.getElementById('number-form');
    if (numberForm) {
        numberForm.addEventListener('submit', function (event) {
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
    }

    let greetForm = document.forms["greetForm"];
    if (greetForm) {
        greetForm.addEventListener("submit", function (event) {
            const name = greetForm["name"].value;
            if (name === "") {
                alert("Name must be filled out");
                event.preventDefault();
            }
        });
    }
}

function setTheme(theme) {
    let themeStylesheet = document.getElementById("theme-stylesheet");
    if (themeStylesheet) {
        themeStylesheet.href = `/static/css/${theme}.css`;
    }
}

function setSubmitType(type) {
    let submitType = document.getElementById('submit-type');
    if (submitType) {
        submitType.value = type;
        let numberForm = document.getElementById('number-form');
        if (numberForm) {
            numberForm.submit();
        }
    }
}