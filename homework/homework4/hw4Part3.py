import hw4_util

def find_university(data,name):
	universities=[]
	for l in data:
		universities.append(l[0])
	return universities.index(name) if name in universities else "University not found"
	
data = hw4_util.read_university_file("university_data.csv")

your_uni=(input("University name => "))
print(your_uni)


first_uni=int(input("Line number for first university to compare (1-1000) => "))
print(first_uni)
second_uni=int(input("Line number for second university to compare (1-1000) => "))
print(second_uni)

result=find_university(data,your_uni)

if type(result) is int:
	print("First university:",data[first_uni][0])
	print("Second university:",data[second_uni][0])
	print()
	f="First"
	s="Second"
	y="Yours"
	print("{0:>37}{1:>12}{2:>12}".format(f,s,y))

	i=find_university(data,your_uni)
	for j in range(1,14):
		print("{0:>25}{1:>12}{2:>12}{3:>12}".format(data[0][j],data[first_uni][j],data[second_uni][j],data[i][j]))
else:
	print(result)
