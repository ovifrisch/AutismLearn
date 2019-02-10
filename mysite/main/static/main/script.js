var signaturePad
var canvas

function dataURLToBlob(dataURL) {
  // Code taken from https://github.com/ebidel/filer.js
  var parts = dataURL.split(';base64,');
  var contentType = parts[0].split(":")[1];
  var raw = window.atob(parts[1]);
  var rawLength = raw.length;
  var uInt8Array = new Uint8Array(rawLength);

  for (var i = 0; i < rawLength; ++i) {
    uInt8Array[i] = raw.charCodeAt(i);
  }

  return new Blob([uInt8Array], { type: contentType });
}

function download(dataURL, filename) {
  if (navigator.userAgent.indexOf("Safari") > -1 && navigator.userAgent.indexOf("Chrome") === -1) {
    window.open(dataURL);
  } else {
    var blob = dataURLToBlob(dataURL);
    var url = window.URL.createObjectURL(blob);

    var a = document.createElement("a");
    a.style = "display: none";
    a.href = url;
    a.download = filename;

    document.body.appendChild(a);
    a.click();

    window.URL.revokeObjectURL(url);
  }
}

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

  canvas = document.querySelector("canvas");
  signaturePad = new SignaturePad(canvas);
  var wrapper = document.getElementById("signature-pad");
  var saveJPGButton = wrapper.querySelector("[data-action=save-jpg]");
  saveJPGButton.addEventListener("click", function (event) {
    if (signaturePad.isEmpty()) {
      alert("Please provide a signature first.");
    } else {
      var dataURL = signaturePad.toDataURL("image/jpeg");
      download(dataURL, "signature.jpg");
    }
  });
});


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
