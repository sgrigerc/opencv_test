import cv2

imd = cv2.imread('images/people_2.jpg')
img = cv2.cvtColor(imd, cv2.COLOR_BAYER_BG2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

result = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=4) #   2 размер лица, 3 количество лиц

for (x, y, w, h) in result:
    cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0, 255), thickness= 3)

cv2.imshow('Result', cv2.cvtColor(imd, cv2.COLOR_GRAY2BGR))
cv2.waitKey(0)
