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
        console.log("1 star")
    });

    button_start_2.addEventListener('click', function () {
        console.log("2 star")
    });

    button_start_3.addEventListener('click', function () {
        console.log("3 star")
    });

    button_start_4.addEventListener('click', function () {
        console.log("4 star")
    });

    button_start_5.addEventListener('click', function () {
        console.log("5 star")
    });
})();
