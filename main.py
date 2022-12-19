from flask import Flask, render_template, request
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask
from PIL import Image

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


# Route for Index Page
@app.route('/')
def showQRForm():
    return render_template('index.html')


# Function to generate Plain QR Code
@app.route('/plainQRCode', methods = ['POST'])
def generatePlainQRCode():
    input = request.form['input']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    
    img = generateQRImage(input,qrColor,qrBgColor)
    img.save("./static/plainQrCode.png")
    return render_template('showQR.html', image = 'plainQrCode.png')


# Function to generate QR Code from Picture/Logo
@app.route('/QRCodeFromLogo', methods = ['POST'])
def generateQRCodeFromLogo():
    input = request.form['input']
    picture  = request.files['picture']

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


# Function to generate QR Code With Logo
@app.route('/QRCodeWithLogo', methods = ['POST'])
def generateQRCodeWithLogo():
    input = request.form['input']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']

    logo = Image.open(picture)
   
    basewidth = 50
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

    img = generateQRImage(input,qrColor,qrBgColor)

    pos = ( (img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)
    img.save('./static/QRCodeWithLogo.png')
    return render_template('showQR.html', image = 'QRCodeWithLogo.png')


if __name__ == '__main__':
   app.run(debug=True)