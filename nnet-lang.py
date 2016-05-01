import re
import string
import sys
import csv
import msvcrt
num = 0
outputstring = ""
#done = False

#input4 is good job boolean
gj_inputboolean = False
while True:
    print (num)
    num += 1
    outputstring = speak()
    if msvcrt.kbhit() and msvcrt.getch() == b'g':
        print ("you pressed",msvcrt.getch(),"so now i will quit")
        gj_inputboolean = True
        #done = True
    

# from keras.models import Sequential

# from keras.layers.core import Dense, Activation

# model = Sequential()

# encoder = Sequential([GRU(26, activation='relu', inner_activation='hard_sigmoid', input_dim=20, return_sequences=True)])




# model.add(Dense())

#input1 is 20 entry array of letters of each word
letterinputarray = []

#input2 is complete word (string)
wordinputstring = ""

#input3 is 3-grams (array of string)


def shouldIspeak(output):


def speak(weights, inputs):
	global output
	if shouldIspeak(output) == True:
	print(output)



#middle layer for letters
lettermemory = [ch for ch in string.ascii_lowercase]
# print(lettermemory)

# #middle layer for words
# wordmemory = ['hey', 'there', 'little', 'baby', 'you', 'are', 'cute', 'say', 'daddy']






class Neuron:
	def __init__(self, neuronID, listOfWeights):
		self.neuronID = neuronID
		self.listOfWeights = []

class WordNeuron(Neuron):
	def __init__(self, neuronID, listOfWeights):





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

