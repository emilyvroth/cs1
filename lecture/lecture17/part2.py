imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()

for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    movie = words[1].strip()
    if movie in counts:
        if words[0] in counts[movie]:
            continue
        counts[movie].append(words[0]) 
        continue
    counts[movie]=[words[0]]


movies=sorted(counts)
vals = sorted(counts.values())
#sorted by value

max_val=max(vals,key=len)
max_movie=[]

ones_count=0
for index in range(len(movies)):
    movie = movies[index]
    if len(counts[movie])==1:
    	ones_count+=1
for key,value in counts.items():
	if value==max_val:
		max_movie.append(key)

print(len(max_val))
print(max_movie[0]) 
print(ones_count)