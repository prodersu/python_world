import cv2
import numpy as np

square = np.zeros((500, 500, 3), dtype='uint8')

# green square
# square[50:450, 50:450] = 0, 200, 0
# square[60:440, 60:440] = 0, 0, 0

cv2.rectangle(square, (50, 50), (450, 450), (0, 0, 200), 7)

cv2.line(square, (30, 250), (300, 300), (200, 0, 0), 2)

cv2.circle(square, (250, 250), 100, (3, 252, 252), 5)

cv2.putText(square, "Dersu", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)

cv2.imshow('result', square)
cv2.waitKey(0)
