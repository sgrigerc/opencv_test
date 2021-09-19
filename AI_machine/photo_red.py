import cv2
import numpy as np

img = cv2.imread('images/shopa.jpg')

img = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 3))
img = cv2.GaussianBlur(img, (9, 9), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 40, 40)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

# img[0:100, 0:150]
cv2.imshow('Result', img)

# print(img.shape)

cv2.waitKey(0)