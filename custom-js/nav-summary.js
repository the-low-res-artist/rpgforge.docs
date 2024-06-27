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
    });

    // Iterate over each <li> element and remove expanded class
    listItems.forEach(li => {
        // toggle visibility
        li.classList.remove('expanded');
    });

    // expand only the correct li (parents of current page)
    // Find <a> element with class 'active' descendant of <nav>
    var a_active = document.querySelector('nav a.active');
    // get the li section (grand grand parent)
    var li_section = a_active.parentElement.parentElement.parentElement;
    // iterate until there is no more li grand parent section to open
    while (li_section && li_section.tagName === 'LI') {    
        var li_sibling = li_section.previousElementSibling;
        li_sibling.classList.add("expanded")
        // open chevron
        var svg = li_sibling.querySelector('svg');
        svg.classList.add('nav-svg-rotate-90');
        // next li grand parent
        li_section = li_section.parentElement.parentElement;
    }
});