import cv2
import numpy as np
import imutils
from imutils.perspective import four_point_transform

def detect_contours(pil_image):
    # load the input image from disk, resize it, and compute the ratio
    orig = np.array(pil_image) 
    image = orig.copy()
    image = imutils.resize(image, width=600)
    ratio = orig.shape[1] / float(image.shape[1])
    # convert the image to grayscale, blur it, and apply edge detection
    # to reveal the outline of the business card
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    # detect contours in the edge map, sort them by size (in descending order), and grab the largest contours
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5] 
    cardCnt = None
    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if this is the first contour we've encountered that has four
        # vertices, then we can assume we've found the business card
        if len(approx) == 4:
            cardCnt = approx
            break
    # if the business card contour not found return original image
    if cardCnt is None:
        return orig
    
    card = four_point_transform(orig, cardCnt.reshape(4, 2) * ratio)
    card_rgb = cv2.cvtColor(card, cv2.COLOR_BGR2RGB)
    return card_rgb
