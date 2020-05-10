import cv2

def add_boxes(img):

	'''
	Takes input of picture in cv2 image format and returns image with boxes
	around faces
	'''

	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	#img = cv2.imread('flex.jpg')

	#ratio = img.shape[0]/img.shape[1]
	#img = cv2.resize(img, (500, int(ratio*500)))

	gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gs, 1.1, 6)

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

	return img

img = cv2.imread('wine.jpg')

ratio = img.shape[0]/img.shape[1]

img = cv2.resize(img, (500, int(ratio*500)))

img = add_boxes(img)

cv2.imshow('img', img)

cv2.waitKey()