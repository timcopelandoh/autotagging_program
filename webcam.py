import cv2
import warnings
from recognize_person import recognize_lh
import pickle
import numpy as np

from keras import Sequential
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

warnings.filterwarnings('ignore')


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

people = pickle.load(open('fitted_models/ids_levi-hassner_006.sav', 'rb'))

model = Sequential()
	# First convolutional layer, note the specification of shape
model.add(Conv2D(96, kernel_size=(7, 7),
	                 activation='relu',
	                 input_shape=(100,100,3)))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Conv2D(256, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Conv2D(384, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3)))
#model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(len(people), activation='softmax'))

model.load_weights('fitted_models/levi-hassner_006_minloss')


while True:
	
	_, img = cap.read()

	gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gs, 1.1, 6)

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 5)
		face = img [y:y+h, x:x+w]
		face = cv2.resize(face, (100,100))
		face = face.reshape(1,100,100,3)

		#identity = recognize_lh(face, 'levi-hassner_006', ext='_minloss')
		predictions = model.predict_proba(face)[0]
		identity = people[np.where(predictions == max(predictions))[0][0]]

		cv2.putText(img, identity, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 5)

	cv2.imshow('img', img)

	k = cv2.waitKey(30) & 0xff

	if k == 27:
		break


cap.release()