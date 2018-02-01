def percentage_happy(sentence):
	happy_words=["laugh","happiness","love","excellent","good"]
	count=0
	for word in sentence:
		for other_word in happy_words:
			if other_word in word.lower():
				count+=1
	return "{:.3f}".format(count/len(sentence))
def percentage_sad(sentence):
	sad_words=["bad","terrible","horrible","problem","sad"]
	count=0
	for word in sentence:
		for other_word in sad_words:
			if other_word in word.lower():
				count+=1
	return "{:.3f}".format(count/len(sentence))

sentence=input("Enter a sentence => ")
print(sentence)
sentence_list=sentence.strip().split(" ")
print("Percentages. happy:",percentage_happy(sentence_list),"sad:",percentage_sad(sentence_list))

if percentage_happy(sentence_list)>percentage_sad(sentence_list):
	print("This is a happy sentence")
elif percentage_sad(sentence_list)>percentage_happy(sentence_list):
	print("This is a sad sentence")
else: 
	print("This is a neutral sentence")