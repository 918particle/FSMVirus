from numpy import array,ones
import random as r
import constants

class CoordinateSystem:
	def __init__(
		self,
		min_x=constants.cs_minX,
		max_x=constants.cs_maxX,
		min_y=constants.cs_minY,
		max_y=constants.cs_maxY):
		self.minX = int(min_x)
		self.maxX = int(max_x)
		self.minY = int(min_y)
		self.maxY = int(max_y)
		self.space = ones((self.maxX,self.maxY))
	def move(self,fsm):
		#Move up, down, left, or right with equal probability
		deltax = 0
		deltay = 0
		if(r.randint(0,1)):
			if(r.randint(0,1)):
				deltax = 1
			else:
				deltax = -1
		else:
			if(r.randint(0,1)):
				deltay = 1
			else:
				deltay = -1
		fsm.pos_x += deltax
		fsm.pos_y += deltay
		#Restrict movement to board...minimums typically 0
		if(fsm.pos_x>=constants.cs_maxX):
			fsm.pos_x = constants.cs_maxX-1
		if(fsm.pos_y>=constants.cs_maxY):
			fsm.pos_y = constants.cs_maxY-1
		if(fsm.pos_x<constants.cs_minX):
			fsm.pos_x = constants.cs_minX
		if(fsm.pos_y<constants.cs_minY):
			fsm.pos_y = constants.cs_minY
	def food(self,x=0,y=0,val=0):
		self.space[x,y] += val
	def is_food(self,x=0,y=0):
		if(self.space[x,y]>0):
			return '1'
		else:
			return '0'
	def generate_food(self):
		for x in range(self.minX,self.maxX):
			for y in range(self.minY,self.maxY):
				self.food(x,y,r.randint(-1,2))
	def remove_food(self):
		for x in range(self.minX,self.maxX):
			for y in range(self.minY,self.maxY):
				self.food(x,y,r.randint(-2,1))