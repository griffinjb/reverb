# Let's go

# Paradigm: Search algorithm

from math import sqrt
import numpy as np

# Simple Room Class
class room:
	shape = ''
	parameters = []
	inner_outer = '' 		# stay inside shape or outside shape

	def __init__(self,shape='cubic',parameters=[],inner_outer='inner'):
		self.shape = shape
		self.parameters = parameters
		self.inner_outer = inner_outer

	def set_dims(parameters=[]):
		self.parameters = parameters	

	# boundary is considered inside
	def in_or_out(self,x,y,z):
		if self.shape == 'cubic':
			l = [x,y,z]
			inbound = 1
			cctr = 0
			comp = 1

			for p in self.parameters:
				if comp:
					if l[cctr] < p:
						inbound = 0
					comp = 1-comp

				else:
					if l[cctr] > p:
						inbound = 0
					comp = 1-comp
					cctr += 1

			if self.inner_outer == 'outer':
				inbound = 1-inbound

			return(inbound)


class ray:
	heading = np.array([0.0,0.0,0.0])
	position = np.array([0.0,0.0,0.0])
	timestep = .001
	speed = 323.0 # m/s speed of sound
	target = np.array([0.0,0.0,0.0])
	rooms = []


	def __init__(self,heading=np.array([0.0,0.0,0.0]),position=np.array([0.0,0.0,0.0]),target=np.array([0.0,0.0,0.0]),room=[]):
		self.heading = heading
		self.position = position
		self.target = target
		self.room = room

	def update_position(self):
		delta = self.speed * self.timestep
		delta = delta * self.heading
		self.position = np.add(self.position,delta,casting='unsafe')
		self.position += delta

		while not self.room_check():
			self.reflect()


	def reflect(self):
		

	def room_check(self):
		for rm in self.rooms:
			if not rm.in_or_out(self.position[0],self.position[1],self.position[2]):
				return(False)
		return(True)


	def distance_to_target(self):
		dist = 0
		for i,j in zip(self.position,self.target):
			dist += (i-j)*(i-j)
		return(sqrt(dist))


if __name__ == '__main__':
	# initialize room boundary surface
	rm1 = room(shape='cubic',parameters=[-3,3,-3,3,-3,3])
	rm2 = room(shape='cubic',parameters=[-3,3,-3,3,-3,3],inner_outer='outer')
	# test ray
	ra1 = ray(heading=np.array([1,1,1]),position=np.array([0,0,0]),target=np.array([2,2,2]),rooms=[rm1])

	# initialize source and destination position

	#

