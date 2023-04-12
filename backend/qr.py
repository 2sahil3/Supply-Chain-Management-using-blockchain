import io
import qrcode
from flask import Flask, render_template, Response
import base64

app = Flask(_name_)


@app.route('/')
def index():
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data('0')
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Convert the image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # Return the image as a response
    return render_template('index.html')


@app.route('/generate_qr')
def generate_qr():
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data('https://www.example.com')
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Convert the image to HTML
    img_html = io.BytesIO()
    img.save(img_html, format='PNG')
    img_html.seek(0)
    img_html_base64 = base64.b64encode(img_html.getvalue()).decode()

    # Return the image as HTML
    return f'<html><body><img src="data:image/png;base64,{img_html_base64}" alt="QR Code"></body></html>'


if _name_ == '_main_':
    app.run(debug=True)
    
    
