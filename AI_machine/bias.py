import cv2
import numpy as np

#bais поворот картинки
img = cv2.imread('images/ai_cat.jpg')

def rotate (img_param, angle):
    height, wight = img_param.shape[:2]
    point = (wight // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (wight, height))

img = rotate(img, 45)

cv2.imshow('Result', img)
cv2.waitKeyEx(0)