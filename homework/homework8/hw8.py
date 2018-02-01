from Person import *
from Universe import *
import json

def make_universe(uni_dict, i):
	'''
	makes a universe object with name, rewards, and portals
	'''
	return Universe(uni_dict["universe_name"], make_rewards(uni_dict), make_portals(uni_dict), i)

def make_rewards(uni_dict):
	'''
	makes the reward objects to be used in the make_universe function
	'''
	rewards = []
	home = uni_dict["universe_name"]
	for x,y,points,name in uni_dict["rewards"]:
		rewards.append(Reward(x,y,points,name,home))
	return rewards[:]

def make_portals(uni_dict):
	'''
	makes the portal objects to be used in the make_universe function
	'''
	portals = []
	for from_x,from_y,to_name,to_x,to_y in uni_dict["portals"]:
		portals.append(Portal(uni_dict["universe_name"],from_x,from_y,to_name,to_x,to_y))
	return portals

def make_people(uni_dict, i):
	'''
	returns a list of person obejects, going through the people in each universe and adding them to a list
	'''
	people=[]
	for name,radius,x,y,dx,dy in uni_dict["individuals"]:
		people.append(Person(name, float(radius), uni_dict["universe_name"], float(x), float(y), float(dx), float(dy), uni_dict["universe_name"], i))
		i += 1
	return people, i

def validate(people, universes, counter):
	'''
	the purpose of this function was to handle the test case where somebody starts out either 
	near the edge of the board or with a speed of less than 10.
	in this case the person would not move through step 0, so after the counter is impletmented below it would not catch these two things
	'''

	#step 2 below - speed less than 10
	for i in range(len(people)): 
		if not people[i].can_move():
			print("{} stopped at simulation step {} at location ({:.1f},{:.1f})".format(people[i].name, counter, people[i].x, people[i].y))
			print()
			people[i].stop()

		#step 3 below - starting near the edge
		if people[i].near_edge(): #near_edge will stop the person from moving if True
			print("{} stopped at simulation step {} at location ({:.1f},{:.1f})".format(people[i].name, counter, people[i].x, people[i].y))
			print()
			people[i].stop()


if __name__ == '__main__':

	#reading the file and creating the proper data types and objects from the data
	file = input("Input file => ")
	print(file)
	data = json.loads(open(file).read())
	uni_counter = 0
	people_counter = 0
	universes = dict()
	people = []
	for universe_dict in data:
		universes[universe_dict["universe_name"]]=make_universe(universe_dict, uni_counter)
		uni_counter += 1
		temp_people, i = make_people(universe_dict, people_counter)
		people += temp_people
		people_counter = i


	# initial printing of all the universes and people with their attributes before the simulation begins
	print("All universes")
	print("-"*40)
	for universe in sorted(universes.values(),key = lambda x:x.i):
		print(str(universe))
	print("All individuals")
	print("-"*40)
	for person in people:
		print(str(person))
	print("\nStart simulation")
	print("-"*40)

	#simulation counter starts here!
	counter = 0
	validate(people, universes, counter)
	move_flag = True #move_flag will keep track of if people are still moving at each step of the simulation
	while counter < 100 and move_flag:
		move_flag = False

		#step 1 of simulation steps outlined in homework pdf, incrementing the counter
		counter += 1

		#step 2, moving each person
		for i in range(len(people)): 
			if not people[i].can_move() and not people[i].stopped():
				print("{} stopped at simulation step {} at location ({:.1f},{:.1f})".format(people[i].name, counter, people[i].x, people[i].y))
				print()
				people[i].finaldx = people[i].dx	# the final speed is set to the current speed at each section in the while loop
				people[i].finaldy = people[i].dy	# this updates the speed while printing and is done every time a person is about to be printed,except for in the print of the winners
				people[i].stop()
			elif people[i].stopped():
				continue
			else:
				people[i].move()
				move_flag = True

		#step 3, checking if they are near an egde and taking the proper action
		for i in range(len(people)): 
			if people[i].near_edge(): #near_edge will stop the person from moving if True
				print("{} stopped at simulation step {} at location ({:.1f},{:.1f})".format(people[i].name, counter, people[i].x, people[i].y))
				print()
				people[i].finaldx = people[i].dx
				people[i].finaldy = people[i].dy
				people[i].stop()

			#step 4, seeing if they are near treasure and taking the proper action (pick_up_treasure), checks each reward in the universe against the person
		for i in range(len(people)): 
			for reward in universes[people[i].current_universe].rewards: 
				if people[i].near_treasure(reward): 
					people[i].pick_up_treasure(reward) #pick_up_treasure will pick up and adjust speed if True
					print("{} picked up \"{}\" at simulation step {}".format(people[i].name, reward.name, counter))
					people[i].finaldx = people[i].dx
					people[i].finaldy = people[i].dy
					print(str(people[i]))
					print()
					universes[people[i].current_universe].rewards.remove(reward) #in persons current universe because they can only pick up in current
					if not people[i].can_move() and not people[i].stopped():
						print("{} stopped at simulation step {} at location ({:.1f},{:.1f})".format(people[i].name, counter, people[i].x, people[i].y))
						print()
						people[i].finaldx = people[i].dx	# the final speed is set to the current speed at each section in the while loop
						people[i].finaldy = people[i].dy	# this updates the speed while printing and is done every time a person is about to be printed,except for in the print of the winners
						people[i].stop()

			#step 5, checking for collisions between people in the same universe and taking the proper actions if True
		for i in range(len(people)): 
			for j in range(i+1,len(people)):  #increment starting at i+1 to never get the same combination of people twice
				if people[i].near_other(people[j]):
					reward = people[i].collide() #returns dropped reward of the person, and in next line the dropped reward of the other person
					other_reward = people[j].collide()
					print("{} and {} crashed at simulation step {} in universe {}".format(people[i].name, people[j].name, counter, people[i].current_universe))
					if reward != None:
						print("{} dropped \"{}\", reward returned to {} at ({},{})".format(people[i].name, reward.name, reward.home_universe, reward.x, reward.y))
						universes[reward.home_universe].rewards.append(reward)  #returns reward to current universe
					if other_reward != None:
						print("{} dropped \"{}\", reward returned to {} at ({},{})".format(people[j].name, other_reward.name, other_reward.home_universe, other_reward.x, other_reward.y))
						universes[other_reward.home_universe].rewards.append(other_reward)
					people[i].finaldx = people[i].dx
					people[i].finaldy = people[i].dy
					print(str(people[i]))
					people[j].finaldx = people[j].dx
					people[j].finaldy = people[j].dy
					print(str(people[j]))
					print()
					
					 

			#step 6, checking if the person is near a portal and passing though accordingly
		for i in range(len(people)): 
			for portal in universes[people[i].current_universe].portals:
				if people[i].near_portal(portal):  
					people[i].go_through_portal(portal) #go_through_portal will transport the person
					print("{} passed through a portal at simulation step {}".format(people[i].name, counter))
					people[i].finaldx = people[i].dx
					people[i].finaldy = people[i].dy
					print(str(people[i]))
					print()

	if not move_flag: #for the case where nobody is moving, before step 100 is reached
		counter -= 1
	values = dict() #to store the point values to later determine a winner
	mover_count = 0
	moving = []
	for i in range(len(people)):	
		values[people[i]] = people[i].get_value()
		if not people[i].stopped():
			mover_count += 1
			moving.append(people[i].name)

	winner = max(values, key=values.get)
	winners = []
	for person in values:
		if values[winner] == values[person]:
			winners.append(person)

	#stopping simulation printing
	print()
	print("-"*40) 
	print("Simulation stopped at step {}".format(counter))
	print("{} individuals still moving".format(mover_count), end="")
	if len(moving):
		print(": ", end="")
	str_buf = ""
	for i in range(len(moving)):
		if i != len(moving)-1:
			str_buf += moving[i]+", "
		else:
			str_buf += moving[i]
	print(str_buf)
	print("Winners:")
	for person in sorted(winners,key = lambda x:x.i):
		print(str(person))
		print("Rewards:")
		for reward in winner.rewards:
			print("    {}".format(reward.name))
		print()
	



