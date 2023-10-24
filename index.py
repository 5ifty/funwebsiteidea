from flask import Flask, render_template, request, send_file, redirect, url_for
import sys
import qrcode
from qrcode.image.pure import PyPNGImage
from io import BytesIO

sys.path.append('/')

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('HTML.html')

@app.route('/generate_qr', methods=['GET', 'POST'])
def generate_qr():
    if request.method == 'POST':
        link = request.form.get('link')
        qr = generate_qr_code(link)
        image_path = save_qr_code(qr)
        return redirect(url_for('show_qr', image_path=image_path))
        
    return render_template('basicInput.html')

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

def save_qr_code(qr):
    img_buffer = BytesIO()
    qr.save(img_buffer)
    img_buffer.seek(0)
    temp_filename = 'static/images/temp_qr.png'
    with open(temp_filename, 'wb') as f:
        f.write(img_buffer.read())

    return temp_filename

@app.route('/show_qr/<path:image_path>')
def show_qr(image_path):
    return send_file(image_path, mimetype='image/png')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)