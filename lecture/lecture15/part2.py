
imdb_file = input("Data file name: ").strip()
print(imdb_file)
prefix= input("Prefix: ")
print(prefix)

name_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip().split(",")
    name_list.append(name[0])

name_set=set(name_list)
match_name=[]
for name in name_set:
	if len(prefix)<len(name):
		#for i in range(len(prefix)):
		if name[0:len(prefix)]==prefix[0:len(prefix)]:
			match_name.append(name)

match_set=set(match_name)
#print(match_set)
print(len(name_set),"last names")
print(len(match_set),"start with",prefix)
