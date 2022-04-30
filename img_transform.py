import cv2
import numpy as np

img = cv2.imread("images/joji.jpg")

height, width = img.shape[:2]
point = (width // 2, height // 2)

new_img = np.zeros(img.shape, dtype='uint8')


def rotate(img_param, angle):
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (width, height))


def offset(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (width, height))


# img = rotate(img, -90)
# img = offset(img, 50, 100)

# СЕРЫЙ ТОН
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# РАЗМЫТИЕ
img = cv2.GaussianBlur(img, (5, 5), 0)
# КОНТУРЫ ИЗОБРАЖЕНИЯ
img = cv2.Canny(img, 20, 20)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, con, -1, (220, 150, 50), 1)


cv2.imshow("Result", new_img)

cv2.waitKey(0)
