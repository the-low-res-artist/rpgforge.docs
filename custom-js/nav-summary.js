"use strict";

// Fix back button cache problem
window.onunload = function () { };

(function sections() {
    var buttonSectionInstallation = document.getElementById('button-installation');
    var buttonSectionGettingStarted = document.getElementById('button-getting-started');
    var buttonSectionUserManual = document.getElementById('button-user-manual');
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
})();
