i=1
l=[]
while i != 0:
	i=int(input("Enter a value (0 to end): "))
	print(i)
	l.append(i)
l.remove(0)
print("Min:",min(l))
print("Max:",max(l))
print("Avg: {:.1f}".format(sum(l)/len(l)))