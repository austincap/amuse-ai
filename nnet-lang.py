import re
import string
import sys
import csv
import msvcrt
import nltk

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, input_dim=20, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(64, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(10, init='uniform'))
model.add(Activation('softmax'))

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(X_train, y_train,
          nb_epoch=20,
          batch_size=16)
score = model.evaluate(X_test, y_test, batch_size=16)


num = 0
outputstring = ""
#done = False

#input4 is good job boolean
# gj_inputboolean = False
# while True:
#     print (num)
#     num += 1
#     outputstring = speak()
#     if msvcrt.kbhit() and msvcrt.getch() == b'g':
#         print ("you pressed",msvcrt.getch(),"so now i will quit")
#         gj_inputboolean = True
#         #done = True
    






#input1 is 20 entry array of letters of each word
letterinputarray = []

#input2 is complete word (string)
wordinputstring = ""

#input3 is 2-grams (array of string)



#middle layer for letters
lettermemory = [ch for ch in string.ascii_lowercase]
# print(lettermemory)




# class Neuron:
# 	def __init__(self, neuronID, listOfWeights):
# 		self.neuronID = neuronID
# 		self.listOfWeights = []

# class WordNeuron(Neuron):
# 	def __init__(self, neuronID, listOfWeights):





# #process text data first
# with open('sdv-train.txt', 'r', encoding='utf8') as f:
#     content = f.readlines()
#     for eachline in content:
#     	print(eachline)
#     	#re.sub(string.punctuation, '', eachline)
#     	#print(eachline)
#     	wordarray = re.split(' ', eachline)
    	
#     	print(wordarray)

#     	for eachword in wordarray:
# 			with open('wordmemories.csv', 'rt') as f:
# 			    reader = csv.reader(f, delimiter=',')
# 			    for index, row in enumerate(reader): #for each index and row in the csv file
#           			if eachword == row[0]: # if the word already exists in the first column
#               			print ("is in file")
#               			break
#               		else:
#               			print('not in file')
#               			break

#     		letterarray = [ch for ch in eachword]
#     		print(letterarray)




#output is a word (or nothing) every 100ms indefinitely

