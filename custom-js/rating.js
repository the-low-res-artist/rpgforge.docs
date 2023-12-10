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
        rate(1);
    });

    button_start_2.addEventListener('click', function () {
        rate(2);
    });

    button_start_3.addEventListener('click', function () {
        rate(3);
    });

    button_start_4.addEventListener('click', function () {
        rate(4);
    });

    button_start_5.addEventListener('click', function () {
        rate(5);
    });

    function rate(rate) {
        var path = window.location.pathname;
        var page = path.split("/").pop();

        console.log("update page")
        // hide stars
        document.getElementById("full-stars-example-two").style.display = 'none';
        // show "thank you" message
        document.getElementById("thank-you").style.display = 'block';
        
        // send the post request
        console.log("send request")
        const url = `https://rpgpowerforge.com/rate/rate.php?page=${page}&rate=${rate}`;

        fetch(url)
        /*.then(response => {
            if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json(); // Assuming the server returns JSON
        })
        .then(data => {
            console.log('Response from server:', data);
            // Process the data as needed
        })*/
        .catch(error => {
            console.error('Error:', error);
        });
    }    
})();
