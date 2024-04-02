document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch dishes data from Flask backend
    function fetchDishes() {
        fetch('/api/dishes')
            .then(response => response.json())
            .then(data => {
                // Update the HTML to display dishes data
                updateDishes(data);
            })
            .catch(error => console.error('Error fetching dishes:', error));
    }

    // Function to update HTML with fetched dishes data
    function updateDishes(dishes) {
        // Example: Update the 'recipes' div with fetched dishes data
        const recipesDiv = document.getElementById('recipes');
        recipesDiv.innerHTML = ''; // Clear previous content
        dishes.forEach(dish => {
            const dishElement = document.createElement('div');
            dishElement.innerHTML = `<h3>${dish.name}</h3><p>Price: ${dish.price}</p>`;
            recipesDiv.appendChild(dishElement);
        });
    }

    // Fetch dishes data when the page loads
    fetchDishes();

    // Example: Handling reservation form submission
    const reservationForm = document.getElementById('reservation-form');
    reservationForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Get form data
        const formData = new FormData(reservationForm);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Send reservation data to Flask backend
        fetch('/api/reservation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log('Reservation successful:', data);
            // Redirect or display success message
        })
        .catch(error => {
            console.error('Error submitting reservation:', error);
            // Display error message to user
        });
    });
});
