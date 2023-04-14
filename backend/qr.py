import io
import qrcode
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data('0')
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return Response(img_bytes, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)