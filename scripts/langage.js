"use strict";

// Fix back button cache problem
window.onunload = function () { };

(function langages() {
    var html = document.querySelector('html');
    var langageToggleButton = document.getElementById('langage-toggle');
    var langagePopup = document.getElementById('langage-list');
    var langageColorMetaTag = document.querySelector('meta[name="langage-color"]');
    var stylesheets = {
        ayuHighlight: document.querySelector("[href$='ayu-highlight.css']"),
        tomorrowNight: document.querySelector("[href$='tomorrow-night.css']"),
        highlight: document.querySelector("[href$='highlight.css']"),
    };

    function showlangages() {
        langagePopup.style.display = 'block';
        langageToggleButton.setAttribute('aria-expanded', true);
        /*langagePopup.querySelector("button#" + get_langage()).focus();*/
    }

    function hidelangages() {
        langagePopup.style.display = 'none';
        langageToggleButton.setAttribute('aria-expanded', false);
        langageToggleButton.focus();
    }

    function get_langage() {
        var langage;
        try { langage = localStorage.getItem('mdbook-langage'); } catch (e) { }
        if (langage === null || langage === undefined) {
            return "latest";
        } else {
            return langage;
        }
    }

    /*function set_langage(langage, store = true) {
        let ace_langage;

        if (langage == 'coal' || langage == 'navy') {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = false;
            stylesheets.highlight.disabled = true;

            ace_langage = "ace/langage/tomorrow_night";
        } else if (langage == 'ayu') {
            stylesheets.ayuHighlight.disabled = false;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = true;
            ace_langage = "ace/langage/tomorrow_night";
        } else {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = false;
            ace_langage = "ace/langage/dawn";
        }

        setTimeout(function () {
            langageColorMetaTag.content = getComputedStyle(document.body).backgroundColor;
        }, 1);

        if (window.ace && window.editors) {
            window.editors.forEach(function (editor) {
                editor.setlangage(ace_langage);
            });
        }

        var previouslangage = get_langage();

        if (store) {
            try { localStorage.setItem('mdbook-langage', langage); } catch (e) { }
        }

        html.classList.remove(previouslangage);
        html.classList.add(langage);
    }*/

    // Set langage
    var langage = get_langage();

    /*set_langage(langage, false);*/

    langageToggleButton.addEventListener('click', function () {
        if (langagePopup.style.display === 'block') {
            hidelangages();
        } else {
            showlangages();
        }
    });

    langagePopup.addEventListener('click', function (e) {
        var langage;
        if (e.target.parentElement.parentElement.id === "langage-list") {
            langage = e.target.id;
        } else {
            return;
        }

        /* safe exit*/
        if (langage == ""){
            return
        }

        var current_location = window.location
        var new_location = current_location
        console.log("current location : " + current_location)
        console.log("new location : " + new_location)
        console.log("(work in progress) switching to documentation v" + langage);
 
        /*window.location.href = new_location;*/
    });

    langagePopup.addEventListener('focusout', function(e) {
        // e.relatedTarget is null in Safari and Firefox on macOS (see workaround below)
        if (!!e.relatedTarget && !langageToggleButton.contains(e.relatedTarget) && !langagePopup.contains(e.relatedTarget)) {
            hidelangages();
        }
    });

    // Should not be needed, but it works around an issue on macOS & iOS: https://github.com/rust-lang/mdBook/issues/628
    document.addEventListener('click', function(e) {
        if (langagePopup.style.display === 'block' && !langageToggleButton.contains(e.target) && !langagePopup.contains(e.target)) {
            hidelangages();
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) { return; }
        if (!langagePopup.contains(e.target)) { return; }

        switch (e.key) {
            case 'Escape':
                e.preventDefault();
                hidelangages();
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
                langagePopup.querySelector('li:first-child button').focus();
                break;
            case 'End':
                e.preventDefault();
                langagePopup.querySelector('li:last-child button').focus();
                break;
        }
    });
})();

function LinkCheck(url)
{
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status!=404;
}