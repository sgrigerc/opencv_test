import cv2
#преобразовть видео в чб и эффект размытия
cap = cv2.VideoCapture("videos/Road.mp4")

while True:
	success, img = cap.read()
	img = cv2.GaussianBlur(img, (19, 19), 0)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Result', img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break