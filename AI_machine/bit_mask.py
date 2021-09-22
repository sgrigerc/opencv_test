import cv2
import numpy as np

# img = cv2.imread('images/siski.jpg')
photo = cv2.imread('images/shopa.jpg')
img = np.zeros(photo.shape[:2], dtype ='uint8')

#создание круга и квадрата
circle = cv2.circle(img.copy(), (300, 200), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

#побитоввые операции
img = cv2.bitwise_and(photo, photo, mask= circle)  #находить одинаковые части и они отображаются
#img = cv2.bitwise_or(circle, square)    #объединяет все фигуры
#img = cv2.bitwise_xor(circle, square)   #все что совпадает не отображается
#img = cv2.bitwise_not(circle, square)   #инверсия

cv2.imshow('Result', img)
cv2.waitKey(0)