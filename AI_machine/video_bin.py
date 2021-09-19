import cv2
import numpy as np

# img = cv2.imread('images/OpenCV.jpg')
# cv2.imshow('Result', img)
#
# cv2.waitKey(0)

cap = cv2.VideoCapture('videos/ashaley.mp4')
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()

    img = np.zeros(img.shape, dtype='uint8')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)  # Blur
    img = cv2.Canny(img, 30, 30)

    kernel = np.ones((5, 5), np.uint8)

    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
    # img = cv2.flip(img, 1)  #mirror зеркало

    con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, con, -1, (189, 21, 105), 1)
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break