import cv2
import easyocr

# Read the image file
image = cv2.imread('images/car1.jpeg')
# Convert to Grayscale Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny Edge Detection
canny_edge = cv2.Canny(gray_image, 170, 200)

# Find contours based on Edges
contours, new = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

# Initialize license Plate contour and x,y coordinates
contour_with_license_plate = None
license_plate = None
x = None
y = None
w = None
h = None


def text_recognize(crop):
    text = easyocr.Reader(['en'])
    text = text.readtext(crop)
    res = ''
    for i in text:
        for j in i:
            if isinstance(j, str):
                res = j
                break
    return res


# Find the contour with 4 potential corners and creat ROI around it
for contour in contours:
    # Find Perimeter of contour and it should be a closed contour
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
    if len(approx) == 4:  # see whether it is a Rect
        contour_with_license_plate = approx
        x, y, w, h = cv2.boundingRect(contour)
        license_plate = gray_image[y:y + h, x:x + w]
        text = text_recognize(license_plate)
        if len(text) > 0:
            print(text)
            break


# Draw License Plate and write the Text
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imshow("License Plate Detection", image)
cv2.waitKey(0)



