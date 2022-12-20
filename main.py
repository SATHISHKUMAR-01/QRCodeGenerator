from flask import Flask, render_template, request
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask
from PIL import Image
import wifi_qrcode_generator as wifi

app = Flask(__name__)

# Function to create QR Code
def generateQRImage(input, qrColor, qrBgColor):
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(input)
    qr.make(fit=True)
    img = qr.make_image( fill_color=qrColor, back_color=qrBgColor)
    return img

# Function to add Logo to QR Code
def generateLogo(picture,input,qrColor,qrBgColor):
    logo = Image.open(picture)
    basewidth = 50
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    img = generateQRImage(input,qrColor,qrBgColor)
    pos = ( (img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)
    return img

# Function to save QR code
def save(img,name):
    img.save("./static/"+name)
    return render_template('showQR.html', image = name)

# Route for Index Page
@app.route('/')
def showQRForm():
    return render_template('index.html')

# Function to generate QR Code for text
@app.route('/text', methods = ['POST'])
def generateTextQRCode():
    input = request.form['input']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']
    img = ''
    if(picture.filename != ''):
        img = generateLogo(picture,input,qrColor,qrBgColor)
    else:
        img = generateQRImage(input,qrColor,qrBgColor)
    return save(img,"text.png")


# Function to generate QR Code for URL
@app.route('/url', methods = ['POST'])
def generateUrlQRCodeF():
    input = request.form['input']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']
    img = ''
    if(picture.filename != ''):
        img = generateLogo(picture,input,qrColor,qrBgColor)
    else:
        img = generateQRImage(input,qrColor,qrBgColor)
    return save(img,"url.png")


# Function to generate QR Code for Mail
@app.route('/mail', methods = ['POST'])
def generateMailQRCode():
    mail = request.form['mailId']
    sub = request.form['sub']
    body = request.form['body']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']

    input = "mailto:"+mail+"?subject="+sub+"&body="+body
    
    img = ''
    if(picture.filename != ''):
        img = generateLogo(picture,input,qrColor,qrBgColor)
    else:
        img = generateQRImage(input,qrColor,qrBgColor)
    return save(img,"mail.png")


# Function to generate QR Code for Whatsapp
@app.route('/whatsapp', methods = ['POST'])
def generateWhatsappQRCode():
    whatsappNum = request.form['whatsappNum']
    message = request.form['message']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']

    input = "https://wa.me/+91"+whatsappNum+"?text="+message
    img = ''
    if(picture.filename != ''):
        img = generateLogo(picture,input,qrColor,qrBgColor)
    else:
        img = generateQRImage(input,qrColor,qrBgColor)
    return save(img,"whatsapp.png")


# Function to generate QR Code for Telephone
@app.route('/telephone', methods = ['POST'])
def generateTelephoneQRCode():
    telephoneNum = request.form['telephoneNum']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']

    input = "tel:+91"+telephoneNum
    img = ''
    if(picture.filename != ''):
        img = generateLogo(picture,input,qrColor,qrBgColor)
    else:
        img = generateQRImage(input,qrColor,qrBgColor)
    return save(img,"telephone.png")

# Function to generate QR Code for SMS
@app.route('/sms', methods = ['POST'])
def generateSmsQRCode():
    mobileNum = request.form['mobileNum']
    message = request.form['message']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']

    input = "SMSTO:+91"+mobileNum+":"+message
    img = ''
    if(picture.filename != ''):
        img = generateLogo(picture,input,qrColor,qrBgColor)
    else:
        img = generateQRImage(input,qrColor,qrBgColor)
    return save(img,"sms.png")

# Function to generate QR Code for Wifi
@app.route('/wifi', methods = ['POST'])
def generateWifiQRCode():
    wifiId = request.form['wifiId']
    password = request.form['password']
    img= wifi.wifi_qrcode(wifiId,False,"WPA",password)
    return save(img,"wifi.png")


# Function to generate QR Code from Picture/Logo
@app.route('/QRCodeFromLogo', methods = ['POST'])
def generateQRCodeFromLogo():
    input = request.form['input']
    picture  = request.files['picture']

    print(picture)
    print(input)
    logo = Image.open(picture)
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(input)
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask = ImageColorMask(back_color=(255,255,255), color_mask_image=logo))
    img.save('./static/QRCodeFromLogo.png')
    return render_template('showQR.html', image = 'QRCodeFromLogo.png')


if __name__ == '__main__':
   app.run(debug=True)