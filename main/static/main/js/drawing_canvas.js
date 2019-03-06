var signaturePad
var canvas

$(document).ready(function(){
	canvas = document.querySelector("canvas");
	if (canvas != null) {
		signaturePad = new SignaturePad(canvas);
	}
})

function clearIm() {
	signaturePad.clear();
}


function submitIm() {
	image = signaturePad.toDataURL("image/jpeg");
	$.ajax({
		method: "POST",
		url: "/button_check/",
		data: {
			 imgBase64: image
		}
	}).done(function(o) {
		console.log('saved');
	});
	signaturePad.clear();
}
