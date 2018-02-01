

class Ball(object):
	def __init__(self, x, y, dx, dy, radius, color):
		self.start_x = x
		self.start_y = y
		self.x = x
		self.y = y
		self.start_dx = dx
		self.start_dy = dy
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.color = color

	def position(self):
		return (self.x, self.y)

	def move(self):
		self.x += self.dx
		self.y += self.dy

	def bounding_box(self):
		return (self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)

	def get_color(self):
		return self.color

	def some_inside(self, maxx, maxy):
		return 0 < self.x + self.radius and \
		self.x - self.radius < maxx and \
		0 < self.y + self.radius and \
		self.y - self.radius < maxy

	def check_and_reverse(self, maxx, maxy):
		if 0 > self.x - self.radius or self.x + self.radius > maxx:
			self.dx = -self.dx
		if 0 > self.y - self.radius or self.y + self.radius > maxy:
			self.dy = -self.dy