def make_dict(file):
	#makes a dictionary of all words from the input file with floats as the values
	words=dict()
	file=open(file)
	for line in file:
		words[line.strip().split(",")[0]]=float(line.strip().split(",")[1])
	return words

def make_list(file):
	words=[]
	file=open(file)
	for line in file:
		words.append(line.strip())
	return words

def keyboard_dict(file):
	#makes the keyboard dictionary of all letters close on the keyboard to a letter
	keyboard=dict()
	temp=[]
	file=open(file)
	for line in file:
		line=line.strip().split(" ")
		temp.append(line)
	for i in range(len(temp)):
		keyboard[temp[i][0]]=temp[i][1:]
	return keyboard
 
def found(word,words):
	#returns true if the element is in the set
	return word in words

def drop_func(word,words):
	#drops each letter from the word and checks if it is in the set
	fixed=dict()
	for i in range(len(word)):
		drop=word[0:i]+word[i+1:]
		if drop in words.keys():
			fixed[drop]=words[drop]
	return fixed

def swap_func(word,words):
	#swaps two letters int the word and checks if it is in the set
	word=list(word)
	fixed=dict()
	for i in range(len(word)-1):
		working_copy=word[:]
		temp=working_copy[i]
		working_copy[i]=working_copy[i+1]
		working_copy[i+1]=temp
		swap= "".join(working_copy)
		if swap in words:
			fixed[swap]=words[swap]
	return fixed

def replace_func(word,words):
	#replaces each letter of the word with each letter of the alphabet, then checks if it is in the set	
	fixed=dict()
	keyboard=keyboard_dict("keyboard.txt")
	word=list(word)
	for i in range(len(word)):
		for letter in keyboard[word[i]]:
			working_copy=word[:]
			working_copy[i]=letter
			replace="".join(working_copy)
			if replace in words:
				fixed[replace]=words[replace]
	return fixed

if __name__ == '__main__':
	
	dictionary=input("Dictionary file => ").strip()
	print(dictionary)
	bad_words=input("Input file => ").strip()
	print(bad_words)
	keyboard=input("Keyboard file => ").strip()
	print(keyboard)
	x = dict()
	#dictionary="words_10percent.txt"
	#bad_words="input_words.txt"
	#keyboard="keyboard.txt"
	dictionary=make_dict(dictionary)
	bad_words=make_list(bad_words)
	keyboard=keyboard_dict(keyboard)
	print("Spellcheck results:")
	for word in bad_words:
		if found(word,dictionary):
			print("{:<15} -> {:<15} :FOUND".format(word,word))
			continue
		fixed={**drop_func(word,dictionary), **swap_func(word,dictionary), **replace_func(word,dictionary)}
		fixed=sorted(fixed,key=lambda word: fixed[word], reverse=True)

		if len(fixed)==0:
			print("{:<15} -> {:<15} :NO MATCH".format(word,word))	
		for i in range(len(fixed)):
			if i < 3:
				print("{:<15} -> {:<15} :MATCH {}".format(word,fixed[i],i+1))

