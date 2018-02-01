import math
num_bears=int(input("Number of bears => "))
print(num_bears)
num_berries=float(input("Size of berry area => "))
print(round(num_berries))

def find_tourists(bears):
	if bears>15 or bears<4:
		return 0
	if bears <= 10:
		return 10000*bears
	return 10000*10+20000*(bears-10)


def find_next(bears,berries,tourists):
	bears_next=berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)
	bears_next=max(bears_next, 0)

	berries_next = (berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05)
	berries_next=max(berries_next,0)
	return (int(bears_next),berries_next)

bears_out=[num_bears]
berries_out=[num_berries]
tourists=[]
print("Year\tBears\tBerries\tTourists")
for year in range(10):
	tourists.append(find_tourists(bears_out[year]))
	print(year+1, bears_out[year],"{:.1f}".format(berries_out[year]), tourists[year], sep="\t")
	bears_out.append(find_next(bears_out[year], berries_out[year], tourists[year])[0])
	berries_out.append(find_next(bears_out[year], berries_out[year], tourists[year])[1])	 
bears_out.pop()
berries_out.pop()
print()
print("Min:",min(bears_out),round(min(berries_out),1),min(tourists),sep="\t")
print("Max:",max(bears_out),round(max(berries_out),1),max(tourists),sep="\t")
