import lab05_util

def print_info(restaurant):
	print(restaurant[0],"("+restaurant[5]+")")
	address=restaurant[3].split("+")
	print("\t",address[0])
	print("\t",address[1])
	avg=sum(restaurant[-1])/len(restaurant[-1])
	print("Average Score: {:.2f}".format(avg))

restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[0])
print("\n")
print_info(restaurants[4])