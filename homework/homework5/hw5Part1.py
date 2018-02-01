import hw5util

def calculate_scores(games, players, predictions,wrt="players"):
	scores=[]
	if wrt=="players":#populate lists accordingly
		for j in range(len(players)):
			scores.append(0)
	elif wrt=="games":
		for i in range(len(games)):
			scores.append(0)
	for i in range(len(games)): #represents a game
		for j in range(len(players)): #represents a player
			win=False
			loss=False
			tie=False
			if predictions[j][i][0]>predictions[j][i][1]:
				win=True
			elif predictions[j][i][0]<predictions[j][i][1]:
				loss=True
			else:
				tie=True
			if (win and games[i][-2]>games[i][-1]) or (loss and games[i][-2]<games[i][-1]) or (tie and games[i][-2]==games[i][-1]):
				if wrt=="players": 
					scores[j]+=2
				elif wrt=="games":
					scores[i]+=2
			if games[i][-2]==predictions[j][i][0]:
				if wrt=="players":
					scores[j]+=1
				elif wrt=="games":
					scores[i]+=1
			if games[i][-1]==predictions[j][i][1]:
				if wrt=="players":
					scores[j]+=1
				elif wrt=="games":
					scores[i]+=1
	return scores

def find_val(scores,competitors,value):
	value_list=[]
	for i in range(len(scores)):
		if scores[i] == value:
			value_list.append(competitors[i])
	return value_list

if __name__ == '__main__':
	
	file=input("Enter the filename => ")
	print(file)

	print("Player points:")
	games,players,predictions=hw5util.read_predictions(file)
	scores=calculate_scores(games,players,predictions)	
	scores_game=calculate_scores(games,players,predictions,wrt="games")


	for i in range(len(players)):
		print("{:<10}:{:>4}".format(players[i],scores[i]))
	
	print("\nWinner(s): (max points: {})".format(max(scores)))
	for entity in find_val(scores,players,max(scores)):
		print(entity)

	print("\nGame points:")
	for j in range(len(games)):
		print("{:<30}:{:>4}".format(games[j][3]+" vs "+games[j][4],scores_game[j]))

	print("\nHardest game(s) (min points: {})".format(min(scores_game)))
	for entity in find_val(scores_game,[game[3]+" vs "+game[4] for game in games], min(scores_game)):
		print(entity)