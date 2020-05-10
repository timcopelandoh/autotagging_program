import numpy as np
import os
import cv2



def get_data(path = 'training/faces/', people = ['Tim', 'Dan', 'Malachi', 'Grant']):
	index = 0
	X = []
	y = []

	y_row = [0 for x in people]

	for i in range(len(people)):
		name = people[i]
		files = os.listdir(path+name)
		#print(path+name)
		for file in files:

			if file[-4:] == '.jpg':
				#print(file)
				X.append(cv2.imread(path+name+'/'+file))
				#print('1')
				#X[index] = cv2.imread(path+name+'/'+file)
				#index += 1
				new_row = y_row.copy()
				new_row[i] += 1
				#print('2')
				y.append(new_row)
				#print('3')

	return np.array(X), np.array(y)
	#return np.stack(X), np.array(y)

'''
X, y = get_data()




print(type(X[0]))
print(X.shape)
print(X[0].shape)

print(y.shape)


X = np.empty([100,100,3])

print(type(X))
print(X.shape)'''