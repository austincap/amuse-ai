# amuse-ai
text-analysis with nnets and positive reinforcement

Goal: The purpose of this script is to generate amusing strings of text based off nothing but user inputs.

Method: Each time the user inputs a sentence into the program, new words are added to a dictionary. Next, that information is backpropagated through a recurrent neural network along with a signal that denotes positive reinforcement (or punishment). The transformation of the combination of these two data sources (plus whatever previous output was generated via the RNN) causes the script to output a string "sentence" in response to the user string input and the positive reinforcement (or punishment) input. This last input is also referred to as the "good job" or "gj" input. 

Details: For now, all sentences must consist of 6 words with no punctuation. The initial text the amuse-ai script produces is always "hey how are you doing today". After the user reads this, he should be prompted to enter a positive reinforcement/punishment value, with 0.0 denoting an unamusing statement, 0.5 denoting a neutral statement, and 1.0 denoting an amusing statement. Next the user is prompted to enter his own 6 word sentence in "response" to the amuse-ai. The script then generates a new statement based on (in chronological order utilizing the RNN) the previous output sentence, the positive punishment/reinforcement value, and finally the new user input. A better explanation is avaliable in the picture below. The dictionary of all words the script has been exposed to is created on-the-fly although it can be saved from session to session. As new words are added to the dictionary, new "neurons" are added to the hidden layer.

Questions: I'm not sure whether or not to track the letters along with each newly learned word.

![amuse-ai](https://github.com/austincap/amuse-ai/blob/master/amuse-ai.png "amuse-ai")
amuse-ai explained

![amuse-ai-example](https://github.com/austincap/amuse-ai/blob/master/amuse-ai%20-%20example.png "amuse-ai-example")
amuse-ai concrete example

