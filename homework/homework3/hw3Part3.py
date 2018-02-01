name=input("Name of robot => ")
print(name)
x=int(input("X location => "))
print(x)
y=int(input("Y location => "))
print(y)
energy=10
command=''

while command !='end': 
	print("Robot {} is at ({},{}) with energy: {}".format(name,x,y,energy))
	command=input("Enter a command (up/left/right/down/attack/end) => ")
	print(command)
	command=command.lower()
	valid_commands=['up','down','left','right','attack']
	if command in valid_commands:
		if energy>=1:
			if command=='up':
				y-=10
			elif command=='down':
				y+=10
			elif command=='right':
				x+=10
			elif command=='left':
				x-=10
			elif command=='attack': 
				if energy>=3:
					energy-=4
				else:
					continue

		energy+=1
	y=max(y,0)
	y=min(y,100)
	x=max(x,0)
	x=min(x,100)
	energy=min(energy,10)
	energy=max(energy,0)
