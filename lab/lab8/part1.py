def get_words(description):
	words=set()
	punct=[".",",","(",")","\""]
	for line in description:
		for char in punct:
			line=line.replace(char," ")
		for word in line.strip().lower().split("|")[1].split(" "):
			if len(word)>=4 and word.isalpha():
				words.add(word)
	return words

file=open("csa.txt")
s=get_words(file)
print(s)
print(len(s))