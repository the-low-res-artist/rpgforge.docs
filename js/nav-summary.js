$(".part-title").click(function () {
    $header = $(this);
    if ($header.context.className === "part-title") {
    	$header.context.className = "header expanded";
    } else {
    	$header.context.className = "part-title";
    }
});