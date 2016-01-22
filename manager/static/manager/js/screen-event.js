$( document ).ready(function() {
	updateScroll();
	$('#scroll-layout').stellar();
});

function updateScroll() {
	var $img = $('#event-image-reference');
	var mt = parseInt($img.css('height').replace("px", ""))
	
	var $scrollContainer = $('#scroll-layout');
	
	setTimeout(function() {
		$scrollContainer.animate({
		        scrollTop: mt * 0.8
		    }, 1000);
	}, 100);	
	
} 
