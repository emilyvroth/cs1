'''
This file containsed the universe class, as well as a class for reward and portal in order to make formatting simpler later on
'''
class Universe(object):
	'''
	represents a universe with a name, rewards, and people in the multi-verse game. 
	'''
	def __init__(self, name, rewards, portals, i):
		'''
		initializer for Universe with the name of the Universe, a list of rewards
		and a list of portals in it, and an index i
		'''
		self.name = name
		self.rewards = rewards
		self.portals = portals
		self.i = i

	def __str__(self):
		'''
		Formtting a multi-line string of output for each Universe
		Prints 'None' under Rewards and Portals section if there are none
		'''
		s = "Universe: {} ({} rewards and {} portals)\n".format(self.name, len(self.rewards), len(self.portals))
		s += "Rewards:\n"
		if len(self.rewards)>0:
			for i in range(len(self.rewards)):
				s += str(self.rewards[i]) + "\n"
		else:
			s += "None\n"
		s += "Portals:\n"
		if len(self.portals)>0:
			for i in range(len(self.portals)):
				s += str(self.portals[i]) + "\n"
		else:
			s += "None\n"
		return s


class Reward(object):
	'''
	The reward class to initialize, format a string, and add the point values of rewards in a universe
	'''
	def __init__(self, x, y, points, name, home_universe):
		'''
		Initializer with an x and y location, a number of points, a string name, and the universe they are in (to make returning them easier later)
		'''
		self.x = x
		self.y = y
		self.points = points
		self.name = name
		self.home_universe = home_universe

	def __str__(self):
		'''
		formating a string for each reward
		'''
		s = "at ({},{}) for {} points: {}".format(self.x, self.y, self.points, self.name)
		return s


class Portal(object):
	'''
	the portal class to initialize and format a string of the portals in a universe
	'''
	def __init__(self, from_name, from_x, from_y, to_name, to_x, to_y):
		'''
		initializer with location from_x, from_y in the old universe and locations 
		to_x,to_y in to_name, the new universe
		'''
		self.from_name = from_name
		self.from_x = from_x
		self.from_y = from_y
		self.to_name = to_name
		self.to_x = to_x
		self.to_y = to_y 

	def __str__(self):
		'''
		formatting a string for each portal
		'''
		s = "{}:({},{}) -> {}:({},{})".format(self.from_name, self.from_x, self.from_y, self.to_name, self.to_x, self.to_y)
		return s