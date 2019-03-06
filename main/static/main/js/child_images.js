$(document).ready(function(){
	$(".image_sel").click(function() {
		$(this).hide();
		interest = $(this).attr('id')
		console.log(interest)
		$.ajax({
			method: "POST",
			url: "/add_interest/",
			data: {
				 interest: interest
			}
		}).done(function(o) {
			console.log('saved');
		});
	})
});
