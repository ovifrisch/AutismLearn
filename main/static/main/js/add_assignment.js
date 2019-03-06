num_questions = 0

$(document).ready(function(){

})


function add_question() {
	num_questions = num_questions + 1
	html = $(".question_template").html()
	$("#questions").append(html)
}
