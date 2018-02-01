def get_words(description):
	words=set()
	punct=[".",",","(",")","\""]
	for line in description:
		for char in punct:
			line=line.replace(char," ")
		for word in line.strip().lower().split(" "):
			if "|" in word:
				words.add(word.split("|")[1])
				continue
			if len(word)>=4 and word.isalpha():
				words.add(word)
	return words


club1=input("Enter club 1 file: ")
club2=input("Enter club 2 file: ")
s1=get_words(open(club1))
s2=get_words(open(club2))
line1=open(club1).readline()
line2=open(club2).readline()
name1=line1[0:line1.index("|")]
name2=line2[0:line2.index("|")]
print("Comparing clubs {} and {}".format(name1,name2))
print()
print("Same words: {}".format(s1.intersection(s2)))
print()
print("Unique to {}: {}".format(name1,s1.difference(s2)))
print()
print("Unique to {}: {}".format(name2,s2.difference(s1)))