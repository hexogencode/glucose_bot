import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pytesseract


def glucose_check():
    filename = 'Image.png'
    x = 1

    while True:
        screen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2))) #Using catch_coords.py find x and y of screen
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        if x == 2:
            cv2.destroyAllWindows()
            break

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img).strip()

    value = []
    if len(text) == 2:                      # Sometimes tesseract make mistake (e.g. 67 or 5.7)
        for num in text:
            value.append(num)
        first = value[0]
        second = value[1]
    elif len(text) == 3:
        first, second = text.split('.')
    else:
        first, second = 0, 0

    if second == 'o':                       # Tesseract mistakes
        second = '0'
    elif second == 'a':
        second = '4'

    second = int(second) / 10
    num = float(first) + float(second)
    print(f'Glucose level: {num}')

    return num

glucose_check()

def send_daily_graph():
    filename = 'Graph.png'
    x = 1
    while (True):
        screen = np.array(ImageGrab.grab(bbox=(882, 699, 1628, 1309)))
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        if x == 2:
            cv2.destroyAllWindows()
            break