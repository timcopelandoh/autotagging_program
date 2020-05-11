import pickle
filepath='fitted_models/'
model_name='handwriting_007'

people = pickle.load(open(filepath+'ids_'+model_name+'.sav', 'rb'))

print(people)