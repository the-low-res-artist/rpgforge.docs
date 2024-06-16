"use strict";

document.addEventListener('DOMContentLoaded', function() {
    // Add a click event listener to the <nav> element
    document.querySelector('nav').addEventListener('click', function(event) {
        // Check if the clicked element parent is an <li> with the desired classes
        var parent = event.target.parentElement
        if (event.target.tagName == 'SVG' && 
            parent.tagName === 'LI' && 
            (parent.classList.contains('chapter-item') || 
            parent.classList.contains('part-title'))) {
            // Toggle the 'expanded' class on the clicked <li>
            parent.classList.toggle('expanded');
        }
    });
});

// JavaScript to add an SVG icon to each <li> element
document.addEventListener('DOMContentLoaded', function() {
    // Create an SVG element
    const svgIcon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svgIcon.setAttribute('class', 'icon');
    svgIcon.setAttribute('viewBox', '0 0 512 512'); // Adjust viewBox as per your SVG icon dimensions
    svgIcon.setAttribute('width', '26'); // max size

    // Create and append SVG path (replace with your SVG path data)
    const svgPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    svgPath.setAttribute('d', 'M233.4 406.6c12.5 12.5 32.8 12.5 45.3 0l192-192c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L256 338.7 86.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l192 192z');
    svgPath.setAttribute('fill', 'currentColor'); // Use current text color as fill
    
    // Append path to SVG element
    svgIcon.appendChild(svgPath);
    
    // Select all <li> elements within <nav>
    const listItems = document.querySelectorAll('nav li.chapter-item');

    // Iterate over each <li> element and prepend the SVG icon
    listItems.forEach(li => {
        const clonedIcon = svgIcon.cloneNode(true); // Clone the SVG icon to avoid multiple references
        li.appendChild(clonedIcon); // Prepend icon to the <li> element
    });
});

// Fix back button cache problem
/*window.onunload = function () { };

(function sections() {
    var buttonSectionInstallation = document.getElementById('button-installation');
    var buttonSectionGettingStarted = document.getElementById('button-getting-started');
    var buttonSectionUserManual = document.getElementById('button-user-manual');
    var buttonSectionApiDocumentation = document.getElementById('button-api-documentation');
    var buttonSectionCommunity = document.getElementById('button-community');
    var buttonSectionAbout = document.getElementById('button-about');


    function showchapters(chapters, chevron) {
        chapters.className = "part-title expanded";
        chevron.className = "fa fa-chevron-down";
    }

    function hidechapters(chapters, chevron) {
        chapters.className = "part-title";
        chevron.className = "fa fa-chevron-right";
    }

    // Installation chapters
    buttonSectionInstallation.addEventListener('click', function () {
        var chapter = buttonSectionInstallation.parentNode;
        var chevron = document.getElementById('chevron-installation');
        if (chapter.className === 'part-title') {
            showchapters(chapter, chevron);
        } else {
            hidechapters(chapter, chevron);
        }
    });

    // Getting Started chapters
    buttonSectionGettingStarted.addEventListener('click', function () {
        var chapter=buttonSectionGettingStarted.parentNode;
        var chevron = document.getElementById('chevron-getting-started');
        if (chapter.className === 'part-title') {
            showchapters(chapter, chevron);
        } else {
            hidechapters(chapter, chevron);
        }
    });

    // User Manual chapters
    buttonSectionUserManual.addEventListener('click', function () {
        var chapter=buttonSectionUserManual.parentNode;
        var chevron = document.getElementById('chevron-user-manual');
        if (chapter.className === 'part-title') {
            showchapters(chapter, chevron);
        } else {
            hidechapters(chapter, chevron);
        }
    });

    // API documentation chapters
    buttonSectionApiDocumentation.addEventListener('click', function () {
        var chapter=buttonSectionApiDocumentation.parentNode;
        var chevron = document.getElementById('chevron-api-documentation');
        if (chapter.className === 'part-title') {
            showchapters(chapter, chevron);
        } else {
            hidechapters(chapter, chevron);
        }
    });

    // Community chapters
    buttonSectionCommunity.addEventListener('click', function () {
        var chapter=buttonSectionCommunity.parentNode;
        var chevron = document.getElementById('chevron-community');
        if (chapter.className === 'part-title') {
            showchapters(chapter, chevron);
        } else {
            hidechapters(chapter, chevron);
        }
    });

    // About chapters
    buttonSectionAbout.addEventListener('click', function () {
        var chapter=buttonSectionAbout.parentNode;
        var chevron = document.getElementById('chevron-about');
        if (chapter.className === 'part-title') {
            showchapters(chapter, chevron);
        } else {
            hidechapters(chapter, chevron);
        }
    });
})();*/
