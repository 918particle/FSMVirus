import random as r
import constants
import food
from food import Food

class CoordinateSystem:
	def __init__(self,max_x=constants.cs_maxX,max_y=constants.cs_maxY):
		self.maxX = int(max_x)
		self.maxY = int(max_y)
		self.space = []
		for i in range(self.maxX):
			current_row = []
			for j in range(self.maxY):
				current_row.append([])
			self.space.append(current_row)

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
		if(fsm.pos_x == self.maxX):
			fsm.pos_x = self.maxX-1
		if(fsm.pos_y == self.maxY):
			fsm.pos_y = self.maxY-1
		if(fsm.pos_x<0):
			fsm.pos_x = 0
		if(fsm.pos_y<0):
			fsm.pos_y = 0
		return [fsm.pos_x,fsm.pos_y]
	def is_food(self,x,y):
		if(self.space[x][y]):
			n = len(self.space[x][y])
			for i in range(n):
				current_food = self.space[x][y][i]
				if(current_food.get_state() == '1' and not current_food.is_vaccinated()):
					return '1'
			return '0'
	def feed(self,x,y):
		n = len(self.space[x][y])
		for i in range(n):
			current_food = self.space[x][y][i]
			if(current_food.get_state() == '1' and not current_food.is_vaccinated()):
				self.space[x][y][i].toggle_state()
				break
	def generate_food(self):
		for x in range(self.maxX):
			for y in range(self.maxY):
				for k in range(constants.N_p):
					self.space[x][y].append(Food(x,y))
	def move_food(self):
		for i in range(self.maxX):
			for j in range(self.maxY):
				k = 0
				while k < len(self.space[i][j]):
					new = self.move(self.space[i][j][k])
					if(new[0] != i or new[1] != j):
						self.space[new[0]][new[1]].append(self.space[i][j][k])
						self.space[i][j].pop(k)
					k+=1
	def vaccinate_population(self):
		for i in range(self.maxX):
			for j in range(self.maxY):
				n = len(self.space[i][j])
				for k in range(n):
					self.space[i][j][k].vaccinate()
