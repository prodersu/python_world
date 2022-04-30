import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('faces.xml')

    results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
