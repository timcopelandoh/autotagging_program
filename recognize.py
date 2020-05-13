import cv2
from recognize_person import recognize_cnn, recognize_lh

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('oktoberfest.jpg')

ratio = img.shape[0]/img.shape[1]
img = cv2.resize(img, (2000, int(ratio*2000)))

gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gs, 1.135, 9)

#face_images = []

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 5)
	face = img[y:y+h, x:x+w]
	face = cv2.resize(face, (100,100))

	#print(face.shape)
	#identity = recognize_cnn(face, 'simplecnn_007', ext='_maxacc')
	identity = recognize_lh(face, 'levi-hassner_006', ext='_minloss')
	#identity = recognize_lh(face, 'levi-hassner_008', ext='_minloss')

	cv2.putText(img, identity, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 5)


if ratio < 1:
	size = (800, int(ratio*800))
else:
	size = (int(800/ratio), 800)

img = cv2.resize(img, size)

cv2.imwrite('tagged_oktoberfest.jpg', img)


cv2.imshow('img', img)

#cv2.imshow('face', face_images[0])

cv2.waitKey()
'''
x, y, w, h = faces[2]

cv2.imshow('face', img[y:y+h, x:x+h])

cv2.waitKey()'''
