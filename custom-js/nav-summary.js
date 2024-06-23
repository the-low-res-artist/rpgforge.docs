"use strict";

document.addEventListener('DOMContentLoaded', function() {
    // Add a click event listener to the <nav> element
    document.querySelector('nav').addEventListener('click', function(event) {
        // Check if the clicked element parent is an <li> with the desired classes
        var parent = event.target.parentElement;
        console.log("click the chapter");
        if ((event.target.tagName == 'svg' ||event.target.tagName == 'DIV') && 
            parent.tagName === 'LI' && 
            parent.classList.contains('chapter-item')) {
            console.log("toggle section + chevron")
            // Toggle the 'expanded' class on the clicked <li>
            parent.classList.toggle('expanded');
            // rotate the svg
            event.target.classList.toggle('nav-svg-rotate-90');
            // trigger animation for the "section" block ?
        } else {
            console.log("no toggle");
            console.log(event.target.tagName);
            console.log(parent.tagName);
            console.log(parent.classList)
        }
    });
});

// JavaScript to add an SVG icon to each <li> element
document.addEventListener('DOMContentLoaded', function() {
    // Create an SVG element
    const svgIcon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svgIcon.setAttribute('class', 'icon nav-svg-rotate-0');
    svgIcon.setAttribute('viewBox', '0 0 512 512'); // Adjust viewBox as per your SVG icon dimensions
    svgIcon.setAttribute('width', '20px'); // max size
    svgIcon.setAttribute('height', '20px'); // max size

    // Create and append SVG path (replace with your SVG path data)
    const svgPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    svgPath.setAttribute('d', 'M233.4 406.6c12.5 12.5 32.8 12.5 45.3 0l192-192c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L256 338.7 86.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l192 192z');
    svgPath.setAttribute('fill', 'currentColor'); // Use current text color as fill
    
    // Append path to SVG element
    svgIcon.appendChild(svgPath);
    
    // Select all <li> elements within <nav>
    const listItems = document.querySelectorAll('nav li');

    // Filter the list items based on the condition (next sibling is also <li> without class)
    const filteredListItems = Array.from(listItems).filter(li => {
        const nextSibling = li.nextElementSibling;
        return nextSibling && nextSibling.tagName === 'LI' && !nextSibling.classList.length;
    });

    // Iterate over each <li> element and prepend the SVG icon
    filteredListItems.forEach(li => {
        const clonedIcon = svgIcon.cloneNode(true); // Clone the SVG icon to avoid multiple references
        li.appendChild(clonedIcon); // Prepend icon to the <li> element
        // toggle visibility
        li.classList.toggle('expanded');
    });
});

// Fix back button cache problem
/*window.onunload = function () { };*/
