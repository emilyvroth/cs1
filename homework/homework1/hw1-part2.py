first=input("First => ")
print(first)
second=input("Second => ")
print(second)
print("Example variable names")
print("Lower case: "+first,second,sep="_")
print("For constants: "+first.upper(),second.upper(),sep="_")
print("Camel case: "+first.title(),second.title(),sep="")
print("System variables: "+"",first,second,sep="_")
print("Silly variable: "+first.replace("a","_").replace("e","_"),second.replace("a","_").replace("e","_"),sep="_")