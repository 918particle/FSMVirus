import fsm
import coordinate_system

class Operate():
	def __init__(self,cs,fsm_list):
		self.main_coordinate_system = cs
		self.main_fsm_list = fsm_list
		self.new_fsm_list = []
	def run(self):
		for current_fsm in self.main_fsm_list:
			#Phase 1: all FSMs in the fsm_list act or move
			current_fsm.act(self.main_coordinate_system.is_food(current_fsm.pos_x,current_fsm.pos_y))
			#Phase 2: food is consumed
			print(self.main_coordinate_system.is_food(current_fsm.pos_x,current_fsm.pos_y))
			print(current_fsm.get_state())
			if(self.main_coordinate_system.is_food(current_fsm.pos_x,current_fsm.pos_y) and current_fsm.get_state == '01'):
				self.main_coordinate_system.food(current_fsm.pos_x,current_fsm.pos_y,-1)
			#Phase 3: new FSMs reproduced
			if(current_fsm.get_state() == '10'):
				new_fsm_list.append(fsm.FSM(current_fsm.pos_x,current_fsm.pos_y))
			#Phase 4: dying FSMs removed
			if(current_fsm.get_state() == '11'):
				del main_fsm_list[current_fsm]
		#Add new FSMs to main list
		if(len(self.new_fsm_list)>0):
			self.main_fsm_list.append(self.new_fsm_list)
		self.new_fsm_list.clear()
		self.main_coordinate_system.generate_food()