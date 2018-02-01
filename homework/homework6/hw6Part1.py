letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z' ]

def make_set(file):
	#makes a set of all words from the input file
	words=set()
	file=open(file)
	for line in file:
		words.add(line.strip())
	return words

def make_list(file):
	words=[]
	file=open(file)
	for line in file:
		words.append(line.strip())
	return words
  
def found(word,words):
	#returns true if the element is in the set
	return word in words

def drop(word,words):
	#drops each letter from the word and checks if it is in the set
	for i in range(len(word)):
		drop=word[0:i]+word[i+1:]
		if drop in words:
			return True, drop
	return False, ""

def swap(word,words):
	#swaps two letters int the word and checks if it is in the set
	word=list(word)
	for i in range(len(word)-1):
		working_copy=word[:]
		temp=working_copy[i]
		working_copy[i]=working_copy[i+1]
		working_copy[i+1]=temp
		swap= "".join(working_copy)
		if swap in words:
			return True, swap
	return False, ""

def replace(word,words):
	#replaces each letter of the word with each letter of the alphabet, then checks if it is in the set
	# letters=list(string.ascii_lowercase)
	word=list(word)
	for i in range(len(word)):
		for letter in letters:
			working_copy=word[:]
			working_copy[i]=letter
			replace="".join(working_copy)
			if replace in words:
				return True, replace
	return False, ""

if __name__ == '__main__':
	
	dictionary=input("Dictionary file => ").strip()
	print(dictionary)
	bad_words=input("Input file => ").strip()
	print(bad_words)
	# dictionary="words_10pt.txt"
	# bad_words="input_words.txt"
	dictionary=make_set(dictionary)
	bad_words=make_list(bad_words)
	seen=set()
	for word in bad_words:
		if word in seen:
			continue
		seen.add(word)
		if found(word,dictionary):
			print("{:<15} -> {:<15} :FOUND".format(word,word))
			continue
		dropped,fixed=drop(word,dictionary)
		if dropped:
			print("{:<15} -> {:<15} :DROP".format(word,fixed))
			continue
		swapped,fixed=swap(word,dictionary)
		if swapped:
			print("{:<15} -> {:<15} :SWAP".format(word,fixed))
			continue
		replaced,fixed=replace(word,dictionary)
		if replaced:
			print("{:<15} -> {:<15} :REPLACE".format(word,fixed))
			continue
		print("{:<15} -> {:<15} :NO MATCH".format(word,word))


