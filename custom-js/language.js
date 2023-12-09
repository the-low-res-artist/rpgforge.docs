"use strict";

// Fix back button cache problem
window.onunload = function () { };

(function languages() {
    var html = document.querySelector('html');
    var languageToggleButton = document.getElementById('language-toggle');
    var languagePopup = document.getElementById('language-list');
    var languageColorMetaTag = document.querySelector('meta[name="language-color"]');
    var stylesheets = {
        ayuHighlight: document.querySelector("[href$='ayu-highlight.css']"),
        tomorrowNight: document.querySelector("[href$='tomorrow-night.css']"),
        highlight: document.querySelector("[href$='highlight.css']"),
    };

    function showlanguages() {
        languagePopup.style.display = 'block';
        languageToggleButton.setAttribute('aria-expanded', true);
        /*languagePopup.querySelector("button#" + get_language()).focus();*/
    }

    function hidelanguages() {
        languagePopup.style.display = 'none';
        languageToggleButton.setAttribute('aria-expanded', false);
        languageToggleButton.focus();
    }

    function get_language() {
        var language;
        try { language = localStorage.getItem('mdbook-language'); } catch (e) { }
        if (language === null || language === undefined) {
            return "latest";
        } else {
            return language;
        }
    }

    /*function set_language(language, store = true) {
        let ace_language;

        if (language == 'coal' || language == 'navy') {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = false;
            stylesheets.highlight.disabled = true;

            ace_language = "ace/language/tomorrow_night";
        } else if (language == 'ayu') {
            stylesheets.ayuHighlight.disabled = false;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = true;
            ace_language = "ace/language/tomorrow_night";
        } else {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = false;
            ace_language = "ace/language/dawn";
        }

        setTimeout(function () {
            languageColorMetaTag.content = getComputedStyle(document.body).backgroundColor;
        }, 1);

        if (window.ace && window.editors) {
            window.editors.forEach(function (editor) {
                editor.setlanguage(ace_language);
            });
        }

        var previouslanguage = get_language();

        if (store) {
            try { localStorage.setItem('mdbook-language', language); } catch (e) { }
        }

        html.classList.remove(previouslanguage);
        html.classList.add(language);
    }*/

    // Set language
    var language = get_language();

    /*set_language(language, false);*/

    languageToggleButton.addEventListener('click', function () {
        if (languagePopup.style.display === 'block') {
            hidelanguages();
        } else {
            showlanguages();
        }
    });

    languagePopup.addEventListener('click', function (e) {
        var language;
        if (e.target.parentElement.parentElement.id === "language-list") {
            language = e.target.id;
        } else {
            return;
        }

        /* safe exit*/
        if (language == ""){
            return
        }

        var current_location = window.location
        var new_location = current_location
        console.log("current location : " + current_location)
        console.log("new location : " + new_location)
        console.log("(work in progress) switching to documentation v" + language);
 
        /*window.location.href = new_location;*/
    });

    languagePopup.addEventListener('focusout', function(e) {
        // e.relatedTarget is null in Safari and Firefox on macOS (see workaround below)
        if (!!e.relatedTarget && !languageToggleButton.contains(e.relatedTarget) && !languagePopup.contains(e.relatedTarget)) {
            hidelanguages();
        }
    });

    // Should not be needed, but it works around an issue on macOS & iOS: https://github.com/rust-lang/mdBook/issues/628
    document.addEventListener('click', function(e) {
        if (languagePopup.style.display === 'block' && !languageToggleButton.contains(e.target) && !languagePopup.contains(e.target)) {
            hidelanguages();
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) { return; }
        if (!languagePopup.contains(e.target)) { return; }

        switch (e.key) {
            case 'Escape':
                e.preventDefault();
                hidelanguages();
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
                languagePopup.querySelector('li:first-child button').focus();
                break;
            case 'End':
                e.preventDefault();
                languagePopup.querySelector('li:last-child button').focus();
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