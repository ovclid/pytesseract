from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


file_name = r"C:\Users\smba\Desktop\Python\Extract\test.pdf"
pages = convert_from_path(file_name, poppler_path=r'C:\poppler-0.68.0\bin')


for i, page in enumerate(pages):
    page.save(file_name+str(i)+".jpg", "JPEG")


#value = Image.open("가족관계증명서.pdf")
value = Image.open(file_name+str(0)+".jpg")
text = pytesseract.image_to_string(value, lang ="kor+eng")
print(text)
