from numpy import array,ones,zeros
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
		self.vacc_x_min = 0
		self.vacc_y_min = 0
		self.vacc_x_max = 0
		self.vacc_y_max = 0
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
		if(self.space[x,y]<0):
			self.space[x,y]=0
	def is_food(self,x=0,y=0):
		if(self.space[x,y]>0 and self.is_vaccinated(x,y)==False):
			return '1'
		else:
			return '0'
	def is_vaccinated(self,x=0,y=0):
		if(self.vacc_x_min<=x and self.vacc_x_max>=x):
			if(self.vacc_y_min<=y and self.vacc_y_max>=y):
				return True
			else:
				return False
		else:
			return False
	def generate_food(self):
		for x in range(self.minX,self.maxX):
			for y in range(self.minY,self.maxY):
				self.food(x,y,r.randint(-1,2))
	def remove_food(self):
		for x in range(self.minX,self.maxX):
			for y in range(self.minY,self.maxY):
				self.food(x,y,r.randint(-2,1))
	def vaccinate_area(self,xmin,xmax,ymin,ymax):
		self.vacc_x_min = xmin
		self.vacc_y_min = ymin
		self.vacc_x_max = xmax
		self.vacc_y_max = ymax