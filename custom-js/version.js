"use strict";

// Fix back button cache problem
window.onunload = function () { };

(function versions() {
    var html = document.querySelector('html');
    var versionToggleButton = document.getElementById('version-toggle');
    var versionPopup = document.getElementById('version-list');
    var versionColorMetaTag = document.querySelector('meta[name="version-color"]');
    var stylesheets = {
        ayuHighlight: document.querySelector("[href$='ayu-highlight.css']"),
        tomorrowNight: document.querySelector("[href$='tomorrow-night.css']"),
        highlight: document.querySelector("[href$='highlight.css']"),
    };

    function showversions() {
        versionPopup.style.display = 'block';
        versionToggleButton.setAttribute('aria-expanded', true);
        /*versionPopup.querySelector("button#" + get_version()).focus();*/
    }

    function hideversions() {
        versionPopup.style.display = 'none';
        versionToggleButton.setAttribute('aria-expanded', false);
        versionToggleButton.focus();
    }

    function get_version() {
        var version;
        try { version = localStorage.getItem('mdbook-version'); } catch (e) { }
        if (version === null || version === undefined) {
            return "latest";
        } else {
            return version;
        }
    }

    // Set version
    var version = get_version();

    /*set_version(version, false);*/

    versionToggleButton.addEventListener('click', function () {
        if (versionPopup.style.display === 'block') {
            hideversions();
        } else {
            showversions();
        }
    });

    versionPopup.addEventListener('click', function (e) {
        var version;
        if (e.target.parentElement.parentElement.id === "version-list") {
            version = e.target.id;
        } else {
            return;
        }

        /* safe exit*/
        if (version == ""){
            return
        }

        var current_location = window.location
        var new_location = current_location
        console.log("current location : " + current_location)
        console.log("new location : " + new_location)
        console.log("(work in progress) switching to documentation v" + version);
 
        /*window.location.href = new_location;*/
    });

    versionPopup.addEventListener('focusout', function(e) {
        // e.relatedTarget is null in Safari and Firefox on macOS (see workaround below)
        if (!!e.relatedTarget && !versionToggleButton.contains(e.relatedTarget) && !versionPopup.contains(e.relatedTarget)) {
            hideversions();
        }
    });

    // Should not be needed, but it works around an issue on macOS & iOS: https://github.com/rust-lang/mdBook/issues/628
    document.addEventListener('click', function(e) {
        if (versionPopup.style.display === 'block' && !versionToggleButton.contains(e.target) && !versionPopup.contains(e.target)) {
            hideversions();
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) { return; }
        if (!versionPopup.contains(e.target)) { return; }

        switch (e.key) {
            case 'Escape':
                e.preventDefault();
                hideversions();
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
                versionPopup.querySelector('li:first-child button').focus();
                break;
            case 'End':
                e.preventDefault();
                versionPopup.querySelector('li:last-child button').focus();
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