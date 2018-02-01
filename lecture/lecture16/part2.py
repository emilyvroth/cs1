imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
        
names = sorted(counts)
#sorted alphabetical by name

vals = sorted(counts.values())
#sorted by value
max_val=max(vals)
max_name=[]

limit = len(names)
ones_count=0
for index in range(limit):
    name = names[index]
    #print("{} appeared in {} movies".format(name, counts[name])) 
    if counts[name]==1:
    	ones_count+=1
for key,value in counts.items():
	if value==max_val:
		max_name.append(key)

#max_person=names[-1]
print("{} appears most often: {} times".format(max_name[0],max_val))
print("{} people appear once".format(ones_count))