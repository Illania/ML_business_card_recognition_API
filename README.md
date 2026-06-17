# Business Card Recognition Project Using OpenCV, Tesseract, and a Pretrained Google BERT Model

This project uses OpenCV, Tesseract OCR, and a pretrained Google BERT model from Hugging Face for extracting contact information from business cards.

**Model used:** dslim/bert-large-NER
https://huggingface.co/dslim/bert-large-NER

---

# Project Structure

```text
ML_business_card_recognition_api/
├── __init__.py                     Module initialization file
├── main.py                         Main API application file
├── test_main.py                    API test file
├── bert_model.py                   BERT model loading module
├── card_recognizer.py              Business card contour detector
├── contact_recognizer.py           Contact information recognizer
├── contact.py                      Contact entity class
├── data/
│   └── jobs                        Text file containing job titles
├── templates/
│   ├── card.html                   Recognition result template
│   └── style.css                   CSS stylesheet
├── uploads/                        Uploaded files directory
├── README.md                       Project documentation
├── requirements.txt                Python dependencies
├── text_recognizer.py              Tesseract OCR text recognizer
├── test_data/
│   └── card.jpg                    Sample business card image
└── token_recognizers/
    ├── __init__.py                 Module initialization file
    ├── email_recognizer.py         Email recognizer
    ├── job_recognizer.py           Job title recognizer
    ├── loc_recognizer.py           Address recognizer (uses BERT)
    ├── name_recognizer.py          Name recognizer (uses BERT)
    ├── org_recognizer.py           Organization recognizer (uses BERT)
    ├── phone_recognizer.py         Phone number recognizer
    └── website_recognizer.py       Website recognizer
```

---

# Description, Installation, and Usage

## 1. Running the Application

The project is implemented as a FastAPI application.

Start the API from the project directory using:

```bash
uvicorn main:api
```

By default, the application runs locally at:

```text
http://127.0.0.1:8080
```

The API documentation is available on the homepage after startup.

---

## 2. Uploading and Processing Business Cards

Images uploaded through the `/upload` endpoint must:

* Be in `.jpg`, `.jpeg`, or `.png` format
* Have sufficiently high resolution

Low-quality images may lead to inaccurate recognition results.

**Note:** The application currently supports business cards written in **English only**.

After uploading an image, recognition results can be viewed through:

```text
/view/{filename}
```

where `filename` is the name of the uploaded file.

---

## 3. Installing Tesseract OCR

Before running the application, install the Tesseract OCR engine.

### Linux

```bash
apt install tesseract-ocr
apt install libtesseract-dev
```

### macOS

```bash
brew install tesseract
```

---

### Configure Tesseract Path

You may need to update the Tesseract executable path in `text_recognizer.py`.

#### Linux

```python
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
```

#### macOS

```python
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
```

The location may differ on your system.

To find the correct path, run:

```bash
which tesseract
```

---

## 4. Installing Python Dependencies

After installing Tesseract, install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 5. Running a Test Recognition

For a quick test, use the:

```text
/test
```

endpoint.

---

## 6. Initial BERT Model Download

The first launch may take a significant amount of time because the pretrained BERT model and its dependencies need to be downloaded.

The total download size is approximately **1.33 GB**, so please be patient and grab a cup of coffee ☕ and a cookie 🍪 while waiting.

---

# Technology Stack

* FastAPI
* OpenCV
* Tesseract OCR
* Hugging Face Transformers
* Google BERT (dslim/bert-large-NER)
* Python

# Features

* Business card detection and extraction
* Optical Character Recognition (OCR)
* Person name recognition
* Company name recognition
* Address recognition
* Job title recognition
* Email extraction
* Phone number extraction
* Website extraction
* REST API interface
* HTML result visualization

# Limitations

* Supports English-language business cards only
* Recognition accuracy depends on image quality
* Initial BERT model download requires approximately 1.33 GB of data

```
```
