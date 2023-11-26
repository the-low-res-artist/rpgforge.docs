"use strict";

// Fix back button cache problem
window.onunload = function () { };

(function sections() {
    //var html = document.querySelector('html');
    var buttonSectionInstallation = document.getElementById('button-installation');
    var chaptersSectionInstallation = document.getElementById('li-installation');
    //var sectionPopup = document.getElementById('section-list');
    //var sectionColorMetaTag = document.querySelector('meta[name="section-color"]');
    /*var stylesheets = {
        ayuHighlight: document.querySelector("[href$='ayu-highlight.css']"),
        tomorrowNight: document.querySelector("[href$='tomorrow-night.css']"),
        highlight: document.querySelector("[href$='highlight.css']"),
    };*/

    function showsectionInstallation() {
        chaptersSectionInstallation.className = "part-title expanded";
    }

    function hidesectionInstallation() {
        chaptersSectionInstallation.className = "part-title";
    }

    /*function get_section() {
        var section;
        try { section = localStorage.getItem('mdbook-section'); } catch (e) { }
        if (section === null || section === undefined) {
            return "latest";
        } else {
            return section;
        }
    }*/

    /*function set_section(section, store = true) {
        let ace_section;

        if (section == 'coal' || section == 'navy') {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = false;
            stylesheets.highlight.disabled = true;

            ace_section = "ace/section/tomorrow_night";
        } else if (section == 'ayu') {
            stylesheets.ayuHighlight.disabled = false;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = true;
            ace_section = "ace/section/tomorrow_night";
        } else {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = false;
            ace_section = "ace/section/dawn";
        }

        setTimeout(function () {
            sectionColorMetaTag.content = getComputedStyle(document.body).backgroundColor;
        }, 1);

        if (window.ace && window.editors) {
            window.editors.forEach(function (editor) {
                editor.setsection(ace_section);
            });
        }

        var previoussection = get_section();

        if (store) {
            try { localStorage.setItem('mdbook-section', section); } catch (e) { }
        }

        html.classList.remove(previoussection);
        html.classList.add(section);
    }*/

    // Set section
    //var section = get_section();

    /*set_section(section, false);*/

    buttonSectionInstallation.addEventListener('click', function () {
        if (chaptersSectionInstallation.className === 'part-title') {
            showsectionInstallation();
        } else {
            hidesectionInstallation();
        }
    });

    /*sectionPopup.addEventListener('click', function (e) {
        var section;
        if (e.target.parentElement.parentElement.id === "section-list") {
            section = e.target.id;
        } else {
            return;
        }

        /* safe exit
        if (section == ""){
            return
        }

        var current_location = window.location
        var new_location = current_location
        console.log("current location : " + current_location)
        console.log("new location : " + new_location)
        console.log("(work in progress) switching to documentation v" + section);
 
        /*window.location.href = new_location;
    });*/

    /*sectionPopup.addEventListener('focusout', function(e) {
        // e.relatedTarget is null in Safari and Firefox on macOS (see workaround below)
        if (!!e.relatedTarget && !sectionToggleButton.contains(e.relatedTarget) && !sectionPopup.contains(e.relatedTarget)) {
            hidesections();
        }
    });*/

    /*// Should not be needed, but it works around an issue on macOS & iOS: https://github.com/rust-lang/mdBook/issues/628
    document.addEventListener('click', function(e) {
        if (sectionPopup.style.display === 'block' && !sectionToggleButton.contains(e.target) && !sectionPopup.contains(e.target)) {
            hidesections();
        }
    });*/

    /*document.addEventListener('keydown', function (e) {
        if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) { return; }
        if (!sectionPopup.contains(e.target)) { return; }

        switch (e.key) {
            case 'Escape':
                e.preventDefault();
                hidesections();
                break;
            case 'ArrowUp':
                e.preventDefault();
                var li = document.activeElement.parentElement;
                if (li && li.previousElementSibling) {
                    li.previousElementSibling.querySelector('button').focus();
                }
                break;
            case 'ArrowDown':
                e.preventDefault();
                var li = document.activeElement.parentElement;
                if (li && li.nextElementSibling) {
                    li.nextElementSibling.querySelector('button').focus();
                }
                break;
            case 'Home':
                e.preventDefault();
                sectionPopup.querySelector('li:first-child button').focus();
                break;
            case 'End':
                e.preventDefault();
                sectionPopup.querySelector('li:last-child button').focus();
                break;
        }
    });*/
})();

/*function LinkCheck(url)
{
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status!=404;
}*/