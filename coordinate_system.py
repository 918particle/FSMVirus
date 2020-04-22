from numpy import array,zeros
from random import randint
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
		self.space = zeros((self.maxX-self.minX+1,self.maxY-self.minY+1))
		self.generate_food()
	def food(self,x=0,y=0,val=0):
		self.space[x,y] += val
	def is_food(self,x=0,y=0):
		if(self.space[x,y]>0):
			return '1'
		else:
			return '0'
	def generate_food(self):
		for x in range(self.minX,self.maxX+1,1):
			for y in range(self.minY,self.maxY+1,1):
				i = x-self.minX
				j = y-self.minY
				self.food(i,j,randint(-1,1))