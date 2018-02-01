
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
print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line("	  Here is some spaces 12/32/4"))
print(parse_line("    Again some spaces\n/12/12/12"))