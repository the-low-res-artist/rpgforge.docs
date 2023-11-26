function toggle_section(element) {
    var item = element.parentNode; // get the parent 'li' element
    if (item.className === "part-title") {
    	section.className = "part-title expanded";
    } else {
    	section.className = "part-title";
    }
};