import cv2
import numpy as np
import imutils
from imutils.perspective import four_point_transform


def find_card_contour(pil_image):
    """
    Finds all rectangle contours, grabs the largest one with 4 vertices and
    assumes it is the business card's contour, if the contour is not found returns the original image.
    """
    original_image = np.array(pil_image)
    image = original_image.copy()
    image = imutils.resize(image, width=600)
    ratio = original_image.shape[1] / float(image.shape[1])
    contours = __get_contours(image)
    card_contour = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(approx) == 4:
            card_contour = approx
            break
    if card_contour is None:
        return original_image
    card = four_point_transform(original_image, card_contour.reshape(4, 2) * ratio)
    card_rgb = cv2.cvtColor(card, cv2.COLOR_BGR2RGB)
    return card_rgb


def __get_contours(image):
    """ Converts the image to grayscale, blurs it, and applies edge detection
    to find the contours, sorts them by size (in descending order), and grabs the largest contours.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
    return contours
