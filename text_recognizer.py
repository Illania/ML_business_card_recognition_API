import pytesseract

pytesseract.pytesseract.tesseract_cmd = ( r"/usr/bin/tesseract" )

# For running on MacOS change change this line to:
# pytesseract.pytesseract.tesseract_cmd = ( r'/usr/local/bin/tesseract' )


def get_text(image):
    return pytesseract.image_to_string(image)
