# PaddleOCR Web Application

This project is a simple web application that allows users to upload an image and extract text from it using PaddleOCR. The web application is built with Flask and uses Bootstrap for styling.

## Features

- Upload an image (PNG, JPG, JPEG)
- Display the uploaded image
- Detect and extract text from the image using PaddleOCR
- Display the extracted text

## Prerequisites

- Python 3.10 or later
- pip (Python package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/paddleocr-web-app.git
    cd paddleocr-web-app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` includes the following packages:
    ```text
    Flask==2.0.1
    paddleocr==2.6.1.3
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Open your browser and navigate to**:
    ```
    http://127.0.0.1:5000/
    ```


## Usage

1. **Upload an image**:
   - Click the "Choose image" button and select an image file (PNG, JPG, JPEG).
   - Click the "Upload" button.

2. **View the uploaded image**:
   - The uploaded image will be displayed on the page.

3. **Detect text**:
   - Click the "Detect" button to extract text from the uploaded image.
   - The extracted text will be displayed below the image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for the OCR engine.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bootstrap](https://getbootstrap.com/) for the UI components.

