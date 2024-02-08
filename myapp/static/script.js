var filterInput = document.getElementById('filterInput');

// Add event listener for keyup event on the input element
filterInput.addEventListener('keyup', function() {
    // Get the value entered in the input element
    var filterValue = filterInput.value.toUpperCase();

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