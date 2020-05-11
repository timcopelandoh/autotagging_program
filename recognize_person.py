import pickle
import numpy as np

from keras import Sequential
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

#import tensorflow as tf
#import keras.backend.tensorflow_backend as tfback

import cv2

def recognize_hw(face, model_name, filepath='fitted_models/', ext='', return_name=True):
	
	people = pickle.load(open(filepath+'ids_'+model_name+'.sav', 'rb'))
	
	X = face / 255
	X = X.reshape(1,100,100,3)

	model = Sequential()
	model.add(Conv2D(32, kernel_size=(3, 3),
	                 activation='relu',
	                 input_shape=(100,100,3)))
	model.add(Conv2D(64, (3, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.15))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.35))
	model.add(Dense(len(people), activation='sigmoid'))
	model.load_weights(filepath+model_name+ext)
	if return_name == True:
		predictions = model.predict_proba(X)[0]
		return people[np.where(predictions == max(predictions))[0][0]]
	else:
		return model.predict(X)


def recognize_lh(face, model_name, filepath = 'fitted_models/', ext='', return_name=True):
	
	people = pickle.load(open(filepath+'ids_'+model_name+'.sav', 'rb'))
	
	X = face / 255
	X = X.reshape(1,100,100,3)

	model = Sequential()
	model.add(Conv2D(32, kernel_size=(3, 3),
	                 activation='relu',
	                 input_shape=(100,100,3)))
	model.add(Conv2D(64, (3, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.15))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.35))
	model.add(Dense(len(people), activation='sigmoid'))
	model.load_weights(filepath+model_name+ext)
	if return_name == True:
		#return 
		return people[np.where(model.predict(X)[0] == 1)[0][0]]
	else:
		return model.predict(X)

'''
img = cv2.imread('training/faces/Sydney/00004.jpg')

print(recognize_hw(np.array(img), 'handwriting_001'))

print(img)
print(img.reshape((1,100,100,3)))
'''