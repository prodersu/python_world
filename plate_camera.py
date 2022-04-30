import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)


def sort_results(text):
    nums = False
    for i in range(len(text)-2):
        if text[i:i+3]:
            nums = True

    if len(text) < 5 and not nums:
        pass
    else:
        print(text)


while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = cv2.CascadeClassifier('cascades/car.xml')
    cars1 = cv2.CascadeClassifier('cascades/car1.xml')
    cars2 = cv2.CascadeClassifier('cascades/car2.xml')

    var1 = cars.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(25, 25))
    var2 = cars.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(25, 25))
    var3 = cars.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(25, 25))

    variants = [var1, var2, var3]
    results = None
    for res in variants:
        if res is None:
            pass
        else:
            results = res

    if results is None:
        cv2.imshow('Camera', img)
    else:
        result = None
        for (x, y, w, h) in results:
            result = img[y:y + h, x:x + w]
            cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 0, 255), 2)
        if result is None:
            cv2.imshow('Camera', img)
        else:
            cv2.imshow('Camera', img)
            res_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
            res_blur = cv2.bilateralFilter(res_gray, 5, 90, 90)
            unknown_text = pytesseract.image_to_string(res_blur, lang="eng")
            sort_results(unknown_text)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
