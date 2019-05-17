// set variables
var $myAjax = $(".ajax");
var $myButton = $(".my-button");

// Load it the first time onto page
// Need to clean this code up a lot
$myAjax.load("/temp");

// Function to load external resource
function loadTemp() {
    $myAjax.load("/temp");
}

// When button is clicked call the function, then call it over and over again
$myButton.click(function() {
    loadTemp();
    setInterval(loadTemp, 500);
});  