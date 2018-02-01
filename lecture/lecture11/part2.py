hd=int(input("Enter Dale's height: "))
print(hd)
he=int(input("Enter Erin's height: "))
print(he)
hs=int(input("Enter Sam's height: "))
print(hs)

if hd>he and hd>hs:
	print("Dale")
	if he>hs:
		print("Erin")
		print("Sam")
	else:
		print("Sam")
		print("Erin")
if he>hd and he>hs:
	print("Erin")
	if hd>hs:
		print("Dale")
		print("Sam")
	else:
		print("Sam")
		print("Dale")
if hs>hd and hs>he:
	print("Sam")
	if hd>he:
		print("Dale")
		print("Erin")
	else: 
		print("Erin")
		print("Dale")