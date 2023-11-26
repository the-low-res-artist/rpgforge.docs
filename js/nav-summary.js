"use strict";

// Fix back button cache problem
window.onunload = function () { };

(function sections() {
    var buttonSectionInstallation = document.getElementById('button-installation');
    var chaptersSectionInstallation = document.getElementById('li-installation');
    var buttonSectionGettingStarted = document.getElementById('button-getting-started');
    var chaptersSectionGettingStarted = document.getElementById('li-getting-started');
    var buttonSectionUserManual = document.getElementById('button-user-manual');
    var chaptersSectionUserManual = document.getElementById('li-user-manual');
    var buttonSectionCommunity = document.getElementById('button-community');
    var chaptersSectionCommunity = document.getElementById('li-community');


    function showchapters(chapters) {
        chapters.className = "part-title expanded";
    }

    function hidechapters(chapters) {
        chapters.className = "part-title";
    }

    // Installation chapters
    buttonSectionInstallation.addEventListener('click', function () {
        if (chaptersSectionInstallation.className === 'part-title') {
            showchapters(chaptersSectionInstallation);
        } else {
            hidechapters(chaptersSectionInstallation);
        }
    });

    // Getting Started chapters
    buttonSectionGettingStarted.addEventListener('click', function () {
        if (chaptersSectionGettingStarted.className === 'part-title') {
            showchapters(chaptersSectionGettingStarted);
        } else {
            hidechapters(chaptersSectionGettingStarted);
        }
    });

    // User Manual chapters
    buttonSectionUserManual.addEventListener('click', function () {
        if (chaptersSectionUserManual.className === 'part-title') {
            showchapters(chaptersSectionUserManual);
        } else {
            hidechapters(chaptersSectionUserManual);
        }
    });

    // Community chapters
    buttonSectionCommunity.addEventListener('click', function () {
        if (chaptersSectionCommunity.className === 'part-title') {
            showchapters(chaptersSectionCommunity);
        } else {
            hidechapters(chaptersSectionCommunity);
        }
    });
})();
