import lab05_util
import webbrowser

def print_info(restaurant):
	print(restaurant[0],"("+restaurant[5]+")")
	address=restaurant[3].split("+")
	print("\t",address[0])
	print("\t",address[1])
	if len(restaurant[-1])>3:
		improved_avg=(sum(restaurant[-1])-min(restaurant[-1])-max(restaurant[-1]))/len(restaurant[-1])
		length=len(restaurant[-1])-2
	else:
		improved_avg=(sum(restaurant[-1]))/len(restaurant[-1])
		length=len(restaurant[-1])

	if improved_avg<2:
		print("This resturant is rated bad, based on {} reviews.".format(length))
	elif improved_avg>=2 and improved_avg<3:
		print("This restaurant is rated average, based on {} reviews.".format(length))
	elif improved_avg>=3 and improved_avg<4:
		print("This restaurant is rated above average, based on {} reviews.".format(length))
	else:
		print("This restaurant is rated very good, based on {} reviews.".format(length))

restaurants = lab05_util.read_yelp('yelp.txt')

number=int(input("Enter the resturaunt id (1 to 155): "))
if number>len(restaurants):
	print("Warning: number not in range 1-155")
else:
	print_info(restaurants[number-1])

web=int(input("What would you like to do next? \n 1. Visit the homepage \
	\n 2. Show on Google Maps \n 3. Show directions to this restaurant \
	\n Your choice (1-3) ==> "))
if web==1:
	webbrowser.open(restaurants[number-1][4])
elif web==2:
	webbrowser.open('http://www.google.com/maps/place/'+restaurants[number-1][3])
elif web==3:
	webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/'+restaurants[number-1][3])