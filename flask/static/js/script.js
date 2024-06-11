document.addEventListener("DOMContentLoaded", init);

function init() {
  let savedTheme = localStorage.getItem('selected-theme') || 'theme1';
  setTheme(savedTheme);

  let themePicker = document.getElementById("theme-picker");
  themePicker.value = savedTheme;
  themePicker.addEventListener("change", function() {
    let selectedTheme = themePicker.value;
    setTheme(selectedTheme);
    localStorage.setItem('selected-theme', selectedTheme);
  });
}

function setTheme(theme) {
  let themeStylesheet = document.getElementById("theme-stylesheet");
  themeStylesheet.href = `/static/css/${theme}.css`;
}