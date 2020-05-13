import cv2
import numpy as np
import keras
import pickle

from keras import Sequential
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint

import tensorflow as tf
import keras.backend.tensorflow_backend as tfback

from sklearn.model_selection import train_test_split

import generate_data

save_name = 'simplecnn_009'

people = ['Tim', 'Dan', 'Malachi', 'Grant', 'Jess', 'Lindsey', 'Sydney', 'Kate']

X, y = generate_data.get_data(people = people)

pickle.dump(people, open('fitted_models/' + 'ids_' + save_name + '.sav', 'wb'))

X = X / 255

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)

checkpoint_loss = ModelCheckpoint(
    filepath = 'fitted_models/'+save_name+'_minloss',
    save_weights_only=True,
    monitor='val_loss',
    mode='min',
    verbose=1,
    save_best_only=True)

checkpoint_acc = ModelCheckpoint(
    filepath = 'fitted_models/'+save_name+'_maxacc',
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    verbose=1,
    save_best_only=True)

def get_batch_size(samples, batches):
    if samples // batches == samples / batches:
        return samples // batches
    else:
        return samples // batches + 1

def _get_available_gpus():
    """Get a list of available gpu devices (formatted as strings).

    # Returns
        A list of available GPU devices.
    """
    #global _LOCAL_DEVICES
    if tfback._LOCAL_DEVICES is None:
        devices = tf.config.list_logical_devices()
        tfback._LOCAL_DEVICES = [x.name for x in devices]
    return [x for x in tfback._LOCAL_DEVICES if 'device:gpu' in x.lower()]

tfback._get_available_gpus = _get_available_gpus


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(100,100,3)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(y.shape[1], activation='sigmoid'))

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(X_train, y_train,
          batch_size=get_batch_size(X_train.shape[0],4),
          epochs=400,
          verbose=1,
          callbacks=[checkpoint_loss, checkpoint_acc],
          validation_data=(X_test, y_test))