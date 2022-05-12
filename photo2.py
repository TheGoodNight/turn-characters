import pytesseract
from PIL import Image
photo2 = pytesseract.image_to_string(Image.open('photo2.jpg'),lang='chi_sim')
print(photo2)
