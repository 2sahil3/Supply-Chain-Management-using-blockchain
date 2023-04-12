import io
import qrcode
from flask import Flask, render_template, Response

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
    return Response(img_bytes, mimetype='image/png')


if _name_ == '_main_':
    app.run(debug=True)
