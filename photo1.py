import pytesseract
from PIL import Image
photo1 = pytesseract.image_to_string(Image.open('photo1.jpg'),lang='chi_sim')
print(photo1)
