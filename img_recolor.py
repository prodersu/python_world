import cv2
import numpy as np

img = cv2.imread("images/joji.jpg")
# RGB to HSV
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# RGB to LAB
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# BGR to RGB
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
b, g, r = cv2.split(img)

img = cv2.merge([b, g, r])

cv2.imshow("Result", img)
cv2.waitKey(0)
