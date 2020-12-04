from PIL import Image
import pytesseract

value = Image.open("1.jpg")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(value, lang ="kor+eng")
print(text)
