import cv2
import imutils
import easyocr

img = cv2.imread("images/black_plate.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)

edges = cv2.Canny(img_filter, 170, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)

contour_with_license_plate = None
license_plate = None
x = None
y = None
w = None
h = None


def is_number(licence_plate):
    text = easyocr.Reader(['en'])
    text = text.readtext(license_plate)
    for i in text:
        for j in i:
            if isinstance(j, str):
                print(j)
                return True
    return False


for c in cont:
    approx = cv2.approxPolyDP(c, 10, True)
    if len(approx) == 4:
        contour_with_license_plate = approx
        x, y, w, h = cv2.boundingRect(c)
        license_plate = gray[y:y + h, x:x + w]
        if is_number(licence_plate=license_plate):
            print("")


final_image = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("result", final_image)
cv2.waitKey(0)
