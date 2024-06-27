"use strict";

document.addEventListener('DOMContentLoaded', function() {
    // Add a click event listener to the <nav> element
    document.querySelector('nav').addEventListener('click', function(event) {
        // Check if the clicked element parent is an <li> with the desired classes
        var parent = event.target.parentElement;
        var grandparent = parent.parentElement;
        console.log("click the chapter");
        if (((event.target.tagName == 'path' || event.target.tagName == 'svg' || event.target.tagName == 'DIV') && 
            ((parent.tagName === 'LI' && 
            parent.classList.contains('chapter-item')) || 
            (grandparent.tagName === 'LI' && 
            grandparent.classList.contains('chapter-item')))) ||
            (event.target.tagName === 'LI' && 
            event.target.classList.contains('chapter-item'))) {
            console.log("toggle section + chevron")
            var liElement = null;
            // click li itself
            if (event.target.tagName == 'LI') {
                console.log("click LI itself")
                liElement = event.target;
            // click li grand children
            } else if (event.target.tagName == 'path') {
                console.log("click LI grand children")
                liElement = grandparent;
            // click li children
            } else {
                console.log("click LI children")
                liElement = parent;
            }
            // Toggle the 'expanded' class on the clicked <li>
            liElement.classList.toggle('expanded');
            // rotate the svg
            var svgElement = liElement.querySelector('svg');
            svgElement.classList.toggle('nav-svg-rotate-90');
            // trigger animation for the "section" block ?
        } else {
            console.log("fail to expand");
            console.log("event target :");
            console.log(event.target.tagName);
        }
    });
});