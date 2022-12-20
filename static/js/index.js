var url = document.getElementById('url')
var text = document.getElementById('text')
var mail = document.getElementById('mail')
var whatsapp = document.getElementById('whatsapp')
var telephone = document.getElementById('telephone')
var sms = document.getElementById('sms')
var wifi = document.getElementById('wifi')
var QRCodeFromLogo  = document.getElementById('QRCodeFromLogo')

var currentShow = text

function showUrl(){
    prev = currentShow
    prev.style.display="none"
    url.style.display ="block"
    currentShow = url
}

function showText(){
    prev = currentShow
    prev.style.display ="none"
    text.style.display="block"
    currentShow = text
}

function showMail(){
    prev = currentShow
    prev.style.display ="none"
    mail.style.display="block"
    currentShow = mail
}

function showWhatsapp(){
    prev = currentShow
    prev.style.display ="none"
    whatsapp.style.display="block"
    currentShow = whatsapp
}

function showTelephone(){
    prev = currentShow
    prev.style.display ="none"
    telephone.style.display = "block"
    currentShow = telephone
}

function showSms(){
    prev = currentShow
    prev.style.display ="none"
    sms.style.display = "block"
    currentShow = sms
}

function showWifi(){
    prev = currentShow
    prev.style.display ="none"
    wifi.style.display = "block"
    currentShow = wifi
}

function showQRCodeFromLogo(){
    prev = currentShow
    prev.style.display ="none"
    QRCodeFromLogo.style.display = "block"
    currentShow = QRCodeFromLogo
}