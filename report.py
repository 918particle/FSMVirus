import operate
from numpy import array,ndindex,zeros
import constants

class Report():

	def __init__(self,oper,title,title2,times):
		self.main_operater = oper
		self.food_count = []
		self.turn_count = []
		self.virus_count = []
		self.output_title = title
		self.output_title2 = title2
		self.output_flag = True
		self.time_points = [constants.N_turns*i for i in times]

	def update(self):
		self.virus_count.append(len(self.main_operater.main_fsm_list))
		self.turn_count.append(self.main_operater.turn_count)
		self.food_count.append(sum(sum(self.main_operater.main_coordinate_system.space)))
		if(max(self.turn_count) >= constants.N_food and self.virus_count[-1]==0):
			self.output_flag = False

	def output(self):
		if(self.output_flag):
			fout = open(self.output_title,'w')
			n = max(self.turn_count)
			for i in range(0,n):
				output_string = str(self.turn_count[i])+" "+str(self.virus_count[i])+" "+str(self.food_count[i])+"\n"
				fout.write(output_string)
			fout.close()

	def reveal_virus(self,turn):
		if(turn in self.time_points and self.output_flag):
			fileString = self.output_title2+"_turn"+str(turn)+".dat"
			fout = open(fileString,'w')
			nx = self.main_operater.main_coordinate_system.space.shape[0]
			ny = self.main_operater.main_coordinate_system.space.shape[1]
			virus_array = zeros((nx,ny))
			for temp_fsm in self.main_operater.main_fsm_list :
				virus_array[temp_fsm.pos_x,temp_fsm.pos_y] += 1
			for i in range(0,nx):
				for j in range(0,ny):
					fout.write(str(virus_array[i,j]))
					fout.write(" ")
				fout.write("\n")
			fout.close()
