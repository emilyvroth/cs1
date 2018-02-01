import syllables
paragraph=input("Enter a paragraph => ").strip()
sentences=paragraph.split(".")
sentences.pop()
words=paragraph.split(" ")

#to find ASL, the average sentence length
ASL=len(words)/len(sentences)
	
#to find PHW, the percent hard words
hard_words=[]
count=0
total_sylls=0
for word in words:
	if syllables.find_num_syllables(word) >= 3 and "-" not in word and word[-2:len(word)] != "es" and word[-2:len(word)] !="ed":
		count+=1
		hard_words.append(word)
	#to find AYSL, the average number of syllables
	total_sylls+=syllables.find_num_syllables(word)
AYSL=total_sylls/len(words)
PHW=count/len(words)

GFRI= 0.4*(ASL + PHW*100)
FKRI=206.835-1.015*ASL-86.4*AYSL

print(paragraph)
print("Here are the hard words in this paragraph:")
print(hard_words)
print("Statistics: ASL:{:.2f} PHW:{:.2%} ASYL:{:.2f}".format(ASL,PHW,AYSL))
print("Readability index (GFRI): {:.2f}".format(GFRI))
print("Readability index (FKRI): {:.2f}".format(FKRI))