document.getElementById('obituaryForm').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const dateOfBirth = document.getElementById('date_of_birth').value;
    const dateOfDeath = document.getElementById('date_of_death').value;
    const content = document.getElementById('content').value;
    const author = document.getElementById('author').value;

    if (!name || !dateOfBirth || !dateOfDeath || !content || !author) {
        alert('Please fill in all fields.');
        event.preventDefault();
    }
});
