from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_name = '2.jpg'
value = Image.open(image_name)

"""
image = cv2.imread(image_name)

value = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
value = cv2.threshold(value, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
value = cv2.medianBlur(image, 10)
"""

text = pytesseract.image_to_string(value, lang ="kor+eng")
print(text)

