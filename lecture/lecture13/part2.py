input_file=input("Enter the scores file: ")
print(input_file)
output_file=input("Enter the output file: ")
print(output_file)


lines=[]
for line in open(input_file):
	lines.append(int(line))

lines.sort()

out=open(output_file,"w") 
for l in range(len(lines)):
	out.write("{:2d}: {:3d}\n".format(l,lines[l]))
out.close()