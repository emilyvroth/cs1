""" Find all words containing three consecutive pairs of double letters 
in a file of all English words located at:

		http://www.greenteapress.com/thinkpython/code/words.txt

**Modules used:**  :py:mod:`urllib` 

**Author**: Sibel Adali <adalis@rpi.edu>, Chuck Stewart <cvstewart@gmail.com>

**Returns:** All words matching condition and the count of found words

**Pseudo Code**::

   open the file from the web with all the words in English
	
   for each word in the file:
	   for all positions l in the word
		   if the letters at positions (l and l+1) are the same
			  and the letters at positions (l+2 and l+3) are the same
			  and the letters at positons  (l+4 and l+5) are the same then
			   output word and increment the count

"""

import urllib.request

def has_three_double(word):
	"""
	Returns True if the word contains three consecutive pairs of
	double letters and False otherwise.         
	"""
	for l in range(len(word)-5):
		if word[l] == word[l+1] and \
				word[l+2]==word[l+3] and \
				word[l+4]==word[l+5]:
			return True
	return False

def atleast_two_double(word):
	"""
	Returns True if the word contains at least two consectutive pairs
	f double letters and False otherwise
	"""
	for l in range(len(word)-3):
		if word[l] == word[l+1] and \
				word[l+2] == word[l+3]:
			return True
	return False

def three_double_one_between(word):
	"""
	Returns True if the word contains three pairs of double letters 
	separated by one letter (it is assumed that the letter seperating the 
	doubles cant be the same letter as either pair of double letters)
	"""
	for l in range(len(word)-7):
		if word[l] == word[l+1] and word[l+1] != word[l+2] and \
				word[l+2] != word[l+3] and word[l+3] == word[l+4] and \
				word[l+4] != word[l+5] and word[l+5] != word[l+6] and \
				word[l+6] == word[l+7]:
			return True
	return False

def three_double_two_between(word):
	"""
	Returns True if the word contains three pairs of double letters
	seperated by two letters (it is assumed that the letters consecutive
	to the pairs of doubles cannot equal the same letter as the pair)
	"""
	for l in range(len(word)-9):
		if word[l] == word[l+1] and word[l+1] != word[l+2] and \
				word[l+2] != word[l+3] and word[l+3] != word[l+4] and \
				word[l+4] == word[l+5] and word[l+5] != word[l+6] and \
				word[l+6] != word[l+7] and word[l+7] != word[l+8] and \
				word[l+8] == word[l+9]:
			return True
	return False

# Comments that fit in a single line can be put in this format.

# The main body of the program starts here

"""
Assign the location of the words file and go get it.
"""
word_url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
word_file = urllib.request.urlopen(word_url)

'''
Process each word in the file one by one, testing to see if it has
three consecutive doubles.  Print it and count it if it does.
'''
three_dubs = []
atleast_two_dubs = []
three_dubs_one_between = []
three_dubs_two_between = []
for word in word_file:
	word = word.decode().strip()
	if has_three_double(word):
		three_dubs.append(word)
	if atleast_two_double(word):
		atleast_two_dubs.append(word)
	if three_double_one_between(word):
		three_dubs_one_between.append(word)
	if three_double_two_between(word):
		three_dubs_two_between.append(word)

'''
After we've gone through all the words, output a final message based
on the number of words that were counted.
'''   
print("Three consecutive doubles")
for word in three_dubs: 
	print(word)
if len(three_dubs) == 0:
	print('No words found')
elif len(three_dubs) == 1:
	print("1 word found")
else:
	print(len(three_dubs), 'words were found')

print("\nAt least two doubles")
for word in atleast_two_dubs: 
	print(word)
if len(atleast_two_dubs) == 0:
	print('No words found')
elif len(atleast_two_dubs) == 1:
	print("1 word found")
else:
	print(len(atleast_two_dubs), 'words were found')

print("\nThree doubles one letter between")
for word in three_dubs_one_between: 
	print(word)
if len(three_dubs_one_between) == 0:
	print('No words found')
elif len(three_dubs_one_between) == 1:
	print("1 word found")
else:
	print(len(three_dubs_one_between), 'words were found')

print("\nThree doubles two letters between")
for word in three_dubs_two_between: 
	print(word)
if len(three_dubs_two_between) == 0:
	print('No words found')
elif len(three_dubs_two_between) == 1:
	print("1 word found")
else:
	print(len(three_dubs_two_between), 'words were found')