import Universe
from math import *

class Person(object):
	'''
	the person class is used to contain the information about a person in the multiverse, and see if they are near any objects
	'''
	def __init__(self, name, radius, home_universe, x, y, dx, dy, current_universe, i):
		'''
		initializes a person with their name, radius, home universe, x and y location, dx and dy speed, 
		their current universe and the number of rewards they have, andan index i

		as people stop, their speed is set to 0, so finaldx and finaldy are implemented to keep track of the speed, but dont actually move 
		the person and dont ever get set to 0 in the main code
		'''
		self.name = name
		self.radius = radius
		self.home_universe = home_universe
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.current_universe = current_universe
		self.rewards = []
		self.finaldx = dx
		self.finaldy = dy
		self.i = i

	def __str__(self):
		'''
		formats a two line srting of information about each person, updating the final value of dx and dy to the current values each time
		'''
		#self.finaldx = self.dx
		#self.finaldy = self.dy
		s = "{} of {} in universe {}\n".format(self.name, self.home_universe, self.current_universe)
		s += "    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points".format(self.x, self.y, self.finaldx, self.finaldy, len(self.rewards), self.get_value())
		return s

	def pick_up_treasure(self, reward):
		'''
		if a person is near enough to treasure, do this: picking up the treasure and adjusting the speed accordingly
		'''
		self.rewards.append(reward)
		n = len(self.rewards)
		self.dx = self.dx - (n%2)* (n/6)*self.dx
		self.dy = self.dy - ((n+1)%2)* (n/6)*self.dy
			

	def near_treasure(self, reward):
		'''
		checks if a person is near enough to pick up a reward based on equation provided
		'''
		return not self.stopped() and sqrt((self.x-reward.x)**2+(self.y-reward.y)**2) <= self.radius


	def near_edge(self, minx = 0, miny = 0, maxx=1000, maxy=1000):
		'''
		checks if a person has reached the edge of the board, set in values for min (0,0) and max (1000,1000) so they can easily be changed later if it was necessary
		'''
		if self.stopped():
			return False
		if self.x <= minx or self.x >= maxx or self.y <= miny or self.y >= maxy:
			return True
		return False

	def stop(self):
		'''
		stops a person by setting their person to 0, happens if they hit an edge or later if speed falls below a 10
		'''
		self.dx = 0
		self.dy = 0

	def near_other(self, other):
		'''
		checks if a person is near enough to collide with another person
		'''
		if self.current_universe == other.current_universe and not self.stopped() and not other.stopped():
			if sqrt((self.x - other.x)**2 + (self.y - other.y)**2) <= self.radius + other.radius:
				return True
		return False


	def collide(self):
		'''
		will drop the first object a person picked up (later to be returned to the universe it came from, and adjusts their speed/direction accordingly)
		'''
		if len(self.rewards) > 0:
			r1 = self.rewards.pop(0)
			n = len(self.rewards)
			self.dx = -(self.dx + (n%2)* (n/6)*self.dx)
			self.dy = -(self.dy + ((n+1)%2)* (n/6)*self.dy)
		else:
			r1 = None
		return r1

	def near_portal(self, portal):
		'''
		checks if a person is near a portal
		'''
		return not self.stopped() and sqrt((self.x - portal.from_x)**2+(self.y - portal.from_y)**2)<= self.radius


	def go_through_portal(self, portal):
		'''
		transports a person through a portal to the new universe at spot (x,y), if they are near a portal 
		'''
		self.current_universe = portal.to_name
		self.x = portal.to_x
		self.y = portal.to_y

	def get_value(self):
		'''
		gets the total points value for each person for their rewards
		'''
		return sum([reward.points for reward in self.rewards])

	def can_move(self):
		'''
		seeing if the person has a high enough speed to move in the current step
		'''
		if abs(self.dx) >= 10 and abs(self.dy) >= 10:
			return True
		return False

	def move(self):
		'''
		increments the position of the person in order to move them by their speed provided
		'''
		self.x += self.dx
		self.y += self.dy

	def stopped(self):
		'''
		returns True or False if the person has a speed of 0 or not
		'''
		return self.dx == 0 and self.dy == 0



