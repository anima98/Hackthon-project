import pytesseract
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    print(2)
    return('alen')