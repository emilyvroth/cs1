
def parse_line(line):
	num=('0','1','2','3','4','5','6','7','8','9')
	t=tuple(line.split("/"))
	return_tuple=()
	if line.count("/") < 3: 
		return None 
	for element in t[-3:]:
		for char in element:
			if char not in num:
				return None
		return_tuple+=(int(element),)
	return_tuple+=("/".join(t[:-3]),)
	return return_tuple

def get_line(fname,parno,lineno):
	par_count=1
	line_count=1
	par_flag=False
	poop_flag=False
	for line in open(fname):
		line=line.rstrip()
		if poop_flag and len(line)==0:
			continue
		if len(line)==0:
			poop_flag=True
			if par_count==parno:
				par_flag=True
			par_count+=1
			continue
		poop_flag=False
		if par_flag or par_count==parno:
			if line_count==lineno:
				return line
			line_count+=1

file=input("Please enter the file number ==> ")
par=int(input("Please enter the paragraph number ==> "))
line=int(input("Please enter the line number ==> "))
f=open("program.py","w")
while True:
	file=str(file)+".txt"
	line_temp=get_line(file,par,line)
	if parse_line(line_temp) == None:
		print("Failure while parsing")
		break
	file,par,line,code=parse_line(line_temp)
	if code=="END":
		f.close()
		break
	f.write(code+"\n")
