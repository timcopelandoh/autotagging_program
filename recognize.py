import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('oktoberfest.jpg')


ratio = img.shape[0]/img.shape[1]
img = cv2.resize(img, (500, int(ratio*500)))

gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gs, 1.1, 6)

#face_images = []

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	#face_images = face_images.append(img[y:y+h, x:x+w])

cv2.imshow('img', img)

#cv2.imshow('face', face_images[0])

cv2.waitKey()
'''
x, y, w, h = faces[2]

cv2.imshow('face', img[y:y+h, x:x+h])

cv2.waitKey()'''