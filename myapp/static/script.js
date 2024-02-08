var filterInput = document.getElementById('filterInput');

// Add event listener for keyup event on the input element
filterInput.addEventListener('keyup', function() {
    // Get the value entered in the input element
    var filterValue = filterInput.value.toUpperCase();
    console.log("Form submitted!");

    // Get all elements with class "photogroup"
    var photogroups = document.querySelectorAll('.photogroup');

    // Loop through each photogroup
    for (var i = 0; i < photogroups.length; i++) {
        // Get the state from the data-state attribute
        var state = photogroups[i].getAttribute('data-state').toUpperCase();

        // Check if the state matches the filter value
        if (state.indexOf(filterValue) > -1) {
            // If it matches, display the photogroup
            photogroups[i].style.display = '';
        } else {
            // If it doesn't match, hide the photogroup
            photogroups[i].style.display = 'none';
        }
    }
});

document.getElementById("stateForm").addEventListener("submit", function(event) {

    event.preventDefault(); // Prevent default form submission behavior


    // Perform form submission using AJAX
    submitForm();
});

function submitForm() {
    var form = document.getElementById("stateForm");
    var formData = new FormData(form);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/comiclist/", true);
    xhr.onload = function () {
        if (xhr.status == 200) {
            // Refresh the page after successful form submission
            window.location.reload();
            
            console.log("Form submitted!");

        } else {
            // Handle error
            console.error("Form submission failed:", xhr.responseText);
        }
    };
    xhr.onerror = function () {
        // Handle network error
        console.error("Network error occurred.");
    };
    xhr.send(formData);
    console.log("Form submitted!");

}

function sendDataToServer() {
    var dataToSend = "Data to be inserted"; // Replace with your actual data
    $.ajax({
        type: 'POST',
        url: '/insert/',  // URL mapped to the insert_data view
        data: {
            'your_data': dataToSend
        },
        success: function(response) {
            if (response.success) {
                console.log('Data inserted successfully');
            } else {
                console.error('Failed to insert data:', response.error);
            }
        },
        error: function(xhr, status, error) {
            console.error('Error occurred while inserting data:', error);
        }
    });
}