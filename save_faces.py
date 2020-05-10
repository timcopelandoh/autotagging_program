import cv2
import os
import shutil

path = 'training/raw_pics'
destination = 'training/faces/'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

files = os.listdir(path)

im_num = 0

for file in files:
	#print(file)
	img = cv2.imread(path+'/'+file)
	gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gs, 1.1, 6)
	#print('faces recognized: {}'.format(len(faces)))
	for (x,y,w,h) in faces:
		newface = img[y:y+h, x:x+w]
		newface = cv2.resize(newface, (100,100))
		filename = destination + "0" * (5 - len(str(im_num))) + str(im_num) + '.jpg'
		#print(filename)
		im_num += 1
		cv2.imwrite(filename, newface)
	#print()
	#print()


#cv2.imshow('image', img)

#cv2.waitKey()