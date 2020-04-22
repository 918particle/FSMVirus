import fsm
import coordinate_system
import constants

class Operate():
	def __init__(self,cs,fsm_list):
		self.main_coordinate_system = cs
		self.main_fsm_list = fsm_list
		self.new_fsm_list = []
		self.turn_count = 0
	def run(self):
		self.turn_count+=1
		for current_fsm in self.main_fsm_list:
			#Phase 1: food is consumed
			if(current_fsm.get_state() == '01'):
				self.main_coordinate_system.food(current_fsm.pos_x,current_fsm.pos_y,-1)
				continue
			#Phase 2: new FSMs reproduced
			if(current_fsm.get_state() == '10'):
				self.new_fsm_list.append(fsm.FSM(current_fsm.pos_x,current_fsm.pos_y))
				continue
			#Phase 3: dying FSMs removed
			if(current_fsm.get_state() == '11'):
				print("died")
				self.main_fsm_list.remove(current_fsm)
				continue
			#Phase 4: Move/act
			current_fsm.act(self.main_coordinate_system.is_food(current_fsm.pos_x,current_fsm.pos_y))
		#Add new FSMs to main list
		if(len(self.new_fsm_list)>0):
			self.main_fsm_list.extend(self.new_fsm_list)
		self.new_fsm_list.clear()
		#Generate new food
		if(self.turn_count<constants.N_food):
			self.main_coordinate_system.generate_food()