#input_vector = [letter, unigram, bigram]
import csv
import math, random
import numpy as np
import string




"""Compute softmax values (probabilities) for each sets of scores in x."""
def softmax(x):
	return np.exp(x) / np.sum(np.exp(x), axis=0)

def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i+1

def letterActivationFunction(array_of_letters):
	with open("listOfLetterActivation.txt", "r+") as myfile:
		for letter in array_of_letters:
			for enum, asciichar in enumerate(string.ascii_lowercase):
				print(enum)
				if asciichar == letter:
					print("activate " + asciichar)

def main():
	gj = input('type a 1 or 0 based on quality of AI output: ')
	parent_speech = input('type a sentence to the AI: ')

	speech_array = parent_speech.split()
	print(speech_array)

	for word in speech_array:
		input_vector = []
		unigram_input_vector=[]

		with open("wordmems2.txt", "r+") as myfile:
			word_dim = file_len("wordmems2.txt")
			for i, line in enumerate(myfile, 1):
				if word+"\n" in line:
					unigram_input_vector = [0] * word_dim
					unigram_input_vector[i] = 1
					break
			else: # else in python for loop???!!
				myfile.write(word+"\n") # append missing data
				unigram_input_vector = [0] * word_dim
				unigram_input_vector[-1] = 1

		letter_input_vector = []
		for letter in word:
			letter_input_vector += [letter]
		
		letterActivationFunction(letter_input_vector)
		input_vector = [letter_input_vector, unigram_input_vector, gj]
		print(input_vector)

	word_output_vector = [0.9,0,0,0,0.9]

	output_string = "test"
	print(output_string)

	main()

main()
#type something to it

#let it process your line of text
##tokenize
##activate letters in the temporal order they appear
##activate words in the temporal order they appear at the same time as corresponding letters
##activate bigrams in the temporal order they appear at the same time as corresponding words

#let it say something back

#give it approval or not

#update weights based on feedback

#continue providing it with input and feedback on it's output



# def activateLetterFunction(letter):
# 	with open("lactlist.json", "r+") as lactlist:

# for item in thelist:
#   print>>thefile, item


#26x26 matrix of letters to each other
#30000x30000 matrix of words to each other
#26x30000 matrix of letters to words
#30000x100 matrix of words to hidden layer AI brain
#10x100 matrix of gj memories to hidden layer AI brain
#10x30000 matrix of gj memories to output words
#30000x30000 matrix output words to each other

random.seed(0)
input_string = ""
num_letters = 26
num_words = 20000
AI_brain_size = 50
gj_memories_size = 5
num_output_words = 20000

def sigmoid(t):
	return 1/(math.exp(-t))

def neuron_output(weights, inputs):
	return sigmoid(dot(weights, inputs))

# def feed_forward(neural_network, letter_array, word_array, gj_value):
# 	"""takes in neural net as a list of lists of lists of weights
# 	and returns output from forward propagating the input"""

# 	outputs = []

# 	for layer in neural_network:
# 		input_bias = input_vector + [1]

#  math.tanh(x)

# letter_layer = [[random.random() for __ in range(num_letters)] for __ in range(num_words)]

# output_layer = [[random.random() for __ in range(num_output_words)] for __ in range(AI_brain_size)]





# with open('wordmems2.txt') as f:
# 	for line in f:
# 		for eachword in speech_array:
# 			if eachword != line:
# 				print(line[:-1])



# with open('wordmems.csv', newline='') as f:
# 	reader = csv.reader(f, delimiter=',')
# 	for row in reader:
# 		print(row)

# for eachword in speech_array:
# 	print(eachword)
# 	for row in reader:
# 		if eachword == row[1]:
# 			print("dont add")
# 		else: 
# 			print("add: " + eachword)
 

