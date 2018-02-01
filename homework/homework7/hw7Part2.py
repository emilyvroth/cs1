import json

def movies_in_years(y1,y2,movies):
	#returns a dictionary of only movies that fall within the min and max year
	in_year=dict()
	for i in movies:
		year=movies[i]['movie_year']
		if year>=y1 and year<=y2:
				in_year[i]=movies[i]
	return in_year		

def weighted_ratings(movies,ratings,w1,w2):
	#returns a dictionary of ratings with the weights 
	weight=dict()
	for key in movies.keys():
		imdb_rating=movies[key]['rating']
		if key in ratings.keys() and len(ratings[key])>=3:
			average_twitter_rating=sum(ratings[key])/len(ratings[key])
			rating=(w1* imdb_rating + w2 * average_twitter_rating)/(w1+w2)
			weight[key]=rating
	return weight

if __name__ == "__main__":

	movies = json.loads(open("movies.json").read())
	ratings = json.loads(open("ratings.json").read())

	min_year=int(input("Min year => "))
	print(min_year)
	max_year=int(input("Max year => "))
	print(max_year)
	w1=(input("Weight for IMDB => "))
	print(w1)
	w1=float(w1)
	w2=(input("Weight for Twitter => "))
	print(w2)
	w2=float(w2)
	#min_year=2000
	#max_year=2016
	#w1=0.7
	#w2=0.3

	new_movies=movies_in_years(min_year,max_year,movies)
	ratings=weighted_ratings(new_movies,ratings,w1,w2)
	ordered_ratings=sorted(ratings.keys(),key=lambda m: (ratings[m],m))
	#print(ratings)

	print("10 Highest rated movies")
	for i in range(len(ordered_ratings)-1,len(ordered_ratings)-11,-1):
		key=ordered_ratings[i]
		print("{} ({})".format(movies[key]['name'],movies[key]['movie_year']))
		print("{:>17} {:.2f}".format("Rating:",ratings[key]))
		print("{:>17} {}".format("Genres:",", ".join(movies[key]['genre'])))
	print("\n10 lowest rated movies")
	for i in range(10):
		key=ordered_ratings[i]
		print("{} ({})".format(movies[key]['name'],movies[key]['movie_year']))
		print("{:>17} {:.2f}".format("Rating:",ratings[key]))
		print("{:>17} {}".format("Genres:",", ".join(movies[key]['genre'])))
 
