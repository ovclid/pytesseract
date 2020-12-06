from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

value = Image.open("2.jpg")
text = pytesseract.image_to_string(value, lang ="kor+eng")
print(text)

