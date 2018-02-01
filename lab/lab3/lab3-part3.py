def bpop_year(bpop,fpop):
	bunnies_next= int((10*bpop)/(1+0.1*bpop) - min(0.05*bpop*fpop,(10*bpop)/(1+0.1*bpop)))
	
	return bunnies_next
def fpop_year(bpop,fpop):
	foxes_next= int(0.4 * fpop + 0.02 * fpop * bpop)
	return foxes_next

bpop=int(float(input("Number of bunnies ==> ")))
print(bpop)
fpop=int(float(input("Number of foxes ==>")))
print(fpop)

print("Year 1:",bpop,fpop)

bpop_next=bpop_year(bpop,fpop)
fpop_next=fpop_year(bpop,fpop)
print("Year 2:",bpop_next,fpop_next)

bpop=bpop_year(bpop_next,fpop_next)
fpop=fpop_year(bpop_next,fpop_next)
print("Year 3:",bpop,fpop)

bpop_next=bpop_year(bpop,fpop)
fpop_next=fpop_year(bpop,fpop)
print("Year 4:",bpop_next,fpop_next)

bpop=bpop_year(bpop_next,fpop_next)
fpop=fpop_year(bpop_next,fpop_next)
print("Year 5:",bpop,fpop)
