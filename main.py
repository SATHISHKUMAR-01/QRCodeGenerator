from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import qrcode


app = Flask(__name__)

@app.route('/')
def showQRForm():
    return render_template('index.html')

@app.route('/plainQRCode', methods = ['POST'])
def generatePlainQRCode():
    input = request.form['input']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
    )

    qr.add_data(input)
    qr.make(fit=True)
    img = qr.make_image(fill_color=qrColor, back_color=qrBgColor)
    img.save("plainQrCode.png")
    return "created"

@app.route('/QRCodeFromLogo', methods = ['POST'])
def generateQRCodeFromLogo():
    input = request.form['input']
    picture  = request.files['picture']
    print(picture)
 
    return "createdLogo"

@app.route('/QRCodeWithLogo', methods = ['POST'])
def generateQRCodeWithLogo():
    input = request.form['input']
    qrColor = request.form['qrColor']
    qrBgColor = request.form['qrBgColor']
    picture  = request.files['picture']
    print(picture)
 
    return "createdWithLogo"

if __name__ == '__main__':
   app.run(debug=True)