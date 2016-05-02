#input_vector = [letter, unigram, bigram]
import csv
import math

parent_speech = input('type a sentence to the AI: ')

speech_array = parent_speech.split()




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


letter_layer = [[random.random() for __ in range(num_letters)] for __ in range(num_words)]

output_layer = [[random.random() for __ in range(num_output_words)] for __ in range(AI_brain_size)]

for word in speech_array:
	for letter in word:
		activateLetterFunction(letter)
	# Open for read+write
	with open("wordmems2.txt", "r+") as myfile:

	    # A file is an iterable of lines, so this will
	    # check if any of the lines in myfile equals line+"\n"
	    if word+"\n" not in myfile:
	        # Write it; assumes file ends in "\n" already
	        myfile.write(word+"\n")

	#myfile.write(line+"\n") can also be written as
	# Python 3
	#print(line, file=myfile)





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
 

