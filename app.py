from flask import Flask, render_template, request, redirect, url_for
from paddleocr import PaddleOCR
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Function to initialize PaddleOCR within the request context
def get_ocr():
    return PaddleOCR(use_angle_cls=True, lang='en')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return render_template('index.html', filename=filename)
    return redirect(request.url)

@app.route('/detect', methods=['POST'])
def detect_text():
    filename = request.form ['filename']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Initialize OCR within the request context
    ocr = get_ocr()

    # Perform OCR
    result = ocr.ocr(filepath, cls=True)

    # Extract text from OCR result
    extracted_text = '\n'.join([line[1][0] for line in result[0]])

    return render_template('index.html', filename=filename, text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
