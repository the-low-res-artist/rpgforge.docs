"use strict";

// Fix back button cache problem
window.onunload = function () { };

(function rating() {
    var button_start_1 = document.getElementById('rating3-1');
    var button_start_2 = document.getElementById('rating3-2');
    var button_start_3 = document.getElementById('rating3-3');
    var button_start_4 = document.getElementById('rating3-4');
    var button_start_5 = document.getElementById('rating3-5');

    button_start_1.addEventListener('click', function () {
        rate("1 star");
    });

    button_start_2.addEventListener('click', function () {
        rate("2 star");
    });

    button_start_3.addEventListener('click', function () {
        rate("3 star");
    });

    button_start_4.addEventListener('click', function () {
        rate("4 star");
    });

    button_start_5.addEventListener('click', function () {
        rate("5 star");
    });

    function rate(score) {
        var path = window.location.pathname;
        console.log(path);
        console.log(score);
        // hide stars
        document.getElementById("full-stars-example-two").style.visibility = 'hidden';
        // show "thank you" message
        document.getElementById("thank-you").style.visibility = 'visible';
    }
})();
