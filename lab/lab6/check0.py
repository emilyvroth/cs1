#1 one line of digits from 0-8
line=[]
for i in range(9):
	line.append(i)
print(*line)

#2 block of pairs from 0,0 to 8,8
for i in range(9):
	row=str(i)
	for j in range(9):
		row=row+","+str(j)
print(row)

