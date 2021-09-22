import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread('images/number_1.jpg')

gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



pl.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
pl.show()