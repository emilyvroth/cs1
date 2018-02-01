word=input("Word => ")
print(word)
columns=int(input("#columns => "))
print(columns)
rows=int(input("#rows => "))
print(rows)
print("Your word is: "+word+"\n")

line=("*** "*columns).rstrip()+"\n"
first_and_last="*** "*(columns//2)+" | "+(" ***"*(columns//2))+"\n"
mid_rows=line*(rows//2-1)
word_row=" |  "+"*** "*(columns//2-1)+"CS1"+(" ***"*(columns//2-1))+"  | "+"\n"

array_a=line*rows
array_b=line*(rows//2)+"*** "*(columns//2)+"CS1"+(" ***"*(columns//2))+"\n"+line*(rows//2)
array_c=first_and_last+mid_rows+word_row+mid_rows+first_and_last.rstrip()

print("(a)",array_a,sep="\n")
print("(b)",array_b,sep="\n")
print("(c)",array_c,sep="\n")