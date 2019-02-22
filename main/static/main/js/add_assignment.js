$(document).ready(function(){
  console.log("yo");
})


function add_question() {
  html = $(".question_template").html()
  console.log(html);
  $("#questions").append(html)
}
