$( document ).ready(function() {
	updateScroll();
	$('#clean-layout').stellar();
});

function updateScroll() {
	var $img = $('#event-image-reference');
	var mt = parseInt($img.css('height').replace("px", ""))
	
	var $scrollContainer = $('#clean-layout');
	
	setTimeout(function() {
		//$scrollContainer.scrollTop(mt * 0.8);
		$scrollContainer.animate({
		        scrollTop: mt * 0.8
		    }, 1000);
	}, 100);	
	
} 
