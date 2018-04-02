// Get the modal
var modal1 = document.getElementById('id01');
var modal2 = document.getElementById('id02');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
    }
    if (event.target == modal2) {
        modal2.style.display = "none";
    }
}

// Track any press of the escape button and close modals.
document.onkeydown = function(evt) {
    // evt = evt || window.event;
    if (evt.keyCode == 27) {
        modal1.style.display = "none";
        modal2.style.display = "none";
    }
};
