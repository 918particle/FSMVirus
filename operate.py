import fsm
import coordinate_system
import constants

class Operate():
	def __init__(self,cs,fsm_list):
		self.main_coordinate_system = cs
		self.main_fsm_list = fsm_list
		self.new_fsm_list = []
		self.turn_count = 0
		self.main_coordinate_system.generate_food()
	def run(self):
		self.turn_count+=1
		for current_fsm in self.main_fsm_list:
			current_fsm.act(self.main_coordinate_system.is_food(current_fsm.pos_x,current_fsm.pos_y))
			#Phase 1: movement
			if(current_fsm.get_state() == '00'):
				self.main_coordinate_system.move(current_fsm)
				continue
			#Phase 2: food consumption
			if(current_fsm.get_state() == '01'):
				self.main_coordinate_system.feed(current_fsm.pos_x,current_fsm.pos_y)
				continue
			#Phase 3: reproduction
			if(current_fsm.get_state() == '10'):
				self.new_fsm_list.append(fsm.FSM(current_fsm.pos_x,current_fsm.pos_y))
				continue
			#Phase 4: dying FSMs removed
			if(current_fsm.get_state() == '11'):
				self.main_fsm_list.remove(current_fsm)
				continue
		#Add new FSMs to main list
		if(len(self.new_fsm_list)>0):
			self.main_fsm_list.extend(self.new_fsm_list)
		self.new_fsm_list.clear()
		#Food movement
		self.main_coordinate_system.move_food()
		#Vaccination
		if(self.turn_count > constants.N_vacc):
			self.main_coordinate_system.vaccinate_population()

	def insert_fsm(self,x,y):
		self.main_fsm_list.append(fsm.FSM(x,y))
