// JavaScript code can be added as needed for interactivity
// No JavaScript is needed for this simple example
// Get all the buttons on the page
const buttons = document.querySelectorAll('button');

// Add event listeners to each button
buttons.forEach(button => {
    button.addEventListener('mouseover', () => {
        button.classList.add('cool-effect');
    });

    button.addEventListener('mouseout', () => {
        button.classList.remove('cool-effect');
    });
});