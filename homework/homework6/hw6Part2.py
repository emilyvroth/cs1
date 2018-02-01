import textwrap

def get_info(file,title):
	#finds the title and a set of beasts for the given input
	file=open(file)
	for line in file:
		if title in line.split("|")[0]:
			title=line.split("|")[0]
			beasts=set(line.strip().split("|")[1:])
			return title, beasts


def other_titles(file_list,beasts):
	#finds the other titles with the beasts in common
	titles_common=set()
	for i in range(len(file_list)):
		for beast in beasts:
			if beast in file_list[i][1:]:
				titles_common.add(file_list[i][0])
	titles_common=sorted(titles_common)
	str_titles="Other titles containing beasts in common: "+", ".join(titles_common)
	str_titles=textwrap.wrap(str_titles)
	return str_titles

def make_list(file):
	file_list=[]
	file=open(file)
	for line in file:
		file_list.append(line.strip().split("|"))
	return file_list

def remove_line(i, stuff):
	return stuff[0:i]+stuff[i+1:]

def unique(file_list,beasts):
	#finds the unique beasts for the title
	for i in range(len(file_list)):
		beasts-=set(file_list[i][1:])
	unique_beasts=sorted(beasts)
	str_unique="Beasts appearing only in this title: "+", ".join(unique_beasts)
	str_unique=textwrap.wrap(str_unique)
	return str_unique

if __name__ == '__main__':
	while True: 	
		file="titles.txt"
		input_title=input("Enter a title (stop to end) => ")
		print(input_title)
		input_title=input_title.title().strip() #matches to title case of text file
		if input_title=="Stop":
			print()
			break
		if get_info(file,input_title) == None:
			print("\nThis title is not found!")
			continue

		title,beasts=get_info(file,input_title) #sets the two variables to the output of the function

		beasts_sorted=sorted(beasts) #sorted alphabetically to match output
		beasts_str="Beasts in this title: "+", ".join(beasts_sorted)
		beasts_str=textwrap.wrap(beasts_str) #makes the line not a long mess


		file_list=make_list(file)
		#finds the output of the other_titles function to format printing later
		#titles_str=other_titles(file_list,beasts_sorted)
	
		
		unique_str=""
		title_str=""
		for i in range(len(file_list)):
			if title in file_list[i][0]:
				titles_str=other_titles(remove_line(i,file_list),beasts)
				unique_str=unique(remove_line(i,file_list),beasts)
				break

		print()
		print("Found the following title: {}".format(title))
		for line in beasts_str:
			print(line)
		print()
		for line in titles_str:
			print(line)
		print()
		for line in unique_str:
			print(line)
		print()
		