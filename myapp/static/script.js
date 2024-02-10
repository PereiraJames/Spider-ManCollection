var filterInput = document.getElementById('filterInput');
var stateInput = document.getElementById('stateInput');

// Add event listener for keyup event on the input element
filterDropdown.addEventListener('change', function() {
    // Get the selected value from the dropdown
    var filterValue = filterDropdown.value.toUpperCase();
    console.log("Dropdown selection changed!");

    // Get all elements with class "photogroup"
    var photogroups = document.querySelectorAll('.photogroup');

    // Loop through each photogroup
    for (var i = 0; i < photogroups.length; i++) {
        // Get the state from the data-state attribute

        var state = photogroups[i].getAttribute('data-state').toUpperCase();

        // Check if the state matches the filter value
        if (state === filterValue || filterValue === 'ALL') {
            // If it matches, display the photogroup
            photogroups[i].style.display = '';
        } else {
            // If it doesn't match, hide the photogroup
            photogroups[i].style.display = 'none';
        }
    }
});