import cv2
import warnings

warnings.filterwarnings('ignore')


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
	
	_, img = cap.read()

	gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gs, 1.1, 6)

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 5)



	cv2.imshow('img', img)

	k = cv2.waitKey(30) & 0xff

	if k == 27:
		break


cap.release()