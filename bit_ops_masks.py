import cv2
import numpy as np

img = np.zeros((350, 350), dtype='uint8')
photo = cv2.imread("images/joji.jpg")
new_img = np.zeros(photo.shape[:2], dtype='uint8')


circle = cv2.circle(new_img.copy(), (320, 180), 180, 255, -1)
square = cv2.rectangle(new_img.copy(), (125, 125), (200, 200), 255, -1)

# ТОЛЬКО ОБЩИЕ МЕСТА
# img = cv2.bitwise_and(square, circle)

# ПОЛНОЕ ОБЪЕДИНЕНИЕ
# img = cv2.bitwise_or(square, circle)

# ВСЕ МЕСТА КРОМЕ ОБЩИХ
# img = cv2.bitwise_xor(circle, square)

# ИНВЕРСИЯ
# img = cv2.bitwise_not(circle)

new_img = cv2.bitwise_and(photo, photo, mask=circle)
cv2.imshow("Result", new_img)
cv2.waitKey(0)
