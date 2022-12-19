var msg_bottom = document.getElementById("msg_bottom");
msg_bottom.style.display = "none";

var msg_top = document.getElementById("msg_top");
msg_top.style.display = "none";

function downloadimage() {
  var container = document.getElementById("qr");
  html2canvas(container, { allowTaint: true }).then(function (canvas) {
    var link = document.createElement("a");
    document.body.appendChild(link);
    link.download = "qr.jpg";
    link.href = canvas.toDataURL("image/png");
    link.target = "_blank";
    link.click();
  });
}

var qr_image = document.getElementById("qr_image");
var qrbackgroundcolor = "white";
var msgbackgroundcolor = "white";
var msgColor = "black";
var msg = "";
var pos = "None";

function getMsg(val) {
  msg = val;
  if (pos == "top") {
    msg_top.style.display = "block";
    msg_top.innerHTML = msg;
    msg_bottom.style.display = "none";
  } else if (pos == "bottom") {
    msg_bottom.style.display = "block";
    msg_bottom.innerHTML = msg;
    msg_top.style.display = "none";
  }
}

function getcolor(val) {
  msgColor = val;
  if (pos == "top") {
    msg_top.style.color = msgColor;
  } else if (pos == "bottom") {
    msg_bottom.style.color = msgColor;
  }
}

function getbgcolorQR(val) {
  qrbackgroundcolor = val;
  qr_image.style.borderTop = "10px solid " + qrbackgroundcolor;
  qr_image.style.borderBottom = "10px solid " + qrbackgroundcolor;
  qr_image.style.borderRight = "10px solid " + qrbackgroundcolor;
  qr_image.style.borderLeft = "10px solid " + qrbackgroundcolor;
}

function getbgcolorMsg(val) {
  msgbackgroundcolor = val;
  if (pos == "top") {
    msg_top.style.backgroundColor = msgbackgroundcolor;
  } else if (pos == "bottom") {
    msg_bottom.style.backgroundColor = msgbackgroundcolor;
  }
}

function getPosition(val) {
  pos = val;
  if (pos == "top") {
    msg_top.style.display = "block";
    msg_top.innerHTML = msg;
    msg_bottom.style.display = "none";
  } else if (pos == "bottom") {
    msg_bottom.style.display = "block";
    msg_bottom.innerHTML = msg;
    msg_top.style.display = "none";
  }
}

function cancel() {
  qrbackgroundcolor = "white";
  getbgcolorQR(qrbackgroundcolor)
  msgbackgroundcolor = "white";
  getbgcolorMsg(msgbackgroundcolor)
  msgColor = "black";
  getcolor(msgColor)
  msg = "";
  getMsg(msg)
  pos = "None";
  getPosition(pos)
}
