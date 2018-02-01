def get_words(line):
	pipe_flag=False
	words=set()
	punct=[".",",","(",")","\""]
	for char in punct:
		line=line.replace(char," ")
	for word in line.strip().lower().split(" "):
		if "|" in word and not pipe_flag:
			pipe_flag=True
			words.add(word.split("|")[1])
		if len(word)>=4 and word.isalpha() and pipe_flag:
			words=words.union({word})
	return words

def get_club(line):
	return line.strip().lower().split("|")[0]


club1=open(input("Enter the club file: "))

club1_words=[]
for line in club1:
	club1_words.append(get_words(line))

l=dict()
file=open("allclubs.txt")
for line in file:
	c2=get_words(line)
	if c2 != club1_words[0]:
		intersection_code=" ".join(c2 & club1_words[0]) 
		#dicts won't accept sets as keys, so we make a string out of the intersection of the sets
		l[intersection_code]=get_club(line)


sortedl=sorted(l.keys(),reverse=True,key=len)[0:5]
for key in sortedl:
	print(l[key])
	#print(key) 
