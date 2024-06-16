"use strict";

document.addEventListener('DOMContentLoaded', function() {
    // Add a click event listener to the <nav> element
    document.querySelector('nav').addEventListener('click', function(event) {
        // Check if the clicked element parent is an <li> with the desired classes
        var parent = event.target.parentElement
        if (parent.tagName === 'LI' && 
            (parent.classList.contains('chapter-item') || 
            parent.classList.contains('part-title'))) {
            // Toggle the 'expanded' class on the clicked <li>
            parent.classList.toggle('expanded');
        }
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
