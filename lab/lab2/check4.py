first=input("Please enter your first name: ")
last=input("Please enter yout last name: ")
maximum=max(len(first),len(last)+1,len("Hello,"))
hello="** "+"Hello,"+" "*(maximum-len("Hello,"))+" **"
first="** "+first+" "*(maximum-len(first))+" **"
last="** "+last+"!"+" "*(maximum-len(last)-1)+" **"
print("*"*(maximum+6),hello,first,last,"*"*(maximum+6),sep="\n")