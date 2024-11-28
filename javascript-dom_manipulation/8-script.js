// fetch the data from the API and display it in the HTML

document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hello').textContent = data.hello;
        })
        .catch(error => console.error('Error:', error));
});
